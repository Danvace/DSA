"""
Варіант 1
Зоомагазин займається продажем хом’ячкiв. Це мирнi домашнi iстоти, проте, як
виявилося, вони мають цiкаву харчову поведiнку.
Для того, щоб прогодувати хом’ячка, який живе наодинцi, потрiбно H пакетiв корму
на день. Однак, якщо кiлька хом’ячкiв живуть разом, у них прокидається жадiбнiсть.
У такому випадку кожен хом’ячок з’їдає додатково G пакетiв корму в день за
кожного сусiда. Денна норма H та жадiбнiсть G є iндивiдуальними для кожного
хом’ячка.
Всього в магазинi є C хом’ячкiв. Ви бажаєте придбати якомога бiльше, проте у вас
є всього S пакетiв їжi на день. Визначте максимальну кiлькiсть хом’ячкiв, яку ви
можете прогодувати.
Реалізуйте функцію, яка поверне число - максимальне число хо
Вхідні параметри функції:
S — ваш денний запас їжi. 0 ≤ S ≤ 109
C — загальна кiлькiсть хом’ячкiв, яка є в продажу, 1 ≤ C ≤ 105
Матриця `hamsters`, яка містить С рядків, перший стовчик якої містить денну норму корму,
другий - рiвень жадiбностi кожного хом’ячка. Деннs нормb є цілими додатніми числами і гарантовано меншими за 109.
Іноді у вас можуть бути не жадібні хом’ячки, але також можуть траплятись і надзвичайно жадібні,
 рівень жадібності може бути як нульовим, так і великим цілим числом
Приклад 1
S = 7
C = 3
hamsters = `[ [1 2], [2 2], [3 1]]``
Результат:
2
Пояснення: Можна взяти першого хом’ячка та будь-якого з iнших двох.
Приклад 2
S = 19
C = 4
hamsters = `[ [5 0], [2 2], [1 4], [5 1]]
Результат:
3
Пояснення: Третiй хом’ячок надто жадiбний. Можна взяти всiх iнших трьох, тодi за день вони з’їдять (5 + 0 · 2) + (2 + 2 · 2) + (5 + 1 · 2) = 18 пакетiв
Приклад 3
S = 2
C = 2
hamsters = `[[1 50000], [1 60000]]
Результат:
1
Пояснення: Обидва хом’ячки надто жадiбнi, щоб їсти разом. Для перевірки виконання роботи реалізованого алгоритму
слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище
"""


def max_hamsters(food_amount, hamsters):
    # hamsters.sort(key=lambda x: x[0] / (x[0] + x[1]), reverse=True)

    # start = 0
    # end = 0
    # max_hamsters_count = 0
    # total_food_needed = 0

    # while end < len(hamsters):
    #
    #     day_norm, greed = hamsters[end]
    #     food_needed = day_norm + greed * (end - start)
    #
    #     if total_food_needed + food_needed <= food_amount:
    #         max_hamsters_count = max(max_hamsters_count, end - start + 1)
    #         total_food_needed += food_needed
    #         end += 1
    #     else:
    #         total_food_needed -= hamsters[start][0]
    #         start += 1
    # return max_hamsters_count

    # hamster_len = len(hamsters)
    # total_food_needed = 0
    # while hamster_len > 0:
    #     for i in range(hamster_len):
    #         total_food_needed += hamsters[i][0] + hamsters[i][1]*(hamster_len - 1)
    #     if total_food_needed <= food_amount:
    #         if hamster_len == len(hamsters):
    #             return hamster_len
    #         hamster_len += hamster_len//2
    #
    #     else:
    #         hamster_len /= 2
    # return 0
    hamsters.sort(key=lambda x: x[0] + x[1] * len(hamsters))
    hamsters_len = len(hamsters)
    total_food_needed = 0
    found = False
    left = 0
    right = len(hamsters) - 1

    while not found:
        for i in range(hamsters_len):
            total_food_needed += hamsters[i][0] + hamsters[i][1] * (hamsters_len - 1)

        if right - left == len(hamsters) and total_food_needed <= food_amount:
            found = True
        if total_food_needed >= food_amount:
            right

        # if total_food_needed >= food_amount and not hamsters_len == len(hamsters):
        #     hamsters_len = hamsters_len - hamsters_len // 2
        #     hamsters.sort(key=lambda x: x[0] + x[1] * hamsters_len)
        #     total_food_needed = 0
        #     if hamsters_len == 1:
        #         found = True
        #
        # if total_food_needed <= food_amount and not hamsters_len == len(hamsters):
        #     hamsters_len = hamsters_len - hamsters_len // 2
        #     hamsters.sort(key=lambda x: x[0] + x[1] * hamsters_len)
        #     total_food_needed = 0
        #     if hamsters_len == 1:
        #         found = True

    return hamsters_len
