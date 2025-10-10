import pandas as pd
import numpy as np
import pickle
df = pd.read_csv(r"C:\Users\kapil\Downloads\Data-Mining-for-automated-personality-classification-main\Data-Mining-for-automated-personality-classification-main\data-final.csv",sep="\t")

df.dropna(inplace=True)
df.drop(['dateload','testelapse','endelapse','IPC','screenw','screenh','introelapse','country','lat_appx_lots_of_err','long_appx_lots_of_err','EXT1_E', 'EXT2_E', 'EXT3_E',
       'EXT4_E', 'EXT5_E', 'EXT6_E', 'EXT7_E', 'EXT8_E', 'EXT9_E', 'EXT10_E',
       'EST1_E', 'EST2_E', 'EST3_E', 'EST4_E', 'EST5_E', 'EST6_E', 'EST7_E',
       'EST8_E', 'EST9_E', 'EST10_E', 'AGR1_E', 'AGR2_E', 'AGR3_E', 'AGR4_E',
       'AGR5_E', 'AGR6_E', 'AGR7_E', 'AGR8_E', 'AGR9_E', 'AGR10_E', 'CSN1_E',
       'CSN2_E', 'CSN3_E', 'CSN4_E', 'CSN5_E', 'CSN6_E', 'CSN7_E', 'CSN8_E',
       'CSN9_E', 'CSN10_E', 'OPN1_E', 'OPN2_E', 'OPN3_E', 'OPN4_E', 'OPN5_E',
       'OPN6_E', 'OPN7_E', 'OPN8_E', 'OPN9_E', 'OPN10_E'],axis=1,inplace=True)

selected_columns = ['EXT2','EXT4','EXT6','EXT10','OPN1','OPN2','OPN4','OPN6','AGR1','AGR3','AGR5','AGR7','CSN2','CSN4','CSN6','CSN8','EST2','EST4','EST5','EST6']
df[selected_columns]=df[selected_columns].replace([1,2,5,4],[5,4,1,2])

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5)
kmeans.fit(df)
pickle.dump(kmeans,open("model.pkl","wb"))
