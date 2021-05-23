from apyori import apriori
import pandas as pd

path = 'model/AssociativeAnalysis/inputs/railway.csv'
data = pd.read_csv(path)

cols_to_use = ['time','Station','num','delay']
X = data[cols_to_use].copy()

X = X.astype(str)
X = X.values.tolist()

association_rules = apriori(X,min_support=0.01, min_confidence=0.8,min_lift=5,min_length=2)
association_results = list(association_rules)

times = '6th'
file = open(r'model\AssociativeAnalysis\outputs\%sResult.txt'%times,'w')

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    file.write("Rule: "+items[0]+'->'+items[1]+'\n')
    file.write('Support: '+str(item[1])+'\n')
    file.write('Confidence: '+str(item[2][0][2])+'\n')
    file.write('Lift: '+str(item[2][0][3])+'\n')
    file.write('==============================================='+'\n')