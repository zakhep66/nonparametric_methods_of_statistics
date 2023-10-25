import pandas as pd
from scipy import stats

# Чтение данных из CSV файла
df = pd.read_csv('data.csv')

# Вычисляем разницу между парами значений "после" и "до"
df['Differences'] = df['Sample2'] - df['Sample1']

# Удаляем строки с нулевыми разницами
df = df[df['Differences'] != 0]

# Пересчитываем индексы после удаления строк
df = df.reset_index(drop=True)

# Выполняем G-критерий знаков с альтернативной гипотезой "greater" (больше)
G, p_value = stats.wilcoxon(df['Differences'], alternative='greater')

# Задаем уровень значимости (например, alpha = 0.05)
alpha = 0.05

# Проводим статистическую проверку гипотезы
if p_value < alpha:
    print("Результаты различаются (статистически значимо), после обучения лучше.")
else:
    print("Нет статистически значимого различия между результатами до и после обучения.")
