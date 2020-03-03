# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df=pd.read_csv(path)
df.head()

X=df[['ages', 'num_reviews', 'piece_count', 'play_star_rating','review_difficulty', 'star_rating', 'theme_name','val_star_rating','country']]
y=df['list_price']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size = 0.3,random_state = 6)
# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols=X_train.columns
print(cols)
fig,axes=plt.subplots(nrows = 3 , ncols = 3,figsize=(15,7))

for i in range(0,3):
    for j in range(0,3):
        col=cols[ i * 3 + j]
        axes[i,j].scatter(df[col],df['list_price'])

# code ends here



# --------------
# Code starts here

corr=X_train.corr()
X_train.drop(columns=['play_star_rating','val_star_rating'],axis=1,inplace=True)
X_test.drop(columns=['play_star_rating','val_star_rating'],axis=1,inplace=True)

# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

# Code ends here


# --------------
# Code starts here
residual=y_test-y_pred
plt.hist(residual,label='Residuals of y_test')


# Code ends here


