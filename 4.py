import pandas as pd

data = pd.read_csv('bank.csv')
numeric_variables = ['age', 'balance']

outliers = {}
for var in numeric_variables:
    q1 = data[var].quantile(0.25)
    q3 = data[var].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    var_outliers = data[(data[var] < lower_bound) | (data[var] > upper_bound)]
    outliers[var] = var_outliers


for var, var_outliers in outliers.items():
    if len(var_outliers) > 0:
        print(f"Выбросы для переменной {var}:")
        print(var_outliers.to_string(index = False))
        print()
    else:
        print(f"Для переменной {var} нет выбросов.")
