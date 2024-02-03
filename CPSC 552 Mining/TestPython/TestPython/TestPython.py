import sys
import cv2
import torch

def main():
  print(cv2.__version__)         
  print(torch.__version__)
  print('testpy')

if __name__ == "__main__":
  sys.exit(int(main() or 0))
