import sys
import torch

def main():
    print(torch.__version__)
    
if __name__ == "__main__":
    sys.exit(int(main() or 0))
