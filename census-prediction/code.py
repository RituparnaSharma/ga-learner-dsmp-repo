# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",",skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]


#Code starts here
new_record=np.asarray(new_record)
census=np.concatenate((data,new_record),axis=0)


# --------------
#Code starts here

age=census[:,:1]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)


# --------------
#Code starts here
race=census[:,2]
race=np.asarray(race)

race_0=census[np.all([race==0],axis=0)]
race_1=census[np.all([race==1],axis=0)]
race_2=census[np.all([race==2],axis=0)]
race_3=census[np.all([race==3],axis=0)]
race_4=census[np.all([race==4],axis=0)]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

lis=([len_0,len_1,len_2,len_3,len_4])
minority_race=np.min(lis)
minority_race=list(lis).index(minority_race)
print(minority_race)


# --------------
#Code starts here
ages=census[:,0]
ages=np.asarray(ages)
print(ages)
senior_citizens =census[(ages>60)]
print(senior_citizens)
working_hours_sum=senior_citizens[:,6:7]
working_hours_sum=np.sum(working_hours_sum)
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
edu_num=census[:,1]
high=census[np.all([edu_num>10],axis=0)]
print(high)
low=census[np.all([edu_num<=10],axis=0)]
income_high=high[:,7]
avg_pay_high=np.mean(income_high)
income_low=low[:,7]
avg_pay_low=np.mean(income_low)
print(avg_pay_high)
print(avg_pay_low)


