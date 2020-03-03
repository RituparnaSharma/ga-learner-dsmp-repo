# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data=pd.read_csv(path)
plt.subplot(1,2,1)
data.Rating.plot(kind='hist')

data=data[data.Rating<=5]
plt.subplot(1,2,2)
data.Rating.plot(kind='hist')
#Code ends here



# --------------
# code starts here
total_null=data.isnull().sum()
percent_null=round((total_null/data.isnull().count()),2).apply(lambda x:str(x)+'%')
missing_data=pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])

data.dropna(axis=0,inplace=True)
total_null_1=data.isnull().sum()
percent_null_1=round((total_null/data.isnull().count()),2).apply(lambda x:str(x)+'%')
missing_data_1=pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
# code ends here


# --------------

#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
data.Installs.value_counts()
rem_obj=['+',',']
for i in rem_obj:
    data.Installs=data.Installs.apply(lambda x:(x.replace(str(i),'')))
data.Installs=data.Installs.astype(int)
le=LabelEncoder()
data.Installs=le.fit_transform(data.Installs)
sns.regplot(x="Installs", y="Rating", data=data)
plt.title('Rating vs Installs [RegPlot]')
#Code ends here



# --------------
#Code starts here
data.Price.value_counts()
data.Price=data.Price.apply(lambda x:(x.replace('$','')))
data.Price=data.Price.astype(float)
sns.regplot(x="Price", y="Rating",data=data)
plt.title('Rating vs Price [RegPlot]')
#Code ends here


# --------------

#Code starts here
data.Genres.unique()
data.Genres=data.Genres.str.split(";").apply(lambda x:x[0])
gr_mean=data.groupby('Genres',as_index=False)['Rating'].mean()
gr_mean.describe()
gr_mean=gr_mean.sort_values(by='Rating',ascending=True)
print(gr_mean.loc[0],gr_mean.loc[len(gr_mean)-1])
#Code ends here


# --------------
from datetime import datetime
#Code starts here

data['Last Updated']=data['Last Updated'].apply(lambda x:datetime.strptime(x,'%B %d, %Y'))
max_date=data['Last Updated'].max()
data['Last Updated Days']=(max_date-data['Last Updated']).dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
#Code ends here


