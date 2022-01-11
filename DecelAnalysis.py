import pandas as pd
from pandas.core.indexing import _iLocIndexer

# Clean empty rows
filename = input("File Direcotry: ")
df = pd.read_csv(str(filename),low_memory= False)
df.columns = df.iloc[4]
df = df.iloc[5: , : ]
df=df.drop(df.columns[[5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22]],axis = 1)

df = df.astype(float)



df = df.assign(microStrain_BR = lambda x: (x.v0/6.58e-4))
df = df.assign(microStrain_BL = lambda x: (x.v1/6.58e-4))
df = df.assign(microStrain_FR = lambda x: (x.v2/6.58e-4))
df = df.assign(microStrain_FL = lambda x: (x.v3/6.58e-4))
df = df.assign(AccelerometerCenter_g = lambda x: (x.v8/4.51e-3))
df = df.assign(Laser_mm = lambda x: (x.v10*100))



print(df)

