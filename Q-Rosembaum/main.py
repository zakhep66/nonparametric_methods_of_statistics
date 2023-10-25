import pandas as pd
from scipy import stats

# Чтение данных из CSV файла
df = pd.read_csv('data.csv')

# Удаление строк с отсутствующими значениями (NaN)
df = df.dropna()

# Разделение данных на две выборки
sample1 = df['Sample1'].values
sample2 = df['Sample2'].values

# Выполняем t-тест для независимых выборок
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

# Задаем уровень значимости (например, alpha = 0.05)
alpha = 0.05

# Проводим статистическую проверку гипотезы
if p_value < alpha:
    if t_statistic > 0:
        print("Первая группа превосходит вторую.")
    else:
        print("Вторая группа превосходит первую.")
else:
    print("Нет статистически значимого различия между группами.")
