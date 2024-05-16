import pandas as pd
data = pd.read_csv('bank.csv')
print("Основная информация о данных:")
print(data.info())
print("\nКоличество пропущенных значений:")
print(data.isnull().sum())

# data = data.dropna()

print("\nПервые 5 строк данных:")
print(data.head())
