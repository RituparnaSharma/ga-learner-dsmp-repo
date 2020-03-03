# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
p_a=(df['fico']>700).sum()/len(df['fico'])
p_b=(df['purpose']=='debt_consolidation').sum()/len(df['purpose'])
df1=df[df['purpose']=='debt_consolidation']
p_a_b=((df1['fico']>700)&(df1['purpose'])).sum()/(df['fico']>700).sum()
result=((df1['fico']>700)&(df1['purpose'])).sum()/(df1['purpose']).count()==p_a
# code ends here


# --------------
# code starts here
prob_lp=(df['paid.back.loan'] == 'Yes').sum()/len(df)
prob_cs=(df['credit.policy'] == 'Yes').sum()/len(df)
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs=((new_df['paid.back.loan']== 'Yes')&(new_df['credit.policy']=='Yes')).sum()/(df['paid.back.loan'] == 'Yes').sum()

bayes=(prob_pd_cs*prob_lp)/prob_cs

# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind='bar')
df1=df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind='bar')
# code ends here


# --------------
# code starts here
inst_median=df['installment'].median
inst_mean=df['installment'].mean
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(15,7))
df['installment'].plot(kind='hist',bins=25,ax=ax1)
ax1.set_title('histogram for installment')
df['log.annual.inc'].plot(kind='hist',bins=25,ax=ax2)
ax2.set_title('histogram for log anual income ')



# code ends here


