import glob
# C:\Users\User\Desktop
for filename in glob.glob(r'C:\Users\User\Desktop\test\*.xlsx'):
    print(filename[-28:])
    print(filename[-9:-7]+'/'+filename[-7:-5])