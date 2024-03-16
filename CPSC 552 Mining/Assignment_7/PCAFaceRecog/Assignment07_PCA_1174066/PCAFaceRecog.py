import sys
import numpy as np
from PCARow import PCARow
from PCACol import PCACol
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def main():
    pcah = PCACol()  # Change to PCARow() to use row-wise version of data
    
    # ------------------- Column-wise version of PCA -------------------
    
    # Read training data
    [X, y, yseq] = pcah.read_images("E:/16.Data_for_assignments/CPSC552/ATTFacedataSet/Training/")
    print(X[0].shape)
    
    # Read testing data
    [Xtest, ytest, yseqt] = pcah.read_images("E:/16.Data_for_assignments/CPSC552/ATTFacedataSet/Testing/")
    
    # Perform PCA
    [E, EV, mu] = pcah.pca(pcah.asColumnMatrix(X), 100)  # Top 100 Eigen vectors
    print(EV.shape)
    
    # Visualization of Eigenfaces
    EF16 = []
    for i in range(min(len(X), 16)):
        e = EV[:, i].reshape(X[0].shape)
        EF16.append(pcah.normalize(e, 0, 255))  # Normalize for visualization
    print(len(EF16))
    pcah.subplot(title="Eigenfaces AT&T Facedatabase", images=EF16, rows=4, cols=4,
                 sptitle="Eigenface", colormap=cm.jet, filename="python_pca_eigenfaces.png")
    
    # Reconstruct projections of first n Eigen Faces
    steps = [i for i in range(10, min(len(X), 200), 20)]
    EF10 = []
    for i in range(min(len(steps), 16)):
        numEvs = steps[i]
        P = pcah.project(EV[:, 0:numEvs], X[0].reshape(-1, 1), mu)
        R = pcah.reconstruct(EV[:, 0:numEvs], P, mu)
        R = R.reshape(X[0].shape)
        EF10.append(pcah.normalize(R, 0, 255))
    
    # Plot reconstructed Eigen Faces
    pcah.subplot(title="Reconstruction AT&T Facedatabase", images=EF10, rows=4, cols=4,
                 sptitle="Eigenvectors", sptitles=steps, colormap=cm.gray,
                 filename="python_pca_reconstruction.png")
    
    # Compute and display recognition accuracy
    for xi in Xtest:
        pcah.projections.append(pcah.project(EV, xi.reshape(-1, 1), mu))
    
    imtest = 20  # Image number to test
    labelPredicted, index = pcah.predict(EV, Xtest[imtest], mu, y, yseq)
    
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(np.asarray(Xtest[index]), cmap=cm.gray)
    plt.xlabel(ytest[25])
    
    plt.subplot(1, 2, 2)
    plt.imshow(np.asarray(Xtest[imtest]), cmap=cm.gray)
    plt.xlabel(labelPredicted)
    plt.show()
    
    print("Actual label=" + ytest[imtest] + " Label predicted=" + labelPredicted)
    
    # Compute and display recognition accuracy
    i = 0
    accuracyCount = 0
    for xi in Xtest:
        labelPredicted, index = pcah.predict(EV, xi, mu, y, yseq)
        if labelPredicted == ytest[i]:
            accuracyCount = accuracyCount + 1
        i = i + 1
    print("Recognition accuracy = " + str(accuracyCount / i))
    
    # ---------------------------------------------------------

    # ----------------Row version of PCA-----------------------
    
    # pcah = PCARow() #for PCARow()       

    # [X,y,yseq] = pcah.read_images("E:/16.Data_for_assignments/CPSC552/ATTFacedataSet/Training/")
    # [Xtest,ytest,yseqt] = pcah.read_images("E:/16.Data_for_assignments/CPSC552/ATTFacedataSet/Testing/")
    # # X is a list f 112x92 2-d arrays, y is a list of numbers
    # [E, EV, mu] = pcah.pca(pcah.asRowMatrix(X), y) # top 100 Eigen vectors
    # # E is the Eigen value array, EV is the catenated Eigen vectors, mu is the mean image
    # # turn the first (at most) 16 eigenvectors into grayscale
    # # # images (note: eigenvectors are stored by column!)
    # EF16 = []
    # for i in range(min(len(X), 16)):
    #    e = EV[:,i].reshape(X[0].shape)
    #    EF16.append(pcah.normalize(e,0,255))
    #    # plot them and store the plot to "python_eigenfaces.pdf"
    # print(len(EF16))
    # pcah.subplot(title="Eigenfaces AT&T Facedatabase", images=EF16, rows=4, cols=4, sptitle=" Eigenface", colormap=cm.jet, filename="python_pca_eigenfaces.png")
    # # reconstruction steps
    # steps=[i for i in range(10, min(len(X), 200), 20)]
    # EF10 = []
    # for i in range(min(len(steps), 16)):
    #    numEvs = steps[i]
    #    P = pcah.project(EV[:,0:numEvs], X[0].reshape(1,-1), mu)
    #    R = pcah.reconstruct(EV[:,0:numEvs], P, mu)
    #    # reshape and append to plots
    #    R = R.reshape(X[0].shape)
    #    EF10.append(pcah.normalize(R,0,255))
    #    # plot them and store the plot to "python_reconstruction.pdf"
    # pcah.subplot(title="Reconstruction AT&T Facedatabase", images=EF10, rows=4, cols=4, sptitle=" Eigenvectors", sptitles=steps , colormap=cm.gray , filename=" python_pca_reconstruction.png")
    # for xi in X:
    #    pcah.projections.append(pcah.project(EV, xi.reshape(1,-1), mu))
    # labelPredicted, index = pcah.predict(EV,Xtest[11],mu,y,yseq)
    # plt.figure()
    # plt.subplot(1,2,1)
    # plt.imshow(np.asarray(Xtest[index]),cmap=cm.gray)
    # plt.xlabel(ytest[11])
    # plt.subplot(1,2,2)
    # plt.imshow(np.asarray(Xtest[11]),cmap=cm.gray)
    # plt.xlabel(labelPredicted)
    # plt.show()
    # print("actual label=" + ytest[11] + " label predicted=" + labelPredicted)
    # #compute recognition accuracy
    # i = 0
    # accuracyCount = 0
    # for xi in Xtest:
    #    labelPredicted,index = pcah.predict(EV,xi,mu,y,yseq)
    #    if (labelPredicted == ytest[i]):
    #        accuracyCount = accuracyCount+1
    #    i = i+1
    # print("recog accuracy = " + (str)(accuracyCount/i))
 
if __name__ == "__main__":
    sys.exit(int(main() or 0))
