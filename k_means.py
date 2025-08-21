# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 09:27:36 2025

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('musteriler.csv')
print(veriler)


X = veriler.iloc[:,3:].values #yas ve hacimi aldik

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, init = 'k-means++')
kmeans.fit(X)
print(kmeans.cluster_centers_)
sonuclar = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++',random_state=123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)
    
plt.plot(range(1,11),sonuclar) 
plt.show()   

#kumeleme

kmeans = KMeans(n_clusters=3, init='k-means++',random_state=123)
y_pred = kmeans.fit_predict(X) 

 # gorsellestirme

plt.scatter(X[y_pred == 0,0], X[y_pred ==0,1], s=100, c='red',label='küme 1') # 0. kumeye dusen yas ve hacim degerleri bunlari kirmizi noktayla ciziyoruz nokta boyutu 100, kume 1 aciklama kumesindeki isim
plt.scatter(X[y_pred == 1,0], X[y_pred == 1,1], s=100, c= 'blue', label ='küme 2')
plt.scatter(X[y_pred == 2,0], X[y_pred == 2,1], s=100, c= 'green', label ='küme 3')

# kume merkezleri

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            s=300, c='yellow', marker='*', label='Merkezler')
            

plt.title("k-means kümeleme")
plt.xlabel("yaş")
plt.ylabel("müşteri hacmi")
plt.legend()
plt.show()

veriler["küme"] = y_pred
print(veriler.head())

# kumeleri anlamli bir sekilde isimlendirme
# yuksek hacim = 0 , orta hacim = 1 , dusuk hacim = 2

isimler = {0: 'yüksek hacim', 1: 'orta hacim', 2: 'dusuk hacim'}
veriler['küme ismi'] = veriler['küme'].map(isimler)
print(veriler.head())
