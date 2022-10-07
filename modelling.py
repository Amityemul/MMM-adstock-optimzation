#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import statsmodels.api as sm
import re
import numpy as np
import joblib
class modelling:
        def __init__(self):
                self.lag_range=10
                self.betas=[0.6,0.7,0.8,0.9,1]
                self.decays=[0.6,0.7,0.8,0.9,1]
                self.top_n_features=3
                self.model_name='best_model.pickle'
        def divide_chunks(self,l, n):
                for i in range(0, len(l), n): 
                    yield l[i:i + n]
        def find_best_attributes_combination_and_model(self,all_media_transformed,sales_cols,dep_var):
                col_for_divide=[e for e in all_media_transformed.columns if e not in sales_cols]
                t=list(self.divide_chunks(col_for_divide,self.top_n_features))
                error=[]
                r_sq=[]
                models=[]
                params=[]
                for one in list(t[0]):
                    for two in list(t[1]):
                        for three in list(t[2]):
                            for four in list(t[3]):
                                for five in list(t[4]):
                                    for six in list(t[5]):
                                        for seven in list(t[6]):
                                            for eight in list(t[7]):
                                                for nine in list(t[8]):
                                                    lis=[one,two,three,four,five,six,seven,eight,nine]
                                                    Y=all_media_transformed[dep_var]
                                                    X=all_media_transformed[lis]
                                                    X = sm.add_constant(X)
                                                    model = sm.OLS(Y, X).fit()
                                                    r_sq.append(model.rsquared)
                                                    error.append(sum(model.bse))
                                                    models.append(model)
                                                    params.append(model.params)

                df=pd.DataFrame()
                df['model']=models
                df['error']=error
                df['r_squared']=r_sq
                df['model_coefficients']=params
                df.to_csv('all_combinations_results.csv',index=False)
                #criteria to select best model
                mod=df[(df['r_squared']==max(df['r_squared'])) & (df['error']==min(df['error']))]['model'].iloc[0]
                self.best_model=mod
                mod.save(self.model_name)
        def get_best_lag_decay_beta(self):
                res1=pd.DataFrame()
                for i in self.best_model.params[1:].index:
                    k=i.split('_',1)
                    medi=k[0]
                    k=re.findall(r'\d+(?:\.\d+)?', k[1])
                    y={'media':medi,'lag':k[0],'beta':k[1],'decay':k[2],'rate_of_change_w.r.t_sales':self.best_model.params[i]}
                    res1=res1.append(y,ignore_index=True)
                res1.to_csv('best_parameters_for_media.csv')
                return(res1)     


# In[ ]:




