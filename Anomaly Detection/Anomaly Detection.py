#!/usr/bin/env python
# coding: utf-8

# In[70]:


import seaborn as sns
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans #KMEANS OMP DURUM ANALIZI ICIN.
import warnings #HATA YONETIMI ICIN.
import numpy as nmp
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.cluster import DBSCAN


# In[71]:


iris_dataset = sns.load_dataset("iris")


# In[72]:


print(iris_dataset)


# In[73]:


iris_dataset.head()
print("##############DATA INFO##############")
iris_dataset.info()
print("#####################################")


# In[74]:


iris_dataset


# In[75]:


iris_dataset.describe()
iris_dataset.columns
print("##############DATA COLUMNS##############")
print(iris_dataset.columns)
print("##############DATA DESCRIBE#############")
print(iris_dataset.describe())
print("##############DATA NULL?################")
iris_dataset.isnull().sum()


# In[76]:


iris_dataset['species'].unique()
print(iris_dataset['species'].unique())


# In[77]:


print(iris_dataset.head(20))


# In[78]:


iris_dataset.iloc[2,4] = 'virginica'
iris_dataset.iloc[7,4] = 'virginica'
iris_dataset.iloc[9,4] = 'virginica'
iris_dataset.iloc[11,4] = 'virginica'


# In[79]:


print(iris_dataset.head(20))


# In[80]:


virginica_df = iris_dataset.loc[iris_dataset['species']=='virginica']
virginica_df = virginica_df.reset_index(drop=True) 


# In[81]:


virginica_df.head(5)


# In[82]:


virginica_np = virginica_df.iloc[:,:4].values
scaler = MinMaxScaler()
virginica_sc = scaler.fit_transform(virginica_np)


# In[83]:


sns.set()
plot.subplot(1,2,1)
sns.scatterplot(data=virginica_df, x='sepal_length', y='sepal_width')
plot.scatter(x=5.1, y=3.5, marker='*', color='red',linewidths = 2.1)
plot.scatter(x=4.6, y=3.1, marker='*', color='red',linewidths = 2.1)
plot.xlabel('sepal_length')
plot.ylabel('sepal_width')
plot.title('Sepal length v width')
print("##############USER FOLDER##############")
plot.savefig('Sepal length v width V-1') 
print("##############CUSTOM FOLDER############")
plot.savefig('C:/Users/user/Desktop/Sepal length v width V-1') 
plot.show()
plot.close()


# In[84]:


plot.subplot(1,1,1)
sns.scatterplot(data=virginica_df, x='petal_length', y='petal_width')
plot.scatter(x=1.4, y=0.2, marker='*', color='red')
plot.scatter(x=1.5, y=0.2, marker='*', color='red')
plot.xlabel('petal_length')
plot.ylabel('petal_width')
plot.title('Petal length v width')
plot.show()

plot.subplot(1,2,1)
sns.scatterplot(data=virginica_df, x='petal_length', y='petal_width')
plot.scatter(x=1.4, y=0.2, marker='*', color='red')
plot.scatter(x=1.5, y=0.2, marker='*', color='red')
plot.xlabel('petal_length')
plot.ylabel('petal_width')
plot.title('Petal length v width')
plot.show()

plot.subplot(1,2,2)
sns.scatterplot(data=virginica_df, x='petal_length', y='petal_width')
plot.scatter(x=1.4, y=0.2, marker='*', color='red')
plot.scatter(x=1.5, y=0.2, marker='*', color='red')
plot.xlabel('petal_length')
plot.ylabel('petal_width')
plot.title('Petal length v width')
plot.show()

plot.subplot(2,1,1)
sns.scatterplot(data=virginica_df, x='petal_length', y='petal_width')
plot.scatter(x=1.4, y=0.2, marker='*', color='red')
plot.scatter(x=1.5, y=0.2, marker='*', color='red')
plot.xlabel('petal_length')
plot.ylabel('petal_width')
plot.title('Petal length v width')
plot.show()

