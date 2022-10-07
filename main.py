#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import timeit
# #!/usr/bin/env python
# # coding: utf-8

# # In[8]:

# #required 
# from data_transformation import data_transformation
# from modelling import modelling
# from predictions_and_contribution import predictions_and_contribution
# from roi import roi_spend_contribution
# import pandas as pd
# import re
# from statsmodels.regression.linear_model import OLSResults
# import statsmodels.api as sm
# import numpy as np

# #inputs required by user
# medias=['TV', 'Digital',
#        'Sponsorship', 'Content Marketing', 'Online marketing', ' Affiliates',
#        'SEM', 'Radio', 'Other']
# level=['Year','Month']
# dep_var='revenue'
# sales_cols=level.copy()
# sales_cols.append(dep_var)
# #Data Required
# path_for_data='D:/MMM python project/final_data_for_modelling/sales_and_media_effects.csv'
# data=pd.read_csv(path_for_data)
# #Data Transformation for Modelling (add lag ,carryover and decay effect)
# dt=data_transformation()

# transformed_data=dt.add_lag_carryover_decay(data,medias,sales_cols,dep_var)

# modeling=modelling()
# #Find best values of lag,decay and beta for each media for which we get best regression results
# modeling.find_best_attributes_combination_and_model(transformed_data,sales_cols,dep_var)
# ##Getting best values of lag,decay and beta for each media for which we get best regression results.
# res=modeling.get_best_lag_decay_beta()




# In[4]:


res


# In[14]:


modeling.best_model.summary()


# In[8]:



pc=predictions_and_contribution()
predictions_and_contributions=pc.generate_predictions(medias,data.copy())


roi=roi_spend_contribution()
roi_spend_and_contribution=roi.roi_and_spend(data.copy(),predictions_and_contributions,level,medias)


# In[10]:


predictions_and_contributions


# In[11]:


roi_spend_and_contribution


# In[34]:


re_allocate_budgets=data.copy()


# In[36]:


re_allocate_budgets['TV']=0
re_allocate_budgets['Sponsorship']=0
re_allocate_budgets['Radio']=0
re_allocate_budgets[' Affiliates']=0
re_allocate_budgets['Digital']=0


# In[31]:


pc=predictions_and_contribution()
predictions_and_contributions=pc.generate_predictions(medias,re_allocate_budgets)


# In[32]:


predictions_and_contributions


# In[ ]:




