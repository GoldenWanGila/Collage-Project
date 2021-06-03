from apyori import apriori
import pandas as pd

stations = ['Changhua','Chenggong','Fengyuan','Taichung','Taiyuan','Xinwuri','Yuanlin']
for station in stations:
    path = r'model/Taichung/AssociativeAnalysis/inputs/railway_%s.csv'%station
    data = pd.read_csv(path)

    cols_to_use = ['time','num','delay']
    X = data[cols_to_use].copy()

    X = X.astype(str)
    X = X.values.tolist()

    association_rules = apriori(X,min_support=0.004, min_confidence=0.7,min_lift=5,min_length=3)
    association_results = list(association_rules)

    file = open(r'model\Taichung\AssociativeAnalysis\outputs\%sResult.txt'%station,'w')

    # for item in association_results:
    #     print(list(item[2][0][0]))
    # exit()

    for item in association_results:
        file.write("Rule: "+str(list(item[2][0][0]))+'->'+str(list(item[2][0][1]))+'\n')
        file.write('Support: '+str(item[1])+'\n')
        file.write('Confidence: '+str(item[2][0][2])+'\n')
        file.write('Lift: '+str(item[2][0][3])+'\n')
        file.write('==============================================='+'\n')