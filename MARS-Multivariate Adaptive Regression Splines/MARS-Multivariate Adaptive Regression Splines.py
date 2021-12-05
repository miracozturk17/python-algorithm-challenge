#!/usr/bin/env python
# coding: utf-8

# In[3]:


# ÇALISMA ÜZERINDE KULLANILACAK KUTUPHANELERI DAHIL EDELIM.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


# ILGILI VERI SETINI CALISMAMIZA DAHIL EDELIM.
Weather_Data = pd.read_csv("C:\Anaconda\DataWeather.csv") 


# In[5]:


# VERI SETIMIZIN ONIZLEMESINI GERCEKLESTIRELIM.
Weather_Data


# In[6]:


# POTANSIYEL GIRDILERIMIZI BELIRLEYELIM.
Weather_Features = ['Temperature (C)', 'Wind Speed (km/h)', 'Pressure (millibars)']


# In[7]:


# GIRDILERIMIZI ONIZLEMESINI GERCEKLESTIRELIM.
Weather_Features


# In[8]:


# VERI ALANLARIMIZI WEATHER DATA VERI SETI ILE OZDESLESTIRELIM.
X = Weather_Data[Weather_Features]


# In[9]:


# WEATHER DATA VERI SETINDEKI HUMIDITY (NEM) PARAMETRESINI y DEGERINE ATAYALIM.
y = Weather_Data.Humidity


# In[10]:


# PARAMETRIK DEGERLERIMIZI GORSELLESTIRELIM.
plt.subplot(2,2,1)
plt.scatter(X['Temperature (C)'],y)
plt.subplot(2,2,2)
plt.scatter(X['Wind Speed (km/h)'],y)
plt.subplot(2,2,3)
plt.scatter(X['Pressure (millibars)'],y)


# In[11]:


# UC BOYUTLU GRAFIK OLUSTURMAK ICIN BIR PARAMETREMIZI (BASINC) INAKTIF ETMEMIZ GEREKMEKTEDIR.
# UST GRAFIKTE YER ALAN, BASINC DAGILIM GRAFIĞI TUTARSIZLIK SERGILEMEKTEDIR. (DIGER PARAMETRELERE GORE.) 
X = X.drop("Pressure (millibars)", 1)


# In[12]:


# UC BOYUTLU CIZIM OLUSTURALIM.
# BUNUN ICIN 3D plot KUTUPHANESINI ICERI AKTARALIM VE PARAMETRELERIMIZ ILE CIZIM OLUSTURALIM.
# BURADA Pressure - BASINC PARAMETRESI GOZ ARDI EDILDI.TEST ADINA DIGER PARAMETRELER GOZ ARDI EDILEBILIR.
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1 = X["Temperature (C)"]
x2 = X["Wind Speed (km/h)"]
ax.scatter(x1, x2, y, c='r', marker='o')

ax.set_xlabel('Temperature-Sıcaklık (C)')
ax.set_ylabel('Wind Speed-Ruzgar Hızı (km/h)')
ax.set_zlabel('Humidity-Nem')


# In[13]:


# REGRESYON ANALIZI ICIN KUTUPHANEMIZI CALISMAMIZA DAHIL EDELIM.
# mlr_model'IMIZI REGRESYON MODELI OLARAK TANIMLAYALIM.
# SON OLARAK MODELIMIZI YAPIMIZA UYDURUYORUZ.(ADAPTE) - fit(X,y): fitting
from sklearn.linear_model import LinearRegression
mlr_model = LinearRegression()
mlr_model.fit(X, y)


# In[14]:


# ILGILI PARAMETRELERIMIZI REGRESYON FORMULAZASYONU ICIN UYARLAYALIM.
# theta0 = intercept value = KESISIMIN DEGERI.
# theta1 - theta2 = REGRESSION COEFFICIENTS = REGRESYON KATSAYILARI
theta0 = mlr_model.intercept_
theta1, theta2 = mlr_model.coef_
theta0, theta1, theta2


# In[15]:


# PARAMETRELERIMIZI YAPILANDIRDIKTAN SONRA HERHANGI BIR GIRILECEK DEGER ICIN TAHMIN YAPALIM.
# ORNEGIN; 18,16
y_pred = mlr_model.predict([[18, 16]])
y_pred


# In[ ]:




