import sys
from IrisSVM import IrisSVM

def main():
    irissvm = IrisSVM()
    irissvm.visuvalize_sepal_data()
    irissvm.visuvalize_petal_data()
    irissvm.visualizeWithPCA()
    irissvm.svmAccuracy()
    irissvm.plotIrisDecisionBoundaries()
    irissvm.svmWithPCAReducedFeatures()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
