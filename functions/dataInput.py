# input and setting data tables
from matplotlib import pyplot as plt

import pandas as pd

# Δεδομένα Φορτίου
load2012 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2012.xlsx', names=pd.date_range(start='1/1/2012', periods=366, freq='D'))
load2013 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2013.xlsx', names=pd.date_range(start='1/1/2013', periods=365, freq='D'))
load2014 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2014.xlsx', names=pd.date_range(start='1/1/2014', periods=365, freq='D'))
load2015 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2015entsoe.xlsx', names=pd.date_range(start='1/1/2015', periods=365, freq='D'))
load2016 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2016entsoe.xlsx', names=pd.date_range(start='1/1/2016', periods=366, freq='D'))
load2017 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2017entsoe.xlsx', names=pd.date_range(start='1/1/2017', periods=365, freq='D'))
load2018 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2018entsoe.xlsx', names=pd.date_range(start='1/1/2018', periods=365, freq='D'))
load2019 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/load2019entsoe.xlsx', names=pd.date_range(start='1/1/2019', periods=365, freq='D'))

# Δεδομένα θερμοκρασίας
temp2012 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2012.xlsx', names=pd.date_range(start='1/1/2012', periods=366, freq='D'))
temp2013 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2013.xlsx', names=pd.date_range(start='1/1/2013', periods=365, freq='D'))
temp2014 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2014.xlsx', names=pd.date_range(start='1/1/2014', periods=365, freq='D'))
temp2015 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2015.xlsx', names=pd.date_range(start='1/1/2015', periods=365, freq='D'))
temp2016 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2016.xlsx', names=pd.date_range(start='1/1/2016', periods=366, freq='D'))
temp2017 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2017.xlsx', names=pd.date_range(start='1/1/2017', periods=365, freq='D'))
temp2018 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2018.xlsx', names=pd.date_range(start='1/1/2018', periods=365, freq='D'))
temp2019 = pd.read_excel('/home/konstantinos/PycharmProjects/Thesis_Cases1to4/data/tempData2019.xlsx', names=pd.date_range(start='1/1/2019', periods=365, freq='D'))




