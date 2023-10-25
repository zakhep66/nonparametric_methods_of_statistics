import pandas as pd
from scipy.stats import wilcoxon

# Прочитать данные из CSV файла
data = pd.read_csv('data.csv')

# Извлечь данные из двух столбцов
group1 = data['group1']
group2 = data['group2']

# Выполнить Т-критерий Вилкоксона
statistic, p_value = wilcoxon(group1, group2, alternative='two-sided', mode='approx')

# Уровень значимости (обычно 0.05)
alpha = 0.05

# Определить результат
if p_value < alpha:
    print("Подготовленность студентов улучшилась")
else:
    print("Подготовленность студентов не улучшилась")
