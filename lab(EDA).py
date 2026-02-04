
# 1.importin required python libraries(pandas,matplotlib,seaborn,numpy)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("successfully imported all modules")
print("pdandas version: ",pd.__version__)
print("numpy version: ",np.__version__)
#print("matplotlib.pyplot version: ",ptt.__version__)
print("seaborn version: ",sns.__version__)

# 2.loading the dataset into pandas dataframe
df=pd.read_csv("/home/user/Downloads/Customer Purchasing Behaviors.csv")

#3.displaying the number of rows and columns in dataset
print("dataset shape is (rows,column) : ",df.shape)

#4.print the columns names in dataset
print("column names: ",df.columns)

#5.first 5 rows of the dataset
print("first 5 rows of the dataset : ",df.head())

#6.checking data types of each column
print("datatype of each column : ",df.dtypes)

#7.identifying  the misssing values in each column
print("missing value of each column : ",df.isnull().sum())

#8.filling numeric missing column values with mean
n=df.select_dtypes(include=['int','float']).columns
df[n]=df[n].fillna(df[n].mean())
print("filling numeric missing column values with mean :",df[n])

#9.filling categorial missing column values with mode
col=df.select_dtypes(include=['object']).columns
for c in col:
    df[c]=df[c].fillna(df[c].mode()[0])
    print("filling categorial missing column values with mode",df[c])

#10.verifying no missing vakues remain
print("is there any null values:",df.isnull())

#11.mean for all numerical columns
mean_values=df.select_dtypes(include=['number']).mean()
print("mean values are:\n",mean_values)
print()

#12.median for all numerical columns
median_values=df.select_dtypes(include=['number']).median()
print("median values are:\n ",median_values)
print()

#13.standard deviation for all numerical columns
standard_values=df.select_dtypes(include=['number']).std()
print("standard deviation values are:\n",standard_values)
print()

#14.finding (min/max)values for all numerical values
min_values=df.select_dtypes(include=['number']).min()
max_values=df.select_dtypes(include=['number']).max()
print("min values are :\n",min_values)
print()
print("max values are:\n",max_values)

#15.generating summary using describe()
summary=df.describe()
print("summary:\n",summary)

#16.creating histogram for the purchase amount colummn "x-axis=purchase amount ;y-axis=frequency"
plt.hist(df['purchase_amount'],bins=20,color='skyblue',edgecolor='black')
plt.title('distribution of purchase amount')
plt.xlabel('purchase amount')
plt.ylabel('frequency')
plt.grid(axis='y',alpha=0.8)
plt.show()

#17.creating "bar chat" showing the count of customers by product category"x-axis:annual_income;y-axis:number of customers"
category_count=df['annual_income'].value_counts()
plt.figure(figsize=(12,7))
sns.barplot(x=category_count.index, y=category_count.values ,palette='viridis')
plt.title('ANNUAL INCOME')
plt.xlabel('annual_income')
plt.ylabel('Number of customers')
plt.xticks(rotation=45)
plt.show()

#18.boxplot of purchase amount column
sns.boxplot(x=df['purchase_amount'])
plt.title("Boxplot of purchae amount")
plt.show()

#19.creating corelation between age and purchase amount"x-axis:age ,y-axis:purchase amount"
correalation=df['age'].corr(df['purchase_amount'])
print(f"correalation between age and purchase amount(correalation: {correalation:.2f})")
plt.figure(figsize=(12,6))
sns.scatterplot(x=df['age'], y=df['purchase_amount'])
plt.title('RELATIONSHIP BTW AGE AND PURCHASE AMOUNT')
plt.xlabel('AGE')
plt.ylabel('PURCHASE_AMOUNT')
plt.xticks(rotation=45)
plt.show()

#20.corelation heatmap for numercal columns
corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True, cmap='coolwarm')
plt.title("correlation heatmap:")
plt.show()
























































































































































plt.show()




