import pandas as pd

dataset = pd.read_csv("access_log.csv")
from sklearn.cluster import KMeans
model=KMeans()
dataset.drop('Unnamed: 0',inplace=True,axis=1)
freq = {} 
for item in dataset['IP']: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1
print(key_list)
import matplotlib.pyplot as plt
key_list = list(freq.keys()) 
val_list = list(freq.values()) 
plt.scatter(key_list,val_list)
from sklearn.cluster import KMeans
j=0
for i in key_list:
   print(i)
   i=i.strip("[ -]")
   if i.split(".")[-1]=='':
    i+="0"
   dataset['IP'][j]=(str_ip2_int(i))
   j=j+1
df1=pd.DataFrame({'IP':key_list})
df2=pd.DataFrame({'freq':val_list})
dataset=pd.concat([df1,df2],axis=1)
def str_ip2_int(s_ip):
    lst = [int(item) for item in s_ip.split('.')]
    int_ip = lst[3] | lst[2] << 8 | lst[1] << 16 | lst[0] << 24
    return int_ip
kmeans = KMeans(n_clusters=2)
kmeans.fit(df)
kmeans.cluster_centers_

import ipaddress
import os
j=0
for i in df['freq']:
    if int(i)>=300:
        ip=ipaddress.ip_address(df['IP'][j]).__str__()
        with open('Flooding_IPs.txt','a+') as file:
            file.write(""+ip+"\n")
        file.close()
    else:
        j+=1




