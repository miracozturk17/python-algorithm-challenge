#!/usr/bin/env python
# coding: utf-8

# In[93]:


from sklearn import datasets
import pandas as pan
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plot
import seaborn as sea


# In[94]:


iris_dataset = datasets.load_iris()


# In[95]:


print(iris_dataset)


# In[96]:


print(iris_dataset.target_names)

print(iris_dataset.feature_names)


# In[97]:


print(iris_dataset.data[0:10])


# In[98]:


print(iris_dataset.target)


# In[99]:


salt_data=pan.DataFrame({
    'sepal length':iris_dataset.data[:,0],
    'sepal width' :iris_dataset.data[:,1],
    'petal length':iris_dataset.data[:,2],
    'petal width' :iris_dataset.data[:,3],
    'species'     :iris_dataset.target
})


# In[100]:


salt_data.head()


# In[101]:


X=salt_data[['sepal length', 'sepal width', 'petal length', 'petal width']]
y=salt_data['species']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, shuffle=True)


# In[102]:


clf=RandomForestClassifier(n_estimators=120)

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)


# In[103]:


print("Accuracy Value:",metrics.accuracy_score(y_test, y_pred))


# In[104]:


clf.predict([[1, 2, 3, 4]])


# In[105]:


clf=RandomForestClassifier(n_estimators=120)


# In[106]:


clf.fit(X_train,y_train)


# In[107]:


RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=0,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)


# In[108]:


feature_imp = pan.Series(clf.feature_importances_,index=iris_dataset.feature_names).sort_values(ascending=False)


# In[109]:


feature_imp


# In[110]:


sea.barplot(x=feature_imp, y=feature_imp.index)

plot.xlabel('Feature Importance Score')
plot.ylabel('Features')
plot.title("Visualizing Important Features")
plot.show()


# In[111]:


X=salt_data[['petal length', 'petal width','sepal length']]


# In[112]:


y=salt_data['species']                                


# In[113]:


X


# In[114]:


y


# In[127]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.75,shuffle=True, random_state=5)


# In[128]:


clf=RandomForestClassifier(n_estimators=120)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)


# In[130]:


print("Accuracy Value:",metrics.accuracy_score(y_test, y_pred))

