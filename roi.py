#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
class roi_spend_contribution:
    def roi_and_spend(self,sales_and_media_effects,contribution,date_cols,medias):
        rr=sales_and_media_effects[date_cols].astype(str)
        sales_and_media_effects['level']=rr.apply(lambda x: '_'.join(x.values.tolist()), axis=1)
        rrr=contribution[date_cols].astype(str)
        contribution['level']=rrr.apply(lambda x: '_'.join(x.values.tolist()), axis=1)
        df=pd.DataFrame()
        for med in medias:
            for ym in contribution['level'].unique():
                f=contribution[contribution['level']==ym]
                e=sales_and_media_effects[sales_and_media_effects['level']==ym]
    
                contri,spend=f[med].sum(),e[med].sum()
                res={'media':med,'level':ym,'spend':spend,'sales':contri,'ROI':contri/spend}
                df=df.append(res,ignore_index=True)
        df.fillna(0,inplace=True)
        df['ROI'].replace(np.inf,100,inplace=True)
        df['ROI'].replace(-np.inf,-100,inplace=True)
        df.to_csv('roi_spend_and_contribution.csv')
        return(df)


# In[21]:





# In[22]:





# In[23]:





# In[24]:





# In[25]:





