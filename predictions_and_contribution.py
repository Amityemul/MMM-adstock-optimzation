#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd
import statsmodels.api as sm
import re
import numpy as np
from statsmodels.regression.linear_model import OLSResults
import pandas as pd
class predictions_and_contribution:
        def __init__(self):
            self.best_model=OLSResults.load('best_model.pickle')
            self.res=pd.read_csv('best_parameters_for_media.csv')
        def generate_predictions(self,medias,data):
            for med in medias:
                coef=self.res[self.res['media']==med]['rate_of_change_w.r.t_sales'].values[0]
                beta=self.res[self.res['media']==med]['beta'].values[0]
                decay=self.res[self.res['media']==med]['decay'].values[0]
                lag=self.res[self.res['media']==med]['lag'].values[0]
                data[med]=data[med].shift(periods=lag,fill_value=0)
                data[med]=data[med]**beta
                current=data[med]*decay
                prev=data[med].shift(1,fill_value=0)*(1-decay)
                data[med]=current+prev
                data[med]=data[med]*coef
            data['sales_without_media']=self.best_model.params['const'] 
            data['predicted_sales']=data[medias].sum(axis=1)+data['sales_without_media']
            data.to_csv('predictions_and_contributions.csv',index=False)
            return(data)
               
#             del X['const']
#             X.columns=medias
#             return(X)


# In[117]:




