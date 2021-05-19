import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

path = "model/ClassificationAnalysis/inputs/railway.csv"
data = pd.read_csv(path)

data.drop(data[data['delay'].isnull()].index, inplace=True)

y = pd.to_numeric(data['delay'])
X = data.drop(['delay','id','date'], axis=1)


X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=1)
# print(X_train.head())

s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)
# print("Categorical variables:", object_cols)

label_X_train = X_train.copy()
label_X_valid = X_val.copy()

label_encoder = LabelEncoder()
for col in object_cols:
    label_X_train[col] = label_encoder.fit_transform(X_train[col])
    label_X_valid[col] = label_encoder.transform(X_val[col])

# print(label_X_train.head())
# print(y_train.head())

model = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=1)
model.fit(label_X_train, y_train)
preds = model.predict(label_X_valid)


print(accuracy_score(y_val, preds))

output = pd.DataFrame({'Exact delay':y_val, 'Predict delay':preds})
output.to_csv(r'model/ClassificationAnalysis/outputs/RandomForestTree/1stResult.csv', index=False)