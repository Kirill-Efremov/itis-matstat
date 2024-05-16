import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('bank.csv')

plt.figure(figsize=(10, 5))
sns.histplot(data['age'], kde=True, color='blue')
plt.title('Гистограмма и график функции распределения возраста')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(data['balance'], color='red', kde=True)
plt.title('Гистограмма и график функции распределения баланса')
plt.xlabel('Баланс')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

plt.figure(figsize=(5, 10))
sns.boxplot(y=data['age'], color='blue')
plt.title('Боксплот возраста')
plt.ylabel('Возраст')
plt.grid(True)
plt.show()

plt.figure(figsize=(5, 10))
sns.boxplot(y=data['balance'], color='green')
plt.title('Боксплот баланса')
plt.ylabel('Баланс')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(x='age', y='balance', data=data, color='red')
plt.title('Диаграмма рассеивания возраста и баланса')
plt.xlabel('Возраст')
plt.ylabel('Баланс')
plt.grid(True)
plt.show()




