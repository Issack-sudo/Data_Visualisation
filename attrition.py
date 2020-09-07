import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
file='employee.xlsx'
df1=pd.read_excel(file,sheet_name='Existing employees')


#print(df1.head())
#print(df1.info())

#print(df1.describe())
left_count=df1.count()
plt.bar(left_count.index.values,left_count)
plt.xlabel('Employees left comppany')
plt.ylabel('Number of Employees')
#plt.show()
print(left_count.value_counts())

#number of Projects
num_projects=df1.groupby('number_project').count()
plt.bar(num_projects.index.values,num_projects['satisfaction_level'])
plt.xlabel('Number of Projects')
plt.ylabel('Number of Employees')
#plt.show()

#Time spent in Company
time_spent =df1.groupby('time_spend_company').count()
plt.bar(time_spent.index.values,time_spent['satisfaction_level'])
plt.xlabel('Number of Years Spend in Company')
plt.ylabel('Number of Employees')
plt.show()

#Subplots using Seaborn
features=['number_project','time_spend_company','Work_accident', 'promotion_last_5years','dept','salary']
fig=plt.subplots(figsize=(10,15))
for i, j in enumerate(features):
    plt.subplot(4, 2, i+1)
    plt.subplots_adjust(hspace = 1.0)
    sns.countplot(x=j,data = df1)
    plt.xticks(rotation=90)
    plt.title("No. of employee")
    #plt.show()

fig=plt.subplots(figsize=(10,15))
for i, j in enumerate(features):
    plt.subplot(4, 2, i+1)
    plt.subplots_adjust(hspace = 1.0)
    sns.countplot(x=j,data = df1,)
    plt.xticks(rotation=90)
    plt.title("No. of employee")
    plt.show()

