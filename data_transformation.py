#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
class data_transformation:
    def __init__(self):
        self.lag_range=10
        self.betas=[0.6,0.7,0.8,0.9,1]
        self.decays=[0.6,0.7,0.8,0.9,1]
        self.top_n_features=3
    def add_lag_carryover_decay(self,sales_and_media_effects,medias,sales_cols,dep_var):
        """
        inputs:
        
        medias(independent varibles)=list of all media varibles like current_media,Radio etc
        sales_columns=apart from media varibles 
        dep_bar(dependent varible): in our case it is revenue
        sales_cols=['Year','Month','revenue']
        
        description:
                This function will add carry over,lag and shape effect to each media varibles with values mentioned in class constructor.
                and it will select top 3 values  which are highest co-relation values with dependent varible
    
        """
        all_media=[]
        for media in medias:
            #applying lag
            current_media=pd.DataFrame(sales_and_media_effects[media],columns=[media])
            for lag in range(self.lag_range):
                name=media+'_'+'lag'+str(lag)
                current_media[name]=current_media[media].shift(periods=lag,fill_value=0)
            del current_media[media]
            lag_cols=current_media.columns
            #apply shape effect
            for cols in current_media.columns:
                for beta in self.betas:
                    col_name=cols+'beta_'+str(beta)
                    current_media[col_name]=current_media[cols]**beta
            current_media.drop(lag_cols,axis=1,inplace=True)
            beta_cols=current_media.columns
            #applying beta effect
            for cols in current_media.columns:
                for decay in self.decays:
                    col_name=cols+'decay_'+str(decay)
                    current=current_media[cols]*decay
                    prev=current_media[cols].shift(1,fill_value=0)*(1-decay)
                    current_media[col_name]=current+prev
            current_media.drop(beta_cols,axis=1,inplace=True)
            current_media[sales_cols]=sales_and_media_effects[sales_cols]
            corrs=current_media.corr()[dep_var]
            #select top 3 features based on co-relation with sales(dependent variable)
            sorted_corss=corrs.sort_values(ascending=False)
            all_media.append(current_media[sorted_corss.iloc[1:self.top_n_features+1].index])
        all_media_transformed=pd.concat(all_media,axis=1)
        all_media_transformed[sales_cols]=sales_and_media_effects[sales_cols]
        all_media_transformed.to_csv('all_media_transformed.csv',index=False)
        return(all_media_transformed)
        
   
    
    


# In[ ]:




