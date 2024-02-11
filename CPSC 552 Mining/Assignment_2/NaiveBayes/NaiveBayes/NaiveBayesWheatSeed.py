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
    #loading wheat seed dataset
    df = pd.read_csv("E:/16.Data_for_assignments/CPSC552/wheat-seeds.csv") 
    
    #insert column names into the data
    df.columns = ['area' , 'perimeter' , 'compactness' , 'length_of_kernel' , 'width_of_kernel' , 'asymmetry_coefficient' , 'length_of_kernel_groove','class']
    
    #randomize wheat seed data
    dfrandom = df.sample(frac=1, random_state=1119).reset_index(drop=True)
    
    #transforming data from raw string , to first 7 columns of floats
    df1 = dfrandom.iloc[:,0:7].astype(float)
    
    #extracting the last column
    df2 = dfrandom.iloc[:,7]
    
    #joining 4 features and the last column with category name
    dfrandom = pd.concat([df1,df2],axis=1)
    print(dfrandom.head(6))
    
    #extract training and testing data
    dftrain = dfrandom.iloc[0:150,:]  #from 0 to 150
    print(dftrain)
    dftest = dfrandom.iloc[150:,:]  #from 150 to the last row
    print(dftest)
    
    #categorize the data into its classed 
    df_first_class = dfrandom[dfrandom['class'] == 1]
    print(df_first_class)
    df_second_class = dfrandom[dfrandom['class'] == 2]
    print(df_second_class)
    df_third_class = dfrandom[dfrandom['class'] == 3]
    print(df_third_class)

    #mean of each class for each column
    mean_first_class = df_first_class.iloc[:,0:7].mean(axis=0)
    print('mean of the first class\n',mean_first_class) 
    mean_second_class = df_second_class.iloc[:,0:7].mean(axis=0)
    print('mean of the second class\n',mean_second_class)
    mean_third_class = df_third_class.iloc[:,0:7].mean(axis=0)
    print('mean of the third class\n',mean_third_class)

    # #variance of each class
    varnc_first_class = df_first_class.iloc[:,0:7].var(axis=0)
    print('variance of the first class\n',varnc_first_class) 
    varnc_second_class = df_second_class.iloc[:,0:7].var(axis=0)
    print('variance of the second class\n',varnc_second_class)
    varnc_third_class = df_third_class.iloc[:,0:7].var(axis=0)
    print('variance of the third class\n',varnc_third_class)
    
    #predict based on the test set
    count_correct = 0
    for i in range(len(dftest)):
        x = dftest.iloc[i, 0:7].values
    
        # Calculate Gaussian probabilities for each class
        probC1 = compute_gaussian_probability(x, mean_first_class.values, varnc_first_class.values)
        probC2 = compute_gaussian_probability(x, mean_second_class.values, varnc_second_class.values)
        probC3 = compute_gaussian_probability(x, mean_third_class.values, varnc_third_class.values)
    
        # Combine probabilities
        probs = np.array([probC1, probC2, probC3])
        maxindex = probs.argmax(axis=0) #returns the idex of the maximum value      
        
        if dftest.iloc[i,7] == 1:
            index = 0
        if dftest.iloc[i,7] == 2:
            index = 1
        if dftest.iloc[i,7] == 3:
            index = 2
        if maxindex == index:
            count_correct = count_correct + 1
        #print(probC1,' ', probC2,' ', probC3,' class=',dftest.iloc[i,7])
    print('\n*******************************************')
    print('\nclassification accuracy\n =', count_correct/len(dftest)*100)
    print('\n*******************************************')

if __name__ == "__main__":
 sys.exit(int(main() or 0))


    
