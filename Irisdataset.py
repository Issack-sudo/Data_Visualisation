import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

irisData=pd.read_csv('Iris.csv')
print(irisData.head())
print(irisData.describe())
print(irisData.corr())

feature=irisData[{"SepalLengthCm","SepalWidthCm",
                  "PetalLengthCm","PetalWidthCm"
                 }]
targetVarible=irisData.Species
featureTrain,featureTest,targetTrain,targetTest=train_test_split(feature,targetVarible,test_size=.3)

model=DecisionTreeClassifier()
fitteModel=model.fit(featureTrain,targetTrain)
predictions=fitteModel.predict(featureTest)

print(confusion_matrix(targetTest,predictions))
print(accuracy_score(targetTest,predictions))