plot.subplot(2,2,1)
sns.scatterplot(data=virginica_df, x='petal_length', y='petal_width')
plot.scatter(x=1.4, y=0.2, marker='*', color='red')
plot.scatter(x=1.5, y=0.2, marker='*', color='red')
plot.xlabel('petal_length')
plot.ylabel('petal_width')
plot.title('Petal length v width')
plot.show()

plot.subplot(2,2,2)
sns.scatterplot(data=virginica_df, x='petal_length', y='petal_width')
plot.scatter(x=1.4, y=0.2, marker='*', color='red')
plot.scatter(x=1.5, y=0.2, marker='*', color='red')
plot.xlabel('petal_length')
plot.ylabel('petal_width')
plot.title('Petal length v width')
plot.show()


# In[85]:


#OMP_NUM_THREADS UYARISI ICIN KULLANILDI.

#1 YONTEM-KULLANIM
warnings.filterwarnings(action='once')

#2 YONTEM-KULLANIM
warnings.filterwarnings('ignore')

#MULTITHREAD DETAYLARI
#http://scv.bu.edu/examples/python/examples/parallel/multithread/


# In[86]:


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(virginica_sc)
    wcss.append(kmeans.inertia_)
plot.plot(range(1, 11), wcss)
plot.title('The Elbow Method',fontsize=20)
plot.xlabel('Number of clusters')
plot.ylabel('WCSS')
print("##############USER FOLDER##############")
plot.savefig('The Elbow Method') 
print("##############CUSTOM FOLDER############")
plot.savefig('C:/Users/user/Desktop/The Elbow Method') 
plot.show()


# In[87]:


kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 2).fit(virginica_sc)


# In[88]:


virginica_sc_clusters = kmeans.predict(virginica_sc)
virginica_sc_clusters_centers = kmeans.cluster_centers_
dist = [nmp.linalg.norm(x-y) for x, y in zip(virginica_sc, virginica_sc_clusters_centers[virginica_sc_clusters])]


# In[89]:


print("##############virginica_sc_clusters##############")
print(virginica_sc_clusters)
print(f"\n")
print("##############dist##############")
print(dist)
print(f"\n")
print("##############dist info##############")
print("MIN: "),print(nmp.min(list(dist)))
print("MAX: "),print(nmp.max(list(dist)))
print("AVG: "),print(nmp.average(list(dist)))
print("MED: "),print(nmp.median(list(dist)))


# In[90]:


km_y_pred = nmp.array(dist)
km_y_pred[dist >= nmp.percentile(dist, 95)] = 1
km_y_pred[dist <  nmp.percentile(dist, 95)] = 0


# In[91]:


virginica_clus = pd.concat([virginica_df,
                 pd.DataFrame(virginica_sc_clusters,columns=['Clusters'])],axis=1)


# In[92]:


print(virginica_clus.head(10))


# In[93]:


plot.subplot(1,2,1)
sns.scatterplot(data=virginica_clus, x='sepal_length', y='sepal_width', hue='Clusters', palette='deep')
plot.xlabel('sepal_length')
plot.ylabel('sepal_width')
plot.legend( loc='lower right')
plot.title('Sepal length v width')
plot.show()


# In[94]:


plot.subplot(1,2,2)
sns.scatterplot(data=virginica_clus, x='petal_length', y='petal_width', hue='Clusters', palette='deep')
plot.xlabel('petal_length')
plot.ylabel('petal_width')
plot.legend(loc='lower right')
plot.title('Petal length v width')
plot.show()


# In[95]:


dbs = DBSCAN(eps=0.75, min_samples=2, n_jobs=-1).fit(virginica_sc)


# In[96]:


pred_labels = dbs.labels_
n_clusters = len(set(pred_labels)) - (1 if -1 in pred_labels else 0)


# In[97]:


print("##############pred_labels##############")
print(pred_labels)
print(f"\n")
print("##############n_clusters###############")
print(n_clusters)
print(f"\n")
print("##############info#####################")
print('Tahmini küme sayısı: %d' % n_clusters)


# In[98]:


virginica_db = pd.concat([virginica_clus,pd.DataFrame(pred_labels,columns=['dbs_cluster'])],axis=1)


# In[99]:


virginica_db.head(15)

