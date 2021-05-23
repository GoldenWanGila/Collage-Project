import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score

path = r"model/Taichung/inputs/railway.csv"
data = pd.read_csv(path)

data.drop(data[data['delay'].isnull()].index, inplace=True)

y = data['delay']

X = data.drop(['delay','id','date'], axis=1)

object_cols = [cname for cname in X.columns if X[cname].dtype=='object']
# print("Categorical variables:", object_cols)

label_X = X.copy()

label_encoder = LabelEncoder()
for col in object_cols:
    label_X[col] = label_encoder.fit_transform(label_X[col])

def get_score(n_estimators: int):
    my_model = RandomForestClassifier(n_estimators=n_estimators, max_depth=8, criterion='entropy', random_state=0)
    scores = cross_val_score(my_model, label_X, y, cv=10, scoring='accuracy')
    return scores.mean()

print('Score of n_estimators = %d：'%(300), get_score(300))