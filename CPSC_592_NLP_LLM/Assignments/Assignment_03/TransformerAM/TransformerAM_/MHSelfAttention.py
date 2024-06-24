from pickle import NONE
import numpy as np
import torch
from einops import rearrange
from torch import nn

class MHSelfAttention(nn.Module):
    def __init__(self, dim, heads=8, dim_head=None, causal=True):
        """
        Multi-Head Self Attention Layer.
        
        :param dim: Input embedding dimension.
        :param heads: Number of attention heads.
        :param dim_head: Dimension of each attention head.
        :param causal: If True, applies causal mask for auto-regressive models.
        """
        super().__init__()
        self.dim_head = (int(dim / heads)) if dim_head is None else dim_head
        _dim = self.dim_head * heads
        self.heads = heads
        self.causal = causal
        
        # Linear layers to generate query, key, value matrices
        self.to_qkv = nn.Linear(dim, _dim * 3, bias=False)
        # Output linear transformation
        self.W_out = nn.Linear(_dim, dim, bias=False)
        # Scaling factor for dot product attention
        self.scale_factor = self.dim_head ** -0.5
    
    def set_causal(self, causal):
        """
        Set the causal mask.
        
        :param causal: If True, applies causal mask for auto-regressive models.
        """
        self.causal = causal
    
    def forward(self, x, mask=None):
        """
        Forward pass for the multi-head self-attention layer.
        
        :param x: Input tensor of shape [batch, seq_len, dim].
        :param mask: Optional mask tensor of shape [seq_len, seq_len].
        :return: Output tensor after applying multi-head self-attention.
        """
        assert x.dim() == 3  # Ensure input is 3D tensor
        
        # Generate query, key, value matrices
        qkv = self.to_qkv(x)  # Shape: [batch, seq_len, dim*3]
        # Rearrange qkv to separate query, key, value and heads
        q, k, v = tuple(rearrange(qkv, 'b n (d k h) -> k b h n d', k=3, h=self.heads))
        # Shape of q, k, v: [batch, heads, seq_len, dim_head]
        
        # Compute scaled dot-product attention
        scaled_dot_prod = torch.einsum('b h i d, b h j d -> b h i j', q, k) * self.scale_factor
        # Shape of scaled_dot_prod: [batch, heads, tokens, tokens]
        
        # Apply causal mask if specified
        i = scaled_dot_prod.shape[2]
        j = scaled_dot_prod.shape[3]
        if self.causal:
            mask = torch.ones(i, j, device=x.device).triu_(j - i + 1).bool()
        
        # Apply the mask if provided
        if mask is not None:
            assert mask.shape == scaled_dot_prod.shape[2:]
            scaled_dot_prod = scaled_dot_prod.masked_fill(mask, -np.inf)
        
        # Compute attention weights
        attention = torch.softmax(scaled_dot_prod, dim=-1)
        # Compute output of the attention mechanism
        out = torch.einsum('b h i j, b h j d -> b h i d', attention, v)
        # Rearrange output to merge heads
        out = rearrange(out, 'b h n d -> b n (h d)')
        
        # Apply the final linear transformation
        return self.W_out(out)
