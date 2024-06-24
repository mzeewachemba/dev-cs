import torch
from torch import nn
from torch.autograd import Variable
import math

class PositionalEncoding(nn.Module):
    def __init__(self, embedding_dim, max_seq_length=512, dropout=0.1):
        super(PositionalEncoding, self).__init__()
        self.embedding_dim = embedding_dim
        self.dropout = nn.Dropout(dropout)
        
        # Create a positional encoding matrix with shape (max_seq_length, embedding_dim)
        pe = torch.zeros(max_seq_length, embedding_dim)
        for pos in range(max_seq_length):
            for i in range(0, embedding_dim, 2):
                pe[pos, i] = math.sin(pos / (10000 ** (2 * i / embedding_dim)))
                pe[pos, i + 1] = math.cos(pos / (10000 ** ((2 * i + 1) / embedding_dim)))
        
        pe = pe.unsqueeze(0)  # Add a batch dimension
        self.register_buffer('pe', pe)

    def forward(self, x):
        # Scale the input embeddings by the square root of the embedding dimension
        x = x * math.sqrt(self.embedding_dim)
        
        # Get the sequence length of the input
        seq_length = x.size(1)
        
        # Slice the positional encoding matrix to match the sequence length of the input
        pe = Variable(self.pe[:, :seq_length], requires_grad=False).to(x.device)
        
        # Add the positional encoding to the input embeddings
        x = x + pe
        
        # Apply dropout to the resulting embeddings
        x = self.dropout(x)
        
        return x
