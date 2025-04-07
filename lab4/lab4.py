import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model



df = pd.read_excel("датасет-1.xlsx")
area, price = df.items()
area, price = list(area[1]), list(price[1])
print(area, price)
plt.scatter(df.area,df.price,color='red')
plt.xlabel('площадь(кв.м.)')
plt.ylabel('стоимость(млн.руб)')
reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
print(reg.predict(df[['area']]))
plt.scatter(df.area,df.price,color='red')
plt.xlabel('площадь(кв.м.)')
plt.ylabel('стоимость(млн.руб)')
plt.plot(df.area, reg.predict(df[['area']]))
plt.show()
df = pd.read_excel("prediction_price.xlsx")
pred = df[['area']]
p = reg.predict(pred)
print(p)
pred['predicted prices'] = p
pred.to_excel('new.xlsx', index=False)
