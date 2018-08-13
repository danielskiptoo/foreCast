import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn import datasets, linear_model
import numpy as np
# lists1=[]
# lists2=[]
# lists3=[]
# min=800;
# for i in range (500,1300,80):
#     lists1.append(i)
# for x in range(15,25,1):
#     lists2.append(x)
# for y in range(1800,2200,40):
#     lists3.append(y)
# Data={
#     'Temperature':lists2,
#     'Rainfall':lists1,
#     'Production':lists3
#
# }
# df=DataFrame(Data,columns=['Temperature','Rainfall','Production'])
# X=df[['Temperature','Rainfall']].astype(float)
# Y=df['Production'].astype(float)
# regr = linear_model.LinearRegression()
# regr.fit(X, Y)
#
# print(regr.predict([[22,2000]]))

# list1=[1,5,7,1,3,0,6,5,4,45]
# list2=[8,3,14,78,3,0,77,5,4,10]
#
# for i,j in zip(list2,list1):
#     print('the values are'+str(i)+' '+str(j))
# arra=np.linspace(500,1300,num=10,endpoint=False)
# print(arra)
# print(int(2.5))
# from main.models import Crop_requirements
#
# maize_requirements = Crop_requirements.objects.filter(crop_name='Wheat')
# wheat_expected_yield = 0
# temperatures = []
# rainfall = []
# productions = []
# for k in maize_requirements:
#     maxTemp = int(k.temp_max)
#     minTemp = int(k.temp_min)
#     maxRainfall = int(k.max_rainfall)
#     minRainfall = int(k.min_rainfall)
#     minProduction = int(k.max_expected_acre)
#     maxProduction = int(k.max_expected_acre)
# for temp in range(15, 30):
#         temperatures = np.linspace(15, 30, num=10, endpoint=False)
# for rainfll in range(600, 1150):
#         rainfall = np.linspace(600, 1150, num=10, endpoint=False)
# for production in range(3150, 3600):
#         productions = np.linspace(3150, 3600, num=10, endpoint=False)
# Data = {
#                 'Temperature': temperatures,
#                 'Rainfall': rainfall,
#                 'Production': productions
#
#             }
# df = DataFrame(Data, columns=['Temperature', 'Rainfall', 'Production'])
# X = df[['Temperature', 'Rainfall']].astype(float)
# Y = df['Production'].astype(float)
# regr = linear_model.LinearRegression()
# regr.fit(X, Y)
# print(regr.predict([[25.5,930]]))
# print(temperatures)
# print(rainfall)
# print(productions)
# print(np.math.ceil(4.5))

file_path = "main/static/main/data/"
colnames = ['month', 'maxTemp', 'minTemp', 'avgRainfall','avgTemp']
maizePeriod= pd.read_csv(file_path+'maize.csv',names=colnames, skiprows=(1))
wheatPeriod=pd.read_csv(file_path+'wheat.csv',names=colnames, skiprows=(1))
avgRainfall = wheatPeriod['avgRainfall'].tolist()
temperatures = wheatPeriod['avgTemp'].tolist()
rainfall = wheatPeriod['avgRainfall'].tolist()


print(avgRainfall)
print(temperatures)
print(rainfall)




