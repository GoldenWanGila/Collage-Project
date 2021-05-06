from apyori import apriori
import pandas as pd

path = 'model/AssociativeAnalysis/inputs/railway.csv'
data = pd.read_csv(path)

cols_to_use = ['time','Station','num','delay']
X = data[cols_to_use].copy()

X = X.astype(str)
X = X.values.tolist()

association_rules = apriori(X,min_support=0.001, min_confidence=0.1,min_lift=3,min_length=2)
association_results = list(association_rules)

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: "+items[0]+'->'+items[1])
    print('Support: '+str(item[1]))
    print('Confidence: '+str(item[2][0][2]))
    print('Lift: '+str(item[2][0][3]))
    print('===============================================')