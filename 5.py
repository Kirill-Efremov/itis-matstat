import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import mannwhitneyu
import seaborn as sns
from scipy.stats import shapiro
data = pd.read_csv('bank.csv')
stat_age, p_age = shapiro(data['age'])
print("Тест Шапиро-Уилка для возраста:")
print("p-значение:", p_age)
if p_age > 0.05:
    print("Не удалось отвергнуть нулевую гипотезу. Распределение возраста может быть нормальным.")
else:
    print("Отвергаем нулевую гипотезу. Распределение возраста не является нормальным.")

stat_balance, p_balance = shapiro(data['balance'])
print("\nТест Шапиро-Уилка для баланса:")
print("p-значение:", p_balance)
if p_balance > 0.05:
    print("Не удалось отвергнуть нулевую гипотезу. Распределение баланса может быть нормальным.")
else:
    print("Отвергаем нулевую гипотезу. Распределение баланса не является нормальным.")

#H0 (нулевая гипотеза): Средние значения баланса у клиентов с ипотекой и без ипотеки одинаковы.
balance_with_housing = data[data['housing'] == 'yes']['balance']
balance_without_housing = data[data['housing'] == 'no']['balance']

plt.figure(figsize=(10, 5))
sns.histplot(balance_with_housing, kde=True, color='blue')
plt.title('Распределение баланса с ипотекой')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(balance_without_housing, kde=True, color='green')
plt.title('Распределение баланса без ипотеки')
plt.tight_layout()
plt.show()

statistic, p_value = mannwhitneyu(balance_with_housing, balance_without_housing)
alpha = 0.05
if p_value < alpha:
    print("Отвергаем нулевую гипотезу, существует статистически значимая разница в балансе между клиентами с ипотекой и без ипотеки")
else:
    print("Нет оснований отвергать нулевую гипотезу, средние значения баланса для обеих групп клиентов одинаковы")

