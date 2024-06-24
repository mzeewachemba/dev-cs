from torch import nn
from MHSelfAttention import MHSelfAttention

class TransformerBlock(nn.Module):
    def __init__(self, dim, heads=8, dim_head=None, causal=False, 
                 pos_embed=None, dim_linear_block=1024, dropout=0.1):
        """
        Transformer Block with Multi-Head Self-Attention and Feed-Forward Neural Network.
        
        :param dim: Input embedding dimension.
        :param heads: Number of attention heads.
        :param dim_head: Dimension of each attention head.
        :param causal: If True, applies causal mask for auto-regressive models.
        :param pos_embed: Positional embedding (not used in this implementation).
        :param dim_linear_block: Dimension of the hidden layer in the feed-forward block.
        :param dropout: Dropout rate.
        """
        super().__init__()
        
        # Multi-Head Self-Attention layer
        self.mhsa = MHSelfAttention(dim=dim, heads=heads, dim_head=dim_head, causal=causal)
        # Dropout layer
        self.drop = nn.Dropout(dropout)
        # Layer normalization layers
        self.norm_1 = nn.LayerNorm(dim)
        self.norm_2 = nn.LayerNorm(dim)
        # Feed-Forward Neural Network
        self.linear = nn.Sequential(
            nn.Linear(dim, dim_linear_block),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(dim_linear_block, dim),
            nn.Dropout(dropout)
        )
    
    def set_causal(self, causal):
        """
        Set the causal mask for the Multi-Head Self-Attention layer.
        
        :param causal: If True, applies causal mask for auto-regressive models.
        """
        self.mhsa.set_causal(causal)
    
    def forward(self, x, mask=None):
        """
        Forward pass for the Transformer Block.
        
        :param x: Input tensor of shape [batch, seq_len, dim].
        :param mask: Optional mask tensor.
        :return: Output tensor after applying Multi-Head Self-Attention and Feed-Forward Neural Network.
        """
        # Apply Multi-Head Self-Attention with dropout and add residual connection
        y = self.norm_1(self.drop(self.mhsa(x, mask)) + x)
        # Apply Feed-Forward Neural Network with dropout and add residual connection
        return self.norm_2(self.linear(y) + y)
