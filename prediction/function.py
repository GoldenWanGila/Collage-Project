import pandas as pd

stations = ['Changhua','Chenggong','Fengyuan','Taichung','Taiyuan','Xinwuri','Yuanlin']
for station in stations:
    path = r'prediction/inputs/railway_%s.csv' %station
    all_data = pd.read_csv(path)

    all_data.drop(all_data[all_data['delay'].isnull()].index, inplace=True)

    col_to_use = ['num','delay']
    data = all_data[col_to_use].copy()

    nums = []
    for num in data['num']:
        if num not in nums:
            nums.append(num)

    """
    tnd: times of no delay
    tsd: times of short delay
    tld: times of long delay
    msd: mean of short delay
    mld: mean of long delay
    """
    num_and_d = {}     # num and delay
    for index in range(len(nums)):
        ans = []
        df = data[data['num']==nums[index]]
        tnd = len(df[df['delay']==0])
        tld = len(df[df['delay']>=5])
        tsd = len(df)-tld-tnd
        msd = 0 if tsd == 0 else sum(list(df[df['delay']<5].delay))/tsd
        mld = 0 if tld == 0 else sum(list(df[df['delay']>=5].delay))/tld
        ans.append(str(nums[index]))
        ans.append(tnd/len(df))
        ans.append(tsd/len(df))
        ans.append(tld/len(df))
        ans.append(msd)
        ans.append(mld)
        num_and_d[index] = ans

    result = pd.DataFrame(num_and_d,index=['num','pnd','psd','pld','msd','mld']).T

    # print(result.head())
    result.to_csv(r'prediction/outputs/%s.csv'%station, index=False)
"""
outputs:
    車次 --> num
    no_delay的機率 --> pnd
    short_delay的機率 --> psd
    long_delay的機率 --> pld
    short_delay的平均delay長度 --> msd
    long_delay的平均delay長度 --> mld
"""