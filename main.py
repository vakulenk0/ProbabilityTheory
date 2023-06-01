import random
import math
import eel
import docx
from docx import Document
from docxtpl import DocxTemplate
from docx_form import DocxForm
import collections
from jinja2 import Template

# mass = []
# @eel.expose
# def makeVariants(a):
#     global mass
#     mass = a

# @eel.expose
# def check():
#     print(mass)

@eel.expose
def p(a):
    print(a)

@eel.expose
def build(a):
    for i in range(0, int(a[0])):
        # -----------------------------------1
        task1_mass = [
            random.randrange(16, 23),
            random.randrange(7, 9),
            random.randrange(3, 6)
        ]

        ans1 = round(math.comb(task1_mass[0] - task1_mass[1], task1_mass[2]) / math.comb(task1_mass[0], task1_mass[2]), 3)
        task1_a = [
            round(ans1 + 0.05, 3),
            round(ans1 - 0.01, 3),
            round(ans1 + 0.02, 3)
        ]

        task1_answers = [ans1, task1_a[0], task1_a[1],task1_a[2]]
        random.shuffle(task1_answers)

        # -----------------------------------2
        task2_mass = [
            random.randrange(0, 2) + 2
        ]

        if (task2_mass[0] == 2):
            ans2 = 0.2
        elif (task2_mass[0] == 3):
            ans2 = 0.06

        task2_a = [
            ans2 + 0.05,
            ans2 + 0.12,
            ans2 - 0.03,
        ]

        task2_answers = [ans2, task2_a[0], task2_a[1], task2_a[2]]
        random.shuffle(task2_answers)

        # -----------------------------------3
        task3_mass = [
            random.randrange(10, 20)/100,
            random.randrange(5, 15)/100,
            random.randrange(15, 30)/100
        ]

        ans3 = round(task3_mass[0]*task3_mass[1]*task3_mass[2], 3)
        task3_a = [
            round(ans3 + 0.05, 3),
            round(ans3 + 0.07, 3),
            round(ans3 + 0.03, 3)
        ]
        task3_answers = [ans3, task3_a[0], task3_a[1], task3_a[2]]
        random.shuffle(task3_answers)

        # -----------------------------------4
        task4_mass = [
            random.randrange(2, 5),
            random.randrange(6, 9),
            random.randrange(3, 6),
            random.randrange(7, 11)
        ]

        PAB = task4_mass[3]/(task4_mass[2] + task4_mass[3])
        PA = (task4_mass[0] + task4_mass[3])/sum(task4_mass)
        PB = (task4_mass[2] + task4_mass[3])/sum(task4_mass)
        ans4 = round(PAB*PB/PA, 3)

        task4_a = [
            round(ans4 + 0.04, 3),
            round(ans4 - 0.02, 3),
            round(ans4 + 0.05, 3)
        ]
        task4_answers = [ans4, task4_a[0], task4_a[1], task4_a[2]]
        random.shuffle(task4_answers)

        # -----------------------------------5
        task5_mass = [
            random.randrange(2, 5),
            random.randrange(6, 9),
            random.randrange(5, 9),
            random.randrange(2, 6)
        ]

        ans5 = round((4*task5_mass[0])/(4*task5_mass[0]+6*task5_mass[2]), 3)

        task5_a = [
            round(ans5 + 0.1, 3),
            round(ans5 - 0.02, 3),
            round(ans5 + 0.03, 3)
        ]
        task5_answers = [ans5, task5_a[0], task5_a[1], task5_a[2]]
        random.shuffle(task5_answers)

        # -----------------------------------6
        task6_mass = [
            random.randrange(1, 10),
            random.randrange(0, 3),
            random.randrange(4, 6),
            random.randrange(7, 10),
            random.randrange(11, 16),
            random.randrange(1, 15)/100,
            random.randrange(16, 25)/100,
            random.randrange(12, 25)/100,
            random.randrange(20, 28)/100
        ]

        n69 = round((1 - task6_mass[5] - task6_mass[6] - task6_mass[7] - task6_mass[8]), 2)
        ans6 = round((task6_mass[7] + task6_mass[8]), 2)

        task6_a = [
            round(ans6 + 0.09, 2),
            round(ans6 - 0.05, 2),
            round(ans6 + 0.03, 2)
        ]

        task6_answers = [ans6, task6_a[0], task6_a[1], task6_a[2]]
        random.shuffle(task6_answers)

        # -----------------------------------7
        task7_mass = [
            random.randrange(10, 25)/100,
            random.randrange(26, 50)/100,
            1 - random.randrange(1, 50)/100,
            1
        ]
        ans7 = round(task7_mass[2], 2)

        task7_answers = [ans7, task7_mass[3], random.randrange(30, 40)/100, random.randrange(41, 49)/100]
        random.shuffle(task7_answers)

        # -----------------------------------8
        task8_mass = [
            random.randrange(1, 5),
            random.randrange(1, 5),
            random.randrange(1, 3),
            random.randrange(6, 10)
        ]
        ans8 = round((1 - pow(task8_mass[2], 3)/54), 2)

        task8_answers = [ans8, round((ans8 - 0.03), 2), round((ans8 - 0.05), 2), round((ans8 - 0.07), 2)]
        random.shuffle(task8_answers)

        # -----------------------------------9
        task9_mass = [
            random.randrange(6, 8),
            random.randrange(6, 8),
            random.randrange(7, 8)
        ]

        ans9 = '1)'

        # -----------------------------------10
        task10_a = [
            random.randrange(5, 6),
            random.randrange(25, 26),
            random.randrange(125, 126),
        ]
        random.shuffle(task10_a)

        ans10 = '3)'

        # -----------------------------------11
        task11_mass = [
            random.randrange(15, 16)/10,
            random.randrange(5, 6) / 10,
            -random.randrange(5, 6) / 10,
            -random.randrange(15, 16) / 10,
        ]
        task11_answers = [task11_mass[0], task11_mass[1], task11_mass[2], task11_mass[3]]
        random.shuffle(task11_answers)

        ans11 = '0.5'
        # -----------------------------------12

        task12_mass = [
            random.randrange(5, 7),
            random.randrange(5, 7),
            random.randrange(5, 7),
            random.randrange(5, 7),
        ]
        task12_answers = [task12_mass[0], task12_mass[1], task12_mass[2], task12_mass[3]]
        random.shuffle(task12_answers)

        ans12 = '4)'

        # ----------------------------------13

        teoria = [
            "13. Элементарное событие – это {{ent}}    А. Единичный исход; {{ent}}    Б. Число; {{ent}}    В. Эксперимент; {{ent}}    Г. Вывод.",
            "13. Событие – это {{ent}}    А. Пространство элементарных событий; {{ent}}    Б. Утверждение; {{ent}}    В. Подмножество множества элементарных событий; {{ent}}    Г. Доказательство.",
            "13. Вероятность – это {{ent}}    А. Утверждение; {{ent}}    Б. Степень возможности наступления некоторого события; {{ent}}    В. Множество; {{ent}}    Г. Эксперимент.",
            "13. Вероятность наступления некоторого события не может быть равна {{ent}}    А. 2; {{ent}}    Б. 1; {{ent}}    В. 0; {{ent}}    Г. 0.5.",
            "13. P(A+B)= (сложение вероятностей) {{ent}}    А. P(A)+P(B); {{ent}}    Б. P(A)-P(B); {{ent}}    В. P(AB)+P(A); {{ent}}    Г. P(AB)+P(B).",
            "13. Случайное событие – это  {{ent}}    А. Положительное число; {{ent}}    Б. Доказанное утверждение; {{ent}}    В. Очевидное свойство; {{ent}}    Г. Может как произойти так и не произойти",
            "13. Случайная величина есть {{ent}}    А. Функция элементарных событий {{ent}}    Б. Число; {{ent}}    В. Вывод ; {{ent}}    Г. Эксперимент.",
            "13. Функция распределения случайной величины есть {{ent}}    А. Функция элементарных событий; {{ent}}    Б. Функция одного действительного переменного; {{ent}}    В. Функция многих действительных переменных; {{ent}}    Г. Функция двух действительных переменных.",
            "13. Вероятность того, что непрерывная случайная величина примет конкретное значение равна {{ent}}    А. Зависит от задачи; {{ent}}    Б. 1; {{ent}}    В. 0; {{ent}}    Г. Нет правильных ответов.",
            "13. Что означает операция А+В?  {{ent}}    А. Событие В влечет за собой событие А;  {{ent}}    Б. событие А влечет за собой событие В; {{ent}}    В. совместно осуществились события А и В; {{ent}}    Г. Произошло хотя бы одно из двух событий А или В",
            "13. Что означает операция АВ? {{ent}}    А. Ни одно из событий не произошло; {{ent}}    Б. Произошло хотя бы одно из двух событий А или В; {{ent}}    В. Событие А влечет за собой событие В; {{ent}}    Г. Произошло и событие А, и событие В.",
            "13. Выберите неверное утверждение {{ent}}    А. Вероятность появления одного из противоположных событий всегда больше   вероятности другого; {{ent}}    Б. Сумма вероятностей двух противоположных событий равна единице; {{ent}}    В. Если два события единственно возможны и несовместны, то они называются противоположными; {{ent}}    Г. Событие, которое никогда не произойдет, является невозможным.",
            "13. Максимальное значение произведения вероятностей противоположных событий равно {{ent}}    А. 0.25; {{ent}}    Б. 0.5; {{ent}}    В. 1; {{ent}}    Г. 0.54.",
            "13. Парный коэффициент корреляции равен –1. Это означает {{ent}}    А. Наличие нелинейной функциональной связи; {{ent}}    Б. Отрицательную линейную связь; {{ent}}    В. Отсутствие связи; {{ent}}    Г. Положительную линейную связь.",
            "13. Вероятности появления заданного числа благоприятных исходов в схеме Бернулли описываются {{ent}}    А. Однородным распределением; {{ent}}    Б. Геометрическим распределением; {{ent}}    В. Равномерным распределением на отрезке; {{ent}}    Г. Биноминальным распределением.",
            "13. Математического ожидания не существует у случайной величины {{ent}}    А. Равномерно распределенной на отрезке; {{ent}}    Б. Распределенной по Коши; {{ent}}    В. Имеющей нормальное распределение; {{ent}}    Г. Неравномерно распределенной на отрезке.",
            "13. Закон больших чисел выводится из неравенства Чебышева при условии существования у случайной величины {{ent}}    А. Плотности; {{ent}}    Б. Конечного математического ожидания; {{ent}}    В. Конечного второго момента; {{ent}}    Г. Дисперсии.",
            "13. Характеристическая функция случайной величины есть {{ent}}    А. Комплекснозначная функция действительного переменного; {{ent}}    Б. Аналитическая функция комплексного переменного; {{ent}}    В. Действительная функция комплексного переменного; {{ent}}    Г. Мнимая функция комплексного переменного.",
            "13. Если характеристическая функция случайной величины имеет производную в точке нуль, то {{ent}}    А. Случайная величина имеет конечное математическое ожидание; {{ent}}    Б. Случайная величина имеет плотность; {{ent}}    В. Случайная величина имеет конечный момент второго порядка; {{ent}}    Г. Все варианты неверные.",
            "13. Зная характеристическую функцию можно определить функцию распределения {{ent}}    А. Простой случайной величины; {{ent}}    Б. Непрерывной случайной величины; {{ent}}    В. Произвольной случайной величины; {{ent}}    Г. Невозможно определить функцию распределения.",
            "13. Двумерная случайная величина называется непрерывной, если ее функция распределения- {{ent}}    А. непрерывная, дифференцируемая по каждому из аргументов, и существует вторая смешанная производная; {{ent}}    Б. непрерывная, дифференцируемая по каждому из аргументов, и существует третья смешанная производная; {{ent}}    В. непрерывная; {{ent}}    Г. Ни один вариант не является верным.",
            "13. Плотность распределения вероятностей непрерывной двумерной случайной величины –это {{ent}}    А. Сумма всех вероятностей; {{ent}}    Б. Вторая смешанная частная производная ее функции распределения; {{ent}}    В. Постоянная величина; {{ent}}    Г. Все варианты верные.",
            "13. Математическое ожидание постоянной равно {{ent}}    А. Нет верного варианта; {{ent}}    Б. 1; {{ent}}    В. 2; {{ent}}    Г. Этой постоянной."
            "13. Для каких случайных величин справедливо свойство математического ожидания M (X + Y) = MX + MY {{ent}}    А. И для зависимых, и для независимых; {{ent}}    Б. Только для зависимых; {{ent}}    В. Только для независимых; {{ent}}    Г. Нет верного варианта.",
            "13. Какой вероятности соответствует медиана? {{ent}}    А. 0,25; {{ent}}    Б. 1; {{ent}}    В. 0,5; {{ent}}    Г. Нет верного ответа.",
            "13. Вставьте пропуск. {{ent}}Если Х – непрерывная случайная величина, то мода – __________________ плотности распределения {{ent}}    А. Точка локального максимума; {{ent}}    Б. Точка локального минимума; {{ent}}    В. Несуществующая точка; {{ent}}    Г. Нет верного ответа.",
            "13. Числом, равным математическому ожиданию квадрата отклонения случайной величины от её математического ожидания называют {{ent}}    А. Квантиль; {{ent}}    Б. Моду; {{ent}}    В. Медиану; {{ent}}    Г. Дисперсию.",
            "13. D(X+Y)= {{ent}}    А. DX+DY; {{ent}}    Б. D(XY); {{ent}}    В. DX+DY-D(XY); {{ent}}    Г. 0."
        ]

        ansTeor = [
            'А. Единичный исход',
            'В. Подмножество множества элементарных событий',
            'Б. Степень возможности наступления некоторого события',
            'А. 2',
            'А. P(A)+P(B)',
            'Г. Может как произойти так и не произойти',
            'А. Функция элементарных событий',
            'Б. Функция одного действительного переменного',
            'В. 0',
            'Г. Произошло хотя бы одно из двух событий А или В',
            'Г. Произошло и событие А, и событие В',
            'А. Вероятность появления одного из противоположных событий всегда больше вероятности другого',
            'А. 0.25',
            'Б. Отрицательную линейную связь',
            'Г. Биноминальным распределением',
            'Б. Распределенной по Коши',
            'В. Конечного второго момента',
            'А. Комплекснозначная функция действительного переменного',
            'А. Случайная величина имеет конечное математическое ожидание',
            'В. Произвольной случайной величины',
            'А. непрерывная, дифференцируемая по каждому из аргументов, и существует вторая смешанная производная',
            'Б. Вторая смешанная частная производная ее функции распределения',
            'Г. Этой постоянной',
            'А. И для зависимых, и для независимых',
            'В. 0,5',
            'А. Точка локального максимума',
            'Г. Дисперсию',
            'А. DX+DY'
        ]


        tasks = {
            'n11': str(task1_mass[0]),
            'n12': str(task1_mass[1]),
            'n13': str(task1_mass[2]),
            'ans11': str(task1_answers[0]),
            'ans12': str(task1_answers[1]),
            'ans13': str(task1_answers[2]),
            'ans14': str(task1_answers[3]),
            'n21': str(task2_mass[0]),
            'ans21': str(task2_answers[0]),
            'ans22': str(task2_answers[1]),
            'ans23': str(task2_answers[2]),
            'ans24': str(task2_answers[3]),
            'n31': str(task3_mass[0]),
            'n32': str(task3_mass[1]),
            'n33': str(task3_mass[2]),
            'ans31': str(task3_answers[0]),
            'ans32': str(task3_answers[1]),
            'ans33': str(task3_answers[2]),
            'ans34': str(task3_answers[3]),
            'n41': str(task4_mass[0]),
            'n42': str(task4_mass[1]),
            'n43': str(task4_mass[2]),
            'n44': str(task4_mass[3]),
            'ans41': str(task4_answers[0]),
            'ans42': str(task4_answers[1]),
            'ans43': str(task4_answers[2]),
            'ans44': str(task4_answers[3]),
            'n51': str(task5_mass[0]),
            'n52': str(task5_mass[1]),
            'n53': str(task5_mass[2]),
            'n54': str(task5_mass[3]),
            'ans51': str(task5_answers[0]),
            'ans52': str(task5_answers[1]),
            'ans53': str(task5_answers[2]),
            'ans54': str(task5_answers[3]),
            'n60': str(task6_mass[0]),
            'n61': str(task6_mass[1]),
            'n62': str(task6_mass[2]),
            'n63': str(task6_mass[3]),
            'n64': str(task6_mass[4]),
            'n65': str(task6_mass[5]),
            'n66': str(task6_mass[6]),
            'n67': str(task6_mass[7]),
            'n68': str(task6_mass[8]),
            'n69': str(n69),
            'ans61': str(task6_answers[0]),
            'ans62': str(task6_answers[1]),
            'ans63': str(task6_answers[2]),
            'ans64': str(task6_answers[3]),
            'n71': str(task7_mass[0]),
            'n72': str(task7_mass[1]),
            'ans71': str(task7_answers[0]),
            'ans72': str(task7_answers[1]),
            'ans73': str(task7_answers[2]),
            'ans74': str(task7_answers[3]),
            'n81': str(task8_mass[0]),
            'n82': str(task8_mass[1]),
            'n83': str(task8_mass[2]),
            'n84': str(task8_mass[3]),
            'ans81': str(task8_answers[0]),
            'ans82': str(task8_answers[1]),
            'ans83': str(task8_answers[2]),
            'ans84': str(task8_answers[3]),
            'n91': str(task9_mass[0]),
            'n92': str(task9_mass[1]),
            'n93': str(task9_mass[2]),
            'n101': task10_a[0],
            'n102': task10_a[1],
            'n103': task10_a[2],
            'ans111': task11_answers[0],
            'ans112': task11_answers[1],
            'ans113': task11_answers[2],
            'ans114': task11_answers[3],
            'ans121': str(task12_answers[0]),
            'ans122': str(task12_answers[1]),
            'ans123': str(task12_answers[2]),
            'ans124': str(task12_answers[3]),
            'ent': '\n'
        }


        document = DocxForm('pattern.docx')
        document.print_all_content_controls_and_form_fields()
        document.content_control_forms_and_form_fields[0].set_text('Вариант ' + str(i + 1))

        if a[1] == False:
            document.content_control_forms_and_form_fields[1].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[1].set_text(' ')
            print(document.content_control_forms_and_form_fields[1].text)
        if a[2] == False:
            document.content_control_forms_and_form_fields[2].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[2].set_text(' ')
            print(document.content_control_forms_and_form_fields[2].text)
        if a[3] == False:
            document.content_control_forms_and_form_fields[3].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[3].set_text(' ')
            print(document.content_control_forms_and_form_fields[3].text)
        if a[4] == False:
            document.content_control_forms_and_form_fields[4].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[4].set_text(' ')
            print(document.content_control_forms_and_form_fields[4].text)
        if a[5] == False:
            document.content_control_forms_and_form_fields[5].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[5].set_text(' ')
            print(document.content_control_forms_and_form_fields[5].text)
        if a[6] == False:
            document.content_control_forms_and_form_fields[6].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[6].set_text(' ')
            print(document.content_control_forms_and_form_fields[6].text)
        if a[7] == False:
            document.content_control_forms_and_form_fields[7].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[7].set_text(' ')
            print(document.content_control_forms_and_form_fields[7].text)
        if a[8] == False:
            document.content_control_forms_and_form_fields[8].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[8].set_text(' ')
            print(document.content_control_forms_and_form_fields[8].text)
        if a[9] == False:
            document.content_control_forms_and_form_fields[9].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[9].set_text(' ')
            print(document.content_control_forms_and_form_fields[9].text)
        if a[10] == False:
            document.content_control_forms_and_form_fields[10].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[10].set_text(' ')
            print(document.content_control_forms_and_form_fields[10].text)
        if a[11] == False:
            document.content_control_forms_and_form_fields[11].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[11].set_text(' ')
            print(document.content_control_forms_and_form_fields[11].text)
        if a[12] == False:
            document.content_control_forms_and_form_fields[12].set_text(' ')
            # dockeys.content_control_forms_and_form_fields[12].set_text(' ')
            print(document.content_control_forms_and_form_fields[12].text)

        trand = random.randrange(0, len(teoria))
        if a[13] == True:
            document.content_control_forms_and_form_fields[13].set_text(teoria[trand])

        if a[13] == True:
            ans13 = ansTeor[trand]
        else:
            ans13 = ' '

        taskKeys = {
            'ans1': str(ans1),
            'ans2': str(ans2),
            'ans3': str(ans3),
            'ans4': str(ans4),
            'ans5': str(ans5),
            'ans6': str(ans6),
            'ans7': str(ans7),
            'ans8': str(ans8),
            'ans9': ans9,
            'ans10': ans10,
            'ans11': ans11,
            'ans12': ans12,
            'ans13': ans13
        }

        name = 'patterns/patternNEW' + str(i + 1) + '.docx'
        document.save(name)
        doc = DocxTemplate(name)
        doc.render(tasks)
        name1 = 'variants/var' + str(i + 1) + '.docx'
        doc.save(name1)

        dockeys = DocxForm('patternKeys.docx')
        dockeys.print_all_content_controls_and_form_fields()
        dockeys.content_control_forms_and_form_fields[0].set_text('Вариант ' + str(i + 1))
        if a[1] == False:
            dockeys.content_control_forms_and_form_fields[1].set_text(' ')
        if a[2] == False:
            dockeys.content_control_forms_and_form_fields[2].set_text(' ')
        if a[3] == False:
            dockeys.content_control_forms_and_form_fields[3].set_text(' ')
        if a[4] == False:
            dockeys.content_control_forms_and_form_fields[4].set_text(' ')
        if a[5] == False:
            dockeys.content_control_forms_and_form_fields[5].set_text(' ')
        if a[6] == False:
            dockeys.content_control_forms_and_form_fields[6].set_text(' ')
        if a[7] == False:
            dockeys.content_control_forms_and_form_fields[7].set_text(' ')
        if a[8] == False:
            dockeys.content_control_forms_and_form_fields[8].set_text(' ')
        if a[9] == False:
            dockeys.content_control_forms_and_form_fields[9].set_text(' ')
        if a[10] == False:
            dockeys.content_control_forms_and_form_fields[10].set_text(' ')
        if a[11] == False:
            dockeys.content_control_forms_and_form_fields[11].set_text(' ')
        if a[12] == False:
            dockeys.content_control_forms_and_form_fields[12].set_text(' ')
        if a[13] == False:
            dockeys.content_control_forms_and_form_fields[13].set_text(' ')

        nameNew = 'patterns/keysNEW' + str(i + 1) + '.docx'
        dockeys.save(nameNew)
        doc1 = DocxTemplate(nameNew)
        doc1.render(taskKeys)
        name2 = 'keys/keysVar' + str(i + 1) + '.docx'
        doc1.save(name2)




eel.init('web')
eel.start('index.html', mode='chrome')

# print(abz)
# for i in range(0, abz-1):
#     print(doc.paragraphs[i].text)
# docNew = Document()
# docNew.add_p
# docNew.save('tests.docx')
