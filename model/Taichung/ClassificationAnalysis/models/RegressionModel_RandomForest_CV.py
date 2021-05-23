import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_predict

path = "model/ClassificationAnalysis/Taichung/inputs/railway.csv"
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
    my_model = RandomForestRegressor(n_estimators=n_estimators, max_depth=8, random_state=0)
    preds = cross_val_predict(my_model, label_X, y, cv=10)
    return preds

preds = get_score(300)
times = 0
for index in range(len(preds)):
    if abs(int(list(preds)[index]) - list(y)[index]) < 2:
        times += 1
print(times/len(preds))