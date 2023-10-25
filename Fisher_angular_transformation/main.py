from scipy.stats import fisher_exact
import pandas as pd

# Исходные списки
read_list1 = pd.read_csv('control.csv')
read_list2 = pd.read_csv('experimental.csv')

list1 = read_list1.values.tolist()
list2 = read_list2.values.tolist()

# Создаем двумерный список 2 на 2
two_by_two = [[*list1[2], *list2[2]], [*list1[3], *list2[3]]]

# Вычисляем угловое преобразование Фишера
odds_ratio, p_value = fisher_exact(two_by_two)

# Определяем, улучшилась ли успеваемость
if odds_ratio > 1:
    print("Успеваемость улучшилась")
else:
    print("Успеваемость не улучшилась")
