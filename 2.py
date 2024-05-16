import pandas as pd

data = pd.read_csv('bank.csv')
numeric_variables = ['age', 'balance']
print("Описательные статистики для переменных:")
print(data[numeric_variables].describe())
print("\nКорреляции между  переменными:")
print(data[numeric_variables].corr())


