from torch import nn
from TransformerBlock import TransformerBlock
from PositionalEncoding import PositionalEncoding
import torch

class SimpleTransformer(nn.Module):
    def __init__(self, dim, num_unique_tokens=256, num_layers=6, heads=8,
                 dim_head=None, max_seq_len=1024, causal=True):
        """
        Simple Transformer model.

        :param dim: Dimension of the embeddings and hidden states.
        :param num_unique_tokens: Number of unique tokens in the vocabulary.
        :param num_layers: Number of transformer layers.
        :param heads: Number of attention heads.
        :param dim_head: Dimension of each attention head.
        :param max_seq_len: Maximum sequence length.
        :param causal: If True, applies causal mask for auto-regressive models.
        """
        super().__init__()
        self.max_seq_len = max_seq_len
        self.causal = causal

        # Token embedding layer
        self.token_emb = nn.Embedding(num_unique_tokens, dim)
        # Positional encoding layer
        self.pos_enc = PositionalEncoding(dim, max_seq_length=max_seq_len)
        # List of transformer blocks
        self.block_list = [TransformerBlock(dim=dim, heads=heads,
                                            dim_head=dim_head, causal=causal) for _ in range(num_layers)]
        self.layers = nn.ModuleList(self.block_list)
        # Output layer
        self.to_logits = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_unique_tokens)
        )

    def set_causal(self, causal):
        """
        Set the causal flag for all transformer blocks.

        :param causal: If True, applies causal mask for auto-regressive models.
        """
        for b in self.block_list:
            b.set_causal(causal)

    def forward(self, x, mask=None):
        """
        Forward pass for the Simple Transformer.

        :param x: Input tensor of token indices with shape [batch, seq_len].
        :param mask: Optional mask tensor.
        :return: Output tensor with logits for each token.
        """
        # Apply token embedding
        x = self.token_emb(x)
        # Add positional encoding
        x = x + self.pos_enc(x)
        # Pass through each transformer block
        for layer in self.layers:
            x = layer(x, mask)
        # Apply final output layer
        return self.to_logits(x)
