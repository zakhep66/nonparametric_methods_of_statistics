import pandas as pd
from scipy import stats

# Чтение данных из CSV файла
df = pd.read_csv('data.csv')

# Разделение данных на две группы
group1 = df['Group1'].tolist()
group2 = df['Group2'].tolist()

# Выполняем U-критерий Манна-Уитни
U, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')

# Задаем уровень значимости (например, alpha = 0.05)
alpha = 0.05

# Проводим статистическую проверку гипотезы
if p_value < alpha:
    if U < len(group1) * len(group2) / 2:
        print("Результаты студентов первой группы выше результатов студентов второй группы.")
    else:
        print("Результаты студентов второй группы выше результатов студентов первой группы.")
else:
    print("Нет статистически значимого различия между результатами двух групп.")
