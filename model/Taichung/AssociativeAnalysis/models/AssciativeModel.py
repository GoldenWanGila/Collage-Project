from apyori import apriori
import pandas as pd

path = r'model/Taichung/AssociativeAnalysis/inputs/railway.csv'
data = pd.read_csv(path)

cols_to_use = ['time','Station','num','delay']
X = data[cols_to_use].copy()

X = X.astype(str)
X = X.values.tolist()

association_rules = apriori(X,min_support=0.003, min_confidence=0.8,min_lift=5,min_length=3)
association_results = list(association_rules)

times = '3rd'
file = open(r'model\Taichung\AssociativeAnalysis\outputs\%sResult.txt'%times,'w')

# for item in association_results:
#     print(list(item[2][0][0]))
# exit()

for item in association_results:
    file.write("Rule: "+str(list(item[2][0][0]))+'->'+str(list(item[2][0][1]))+'\n')
    file.write('Support: '+str(item[1])+'\n')
    file.write('Confidence: '+str(item[2][0][2])+'\n')
    file.write('Lift: '+str(item[2][0][3])+'\n')
    file.write('==============================================='+'\n')