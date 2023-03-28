import pandas as pd

data_file=pd.read_csv('demodata.csv')

print("Enter Length Of SMA")
length=input()

MA=[]

for i in range(0,int(length)):
    MA.insert(i,0.0)
for i in range(0,len(data_file)-int(length)):
    MA.insert(i+int(length)-1,(data_file.loc[i:i+int(length)-1].close.sum())/float(length))
    
data_file["SMA"]=MA

data_file.to_csv('demodata.csv',index=False)
