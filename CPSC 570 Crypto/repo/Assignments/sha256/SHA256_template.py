
import numpy as np
import sys

def SHA256(data):
    
    return 

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        data = sys.argv[1]
    else:
        data = 'CPSC-570 Blockchain and Crypto Technologies'
        
    print(f'Data: \"{data}\"')
    print(f'Bits in data: {len(data)*8}')
    hash = SHA256(data)
    print(f'Hash: \"{hash}\"')
