import sys
from ucimlrepo import fetch_ucirepo  #using uci api itself 
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np



def main():
    #LOADING DATASET
    # fetch dataset 
    abalone = fetch_ucirepo(id=1) 
  
    # data (as pandas dataframes) 
    X = abalone.data.features 
    label_encoder = LabelEncoder()
    X.loc[:, 'Sex'] = label_encoder.fit_transform(X['Sex']).astype(float)
    X.loc[:, 'Sex'] = X['Sex'].astype(float)
    y = abalone.data.targets 
  
    # metadata 
    #print(abalone.metadata) 
  
    # variable information 
    #print(abalone.variables) 
    
    #PROCESSING DATASET
    df_data = pd.DataFrame(abalone.data.features)
    classes_df = pd.DataFrame(abalone.data.targets) 
    label_encoder = LabelEncoder()
    df_data['Sex'] = label_encoder.fit_transform(df_data['Sex']) # convert categorical variables to numerical using Label Encoding
    # df_all_data.astype(float) #convert all features into float
    # df_data['Sex'] = df_data['Sex'].astype(float)
    # print(df_data)
    # print(df_data.dtypes)
    
    # separating training and testing data
    # df_data_training = df_data[]

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,train_size=0.8, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,train_size=0.8,shuffle=False)
    X_train['Sex'] = label_encoder.fit_transform(X_train['Sex']) # convert categorical variables to numerical using Label Encoding
    # print(X_train)

    training_instances =  X_train.shape[0]
    # training_instances['Sex'] = training_instances['Sex'].astype(float)

    #SETTING number of neighbors
    k = 50
    
    #picking a test instance
    # test_instance = df_data.sample(1) #randomly
    # test_instance = df_data.iloc[2567,:]   #fixed sample
    test_instance = df_data.iloc[389,:]   #fixed sample

    
    #calculating distance
    distances_dict = {}
    
    for i in range(0, training_instances):
        d = np.linalg.norm(test_instance - X_train.iloc[i , :])
        distances_dict[i] = d
        # print(i)
    #sorting in ascending order
    distances_dict = sorted(distances_dict.items(), key=lambda x: x[1])
    # print(distances_dict)
    
    #nearest neignbors
    distances_dict_100 = distances_dict[:k]
    
    
    # print(distances_dict_100)
    
    #determining majority class
    # Convert the dictionary to a DataFrame
    distances_df = pd.DataFrame(distances_dict_100, columns=['index', 'distance'])
    # Set the 'index' column as the index of the DataFrame
    distances_df.set_index('index', inplace=True)

    # print(distances_df)

    # Merge the two DataFrames using index as the key
    result_df = pd.merge(distances_df, df_data, left_index=True, right_index=True)
    result_df = pd.merge(result_df, classes_df, left_index=True, right_index=True)

    print(result_df)
    
    print('mode is',result_df['Rings'].mode()[0])
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))

