# -*- coding: utf-8 -*-
"""final_assessment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EFkF58ocbLzRvTD7UXIjRD2u4jSDcqfI
"""

import pandas as pd

data = pd.read_csv('/content/train_LZdllcl.csv')

data.isna().sum()
#data.value_counts()


#mean and mode
data['previous_year_rating'] = data['previous_year_rating'].fillna(data['previous_year_rating'].mean())
#data['gender'] = data['gender'].fillna(data['gender'].mode()[0])
data['education'] = data['education'].fillna(data['education'].mode()[0])
#data['recruitment_channel'] = data['recruitment_channel'].fillna(data['recruitment_channel'].mode()[0])
#data['education'] = data['education'].fillna(data['education'].mode()[0])

data=pd.get_dummies(data,columns=['department','gender','education','recruitment_channel'])
data.head()

X=data.drop(columns=['employee_id','is_promoted','region'])
y=data['is_promoted']

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)

y_pred = model.predict(X_test)
print('F1 Score:', f1_score(y_test, y_pred))

"""**predicting with test data**"""

import pandas as pd
data2=pd.read_csv('/content/test_2umaH9m.csv')
data2.head()

data2.isnull().sum()

#mean and mode
data2['education']=data2['education'].fillna(data2['education'].mode()[0])
data2['previous_year_rating']=data2['previous_year_rating'].fillna(data2['previous_year_rating'].mean())

#encoding
data2=pd.get_dummies(data2,columns=['department','education','gender','recruitment_channel'])
data2.head()

test=data2.drop(['employee_id','region'],axis=1)
test.head()

from sklearn.preprocessing import StandardScaler
sc2=StandardScaler()
test=sc2.fit_transform(test)
result=model.predict(test)
len(result),result

sample=pd.read_csv('/content/sample_submission_M0L0uXE.csv')
# Assign the predictions to the 'is_promoted' column
sample['is_promoted']=result
sample.to_csv('solution.csv',index=False)