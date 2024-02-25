import sys
import numpy as np
import pandas as pd
import math

def compute_gaussian_probability(x , mean , var):  #calculates gaussian probabilities of each feature
    res = 1
    for i in range(0,len(x)):
        exponent = math.exp(-((x[i]-mean[i])**2 / (2 * var[i] )))
        res *= (1 / (math.sqrt(2 * math.pi * var[i]))) * exponent
    return res

def main():
    #loading iris dataset
    df = pd.read_csv("E:/16.Data_for_assignments/CPSC552/iris.csv") 
    
    #randomize iris data
    dfrandom = df.sample(frac=1, random_state=1119).reset_index(drop=True)
    
    #transforming data from raw string , to first 4 columns of floats
    df1 = dfrandom.iloc[:,0:4].astype(float)
    
    #extracting the last column
    df2 = dfrandom.iloc[:,4]
    
    #joining 4 features and the last column with category name
    dfrandom = pd.concat([df1,df2],axis=1)
    print(dfrandom.head(6))
    
    #extract training and testing data
    dftrain = dfrandom.iloc[0:100,:]  #from 0 to 100
    print(dftrain)
    dftest = dfrandom.iloc[100:,:]  #from 100 to the last row
    print(dftest)
    
    #categorize the data into classes
    dfsetosa = dfrandom[dfrandom['species'] == 'setosa']
    print(dfsetosa)
    dfversicolor = dfrandom[dfrandom['species'] == 'versicolor']
    print(dfversicolor)
    dfvirginica = dfrandom[dfrandom['species'] == 'virginica']
    print(dfvirginica)

    #mean of each class
    mean_setosa = dfsetosa.iloc[:,0:4].mean(axis=0)
    print('\nmean setosa\n',mean_setosa) 
    mean_versicolor = dfversicolor.iloc[:,0:4].mean(axis=0)
    print('\nmean versicolor\n',mean_versicolor)
    mean_virginica = dfvirginica.iloc[:,0:4].mean(axis=0)
    print('\nmean virginica\n',mean_virginica)

    #variance of each class
    var_setosa = dfsetosa.iloc[:,0:4].var(axis=0)
    print('\nvar setosa\n',var_setosa)
    var_versicolor = dfversicolor.iloc[:,0:4].var(axis=0)
    print('\nvar versicolor\n',mean_versicolor)
    var_virginica = dfvirginica.iloc[:,0:4].var(axis=0)
    print('\nvar virginica\n',var_virginica)

    
    #predict based on the test set
    count_correct = 0
    for i in range(len(dftest)):
        x = dftest.iloc[i, 0:4].values
    
        # Calculate Gaussian probabilities for each class
        probC1 = compute_gaussian_probability(x, mean_setosa.values, var_setosa.values)
        probC2 = compute_gaussian_probability(x, mean_versicolor.values, var_versicolor.values)
        probC3 = compute_gaussian_probability(x, mean_virginica.values, var_virginica.values)
    
        # Combine probabilities
        probs = np.array([probC1, probC2, probC3])
    
        maxindex = probs.argmax(axis=0) #returns the idex of the maximum value
        
        #mapping class values to indices
        if dftest.iloc[i,4] == 'setosa':
           index = 0
        if dftest.iloc[i,4] == 'versicolor':
           index = 1
        if dftest.iloc[i,4] == 'virginica':
           index = 2
         
        #comparing resulting index from naive bayes to the expected index           
        if maxindex == index:
           count_correct = count_correct + 1
           
    print('\n*******************************************')
    print('\nclassification accuracy =', count_correct/len(dftest)*100)
    print('\n*******************************************')

if __name__ == "__main__":
 sys.exit(int(main() or 0))


    
