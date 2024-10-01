import matplotlib.pyplot as plt
import pandas as pd

var=pd.read_csv("E:\Mini Project RD\Sorted_Data.csv")
print(var)

x = list(var['No'])
y = list(var['Star Rating'])

plt.figure(figsize=(10,10))
plt.style.use('classic')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="yellow")
plt.xticks(range(1, 80))
plt.xticks(rotation=90)

plt.title("Star Rating for books")
plt.show()





