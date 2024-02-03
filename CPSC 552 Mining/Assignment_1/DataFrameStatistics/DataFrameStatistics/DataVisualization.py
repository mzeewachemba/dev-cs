import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
  df = pd.read_csv('E:/16.Data_for_assignments/CPSC552/diabetes_temp_datasets_for_assignment_1.csv')
  pd.set_option('display.max_columns', None)  # to display all columns
  print('\nObtaining first 6 rows to see if we have right type of data\n',df.head(6))  

  # remove null data rows and duplicate rows
  dfn = df.dropna()
  print('\nDisplaying number of rows and column after dropping rows with null values\n',dfn.shape)
  dfc = dfn.drop_duplicates()
  print('\nDisplaying number of rows and column after deleting rows with duplicate values\n',dfc.shape)

  # plotting the histogram
  dfc.Age.plot(color="blue", kind="hist", bins=20)
  plt.title(label='Histogram of Age',loc='center')
  plt.xlabel("Age")
  plt.ylabel("frequency")
  plt.show()

  # histogram by groups of outcome as 0 or 1 
  dfc.hist(column='Age', by='Outcome')  
  plt.show()

  df2 = dfc[["Age", "Glucose"]] # dataframe with age and glucose attributes
  df2.plot(
      kind='hist',
      alpha=0.7,
      bins=30,
      title='Histogram Of Age,Glucose',
      rot=45,
      grid=True,
      figsize=(12, 8),
      fontsize=15,
      color=['#ff0000', '#00ff00']
  )
  plt.xlabel('Age/Glucose')
  plt.ylabel("Count");
  plt.show()

  sns.countplot(x="Outcome", data=dfc)
  plt.show()

  print('\nTotal of outcome for 0 and 1 is\n',dfc.Outcome.value_counts())  # outcome counts


  # plotting a pie chart for pregnancies
  sizes = dfc.Pregnancies.value_counts().values[0:9]
  labels = dfc.Pregnancies.value_counts().index[0:9]
  colors = ["green", "pink", "yellow", "purple", "grey", "blue", "plum", "orange", "red"]
  plt.title(label='Piechart for Pregnancies',loc='center')
  plt.pie(sizes, data=dfc, labels=labels, colors=colors, radius=1.0) # radius reduced to fit a pie chart into screen
  plt.show()
  
  # plotting a histogram for each attribute of the data
  df2 = (dfc.columns[0:-1])  # remove outcomes column
  dfc.hist(df2, bins=50, figsize=(20, 15))
  plt.show()

  # plotting heatmap, using df2 without the outcome column
  sns.heatmap(dfc[df2].corr(), annot=True) #creating a correlation matrix
  plt.title(label='Corelation Matrix',loc='center')
  plt.show()

if __name__ == "__main__":
  sys.exit(int(main() or 0))
