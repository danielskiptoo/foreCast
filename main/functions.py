import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd

#def getTemprature():
    #path= "main/static/main/temp_values/"
    #colnames = ['MONTH', 'MAX_TEMP', 'MIN_TEMP', 'AVG']
    #data = pd.read_csv(path + 'temp_values.csv', names=colnames, skiprows=(1))
    #return data
from sklearn.preprocessing import PolynomialFeatures

x = np.array([2, 3, 4])
poly = PolynomialFeatures(3, include_bias=False)
poly.fit_transform(x[:, None])

