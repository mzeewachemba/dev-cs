import sys
import numpy as np
import pandas as pd


def main():
    
    df=pd.read_csv('E:/16.Data_for_assignments/CPSC552/diabetes_temp_datasets_for_assignment_1.csv')
    pd.describe_option('display.max_columns', None)  #display all columns
    
    print('Displaying the number of rows and columns in a dataframe\n', df.shape)
  
    print('\nObtaining first 6 rows to see if we have right type of data\n',df.head(6))
    
    print('\nObtaining last 7 rows to see if we have right type of data\n',df.tail(7))
    
    print('\nGetting information about dataframe,set verbose true for more details\n',df.info(verbose=True))
    #print(df.info(verbose=False)) #less details     

    print('\nData type details for each column\n', df.dtypes)
    
    print('\nGetting total Null values for each column\n',df.isna().sum())
    print('\nDuplicate values\n',df.duplicated().sum())
    
    # remove null data rows and dulicate rows
    dfn=df.dropna()
    print('\nDisplaying number of rows and column after dropping rows with null values\n',dfn.shape)
    df_distinct=dfn.drop_duplicates()
    print('\nDisplaying number of rows and column after deleting rows with duplicate values\n',df_distinct.shape)


    column_headers = list(df.columns.values)
    print('\nColumn Headings(names) :\n', column_headers)
    
    # removing last column to compute corelation btn data columns
    data_columns = column_headers[0:-1] #splicing to exclude last column
    print('\nPrinting data columns\n',data_columns)
    data_corr = df_distinct[data_columns].corr() # correlation between columns
    print('\nPrinting co relation data\n',data_corr)

    # max correlations for a feature
    corr_data = df_distinct.corr().abs()
    cbmi = corr_data["BMI"]  #select bmi to see how its corelated to other features
    corrbmi = cbmi.sort_values(ascending = False)
    print("\nsorted correlations--------")
    print(corrbmi)
    
    print('\nGetting statistical features from the data\n',df_distinct.describe())

    print('\nGetting no of distincts elements from the data\n',df_distinct.nunique())
    
    print('\nUnique values for pregnancies\n',df_distinct['Pregnancies'].unique())


    # combining columns from one dataframe to another new dataframe
    seriesBMI = df["BMI"]
    seriesGlucose = df["Glucose"]
    seriesOutcome = df["Outcome"]
    df_bmi_glcos_outcm = pd.concat([seriesBMI,seriesGlucose, seriesOutcome], axis=1) #joining attributes to create a new dataframe
    print('\nNew dataframe first 7 rows with bmi,glucose and outcome attributes\n',df_bmi_glcos_outcm.head(7))
    
    #filtering or removing rows from a dataframe based on criteria
    dffiltered = df_bmi_glcos_outcm[df_bmi_glcos_outcm['Glucose']<= 180]#getting all rows with glucose less than 180
    print('\nNumber of rows with glucose <= 180\n',len(dffiltered))
    print('\nNumber of rows with glucose <= 180(SAMPLE)\n',dffiltered.head())
    
    # change Outcome colum 1 and 0 classes to 1 and 2
    df_bmi_glcos_outcm['Outcome'] = df_bmi_glcos_outcm['Outcome'].map(lambda x: 1 if x ==1 else 2)#python lambda to change column values
    print('\nDataframe with outcome values changed to 1 and 2\n',df_bmi_glcos_outcm.head())

    # splicing dataframe to access particular row
    d1 = df_bmi_glcos_outcm.iloc[25,1] # glucose value in row 25
    print('\nglucose value in row 25\n',d1)
    
    d78 = df_bmi_glcos_outcm.iloc[78,0] # bmi value in row 78
    print('\nbmi value in row 78\n',d78)
    
    # select 10-13 rows into a new dataframe
    d2 = df_bmi_glcos_outcm.iloc[10:14,:] # splice to exlude 14th
    print('\n10-13 rows into a new dataframe without reseting index\n',d2.head())
    
    # select 10-13 rows into a new dataframe and reset index
    d3 = df_bmi_glcos_outcm.iloc[10:14,:].reset_index() # splice to exlude 14th
    print('\n10-13 rows into a new dataframe and reset index\n',d3.head())
    
    # select 10-13 rows into a new dataframe and reset index
    # drop=True to avoid old index being kept
    d3 = df_bmi_glcos_outcm.iloc[10:14,:].reset_index(drop=True) # splice to exlude 14th
    print('\n10-13 rows into a new dataframe and reset index and delete old index\n',d3.head())

if __name__ == "__main__":
    sys.exit(int(main() or 0))