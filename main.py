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
        task1_mass = [
            random.randrange(10, 20),
            random.randrange(7, 9),
            random.randrange(3, 6),

        ]

        task2_mass = [
            random.randrange(0, 2) + 2,

        ]

        tasks = {
            'n11': str(task1_mass[0]),
            'n12': str(task1_mass[1]),
            'n13': str(task1_mass[2]),
            # (math.factorial(task1_mass[0] - task1_mass[1]) * math.factorial(
            # task1_mass[2]) * math.factorial(task1_mass[0] - task1_mass[2]))
            # / (math.factorial(task1_mass[2]) * (
            #         task1_mass[0] - task1_mass[1] - task1_mass[2]) * math.factorial(task1_mass[0]))
            'ans1': str(random.randrange(10,50)),
            'ent': '\n',
            'n21': task2_mass[0]
        }
        document = DocxForm('pattern.docx')
        document.print_all_content_controls_and_form_fields()
        document.content_control_forms_and_form_fields[0].set_text('Вариант ' + str(i+1))
        if a[1] == False:
            document.content_control_forms_and_form_fields[1].set_text(' ')
            print(document.content_control_forms_and_form_fields[1].text)
        if a[2] == False:
            document.content_control_forms_and_form_fields[2].set_text(' ')
            print(document.content_control_forms_and_form_fields[2].text)
        if a[3] == False:
            document.content_control_forms_and_form_fields[3].set_text(' ')
            print(document.content_control_forms_and_form_fields[3].text)
        if a[4] == False:
            document.content_control_forms_and_form_fields[4].set_text(' ')
            print(document.content_control_forms_and_form_fields[4].text)
        if a[5] == False:
            document.content_control_forms_and_form_fields[5].set_text(' ')
            print(document.content_control_forms_and_form_fields[5].text)
        if a[6] == False:
            document.content_control_forms_and_form_fields[6].set_text(' ')
            print(document.content_control_forms_and_form_fields[6].text)
        if a[7] == False:
            document.content_control_forms_and_form_fields[7].set_text(' ')
            print(document.content_control_forms_and_form_fields[7].text)
        if a[8] == False:
            document.content_control_forms_and_form_fields[8].set_text(' ')
            print(document.content_control_forms_and_form_fields[8].text)
        if a[9] == False:
            document.content_control_forms_and_form_fields[9].set_text(' ')
            print(document.content_control_forms_and_form_fields[9].text)
        if a[10] == False:
            document.content_control_forms_and_form_fields[10].set_text(' ')
            print(document.content_control_forms_and_form_fields[10].text)
        if a[11] == False:
            document.content_control_forms_and_form_fields[11].set_text(' ')
            print(document.content_control_forms_and_form_fields[11].text)
        if a[12] == False:
            document.content_control_forms_and_form_fields[12].set_text(' ')
            print(document.content_control_forms_and_form_fields[12].text)
        teoria = ["13. Элементарное событие – это {{ent}}    А. Единичный исход; {{ent}}    Б. Число; {{ent}}    В. Эксперимент; {{ent}}    Г. Вывод.",
                  "13. Событие – это {{ent}}    А. Подмножество множества элементарных событий; {{ent}}    Б. Утверждение; {{ent}}    В. Пространство элементарных событий; {{ent}}    Г. Доказательство.",
                  "13. Вероятность – это {{ent}}    А. Степень возможности наступления некоторого события; {{ent}}    Б. Утверждение; {{ent}}    В. Множество; {{ent}}    Г. Эксперимент.",
                  "13. Вероятность наступления некоторого события не может быть равна {{ent}}    А. 2; {{ent}}    Б. 1; {{ent}}    В. 0; {{ent}}    Г. 0.5.",
                  "13. P(A+B)= (сложение вероятностей) {{ent}}    А. P(A)+P(B); {{ent}}    Б. P(A)-P(B); {{ent}}    В. P(AB)+P(A); {{ent}}    Г. P(AB)+P(B).",
                  "13. Случайное событие – это  {{ent}}    А. Может как произойти так и не произойти; {{ent}}    Б. Доказанное утверждение; {{ent}}    В. Очевидное свойство; {{ent}}    Г. Положительное число.",
                  "13. Случайная величина есть {{ent}}    А. Функция элементарных событий {{ent}}    Б. Число; {{ent}}    В. Вывод ; {{ent}}    Г. Эксперимент.",
                  "13. Функция распределения случайной величины есть {{ent}}    А. Функция одного действительного переменного; {{ent}}    Б. Функция элементарных событий; {{ent}}    В. Функция многих действительных переменных; {{ent}}    Г. Функция двух действительных переменных.",
                  "13. Вероятность того, что непрерывная случайная величина примет конкретное значение равна {{ent}}    А. 0; {{ent}}    Б. 1; {{ent}}    В. Зависит от задачи; {{ent}}    Г. Нет правильных ответов.",
                  "13. Что означает операция А+В?  {{ent}}    А. произошло хотя бы одно из двух событий А или В;  {{ent}}    Б. событие А влечет за собой событие В; {{ent}}    В. совместно осуществились события А и В; {{ent}}    Г. Событие В влечет за собой событие А.",
                  "13. Что означает операция АВ? {{ent}}    А. Произошло и событие А, и событие В; {{ent}}    Б. Произошло хотя бы одно из двух событий А или В; {{ent}}    В. Событие А влечет за собой событие В; {{ent}}    Г. Ни одно из событий не произошло.",
                  "13. Выберите неверное утверждение {{ent}}    А. Вероятность появления одного из противоположных событий всегда больше   вероятности другого; {{ent}}    Б. Сумма вероятностей двух противоположных событий равна единице; {{ent}}    В. Если два события единственно возможны и несовместны, то они называются противоположными; {{ent}}    Г. Событие, которое никогда не произойдет, является невозможным.",
                  "13. Максимальное значение произведения вероятностей противоположных событий равно {{ent}}    А. 0.25; {{ent}}    Б. 0.5; {{ent}}    В. 1; {{ent}}    Г. 0.54.",
                  "13. Парный коэффициент корреляции равен –1. Это означает {{ent}}    А. Отрицательную линейную связь; {{ent}}    Б. Наличие нелинейной функциональной связи; {{ent}}    В. Отсутствие связи; {{ent}}    Г. Положительную линейную связь.",
                  "13. Вероятности появления заданного числа благоприятных исходов в схеме Бернулли описываются {{ent}}    А. Биноминальным распределением; {{ent}}    Б. Геометрическим распределением; {{ent}}    В. Равномерным распределением на отрезке; {{ent}}    Г. Однородным распределением.",
                  "13. Математического ожидания не существует у случайной величины {{ent}}    А. Распределенной по Коши; {{ent}}    Б. Равномерно распределенной на отрезке; {{ent}}    В. Имеющей нормальное распределение; {{ent}}    Г. Неравномерно распределенной на отрезке.",
                  "13. Закон больших чисел выводится из неравенства Чебышева при условии существования у случайной величины {{ent}}    А. Конечного второго момента; {{ent}}    Б. Конечного математического ожидания; {{ent}}    В. Плотности; {{ent}}    Г. Дисперсии.",
                  "13. Характеристическая функция случайной величины есть {{ent}}    А. Комплекснозначная функция действительного переменного; {{ent}}    Б. Аналитическая функция комплексного переменного; {{ent}}    В. Действительная функция комплексного переменного; {{ent}}    Г. Мнимая функция комплексного переменного.",
                  "13. Если характеристическая функция случайной величины имеет производную в точке нуль, то {{ent}}    А. Случайная величина имеет конечное математическое ожидание; {{ent}}    Б. Случайная величина имеет плотность; {{ent}}    В. Случайная величина имеет конечный момент второго порядка; {{ent}}    Г. Все варианты неверные.",
                  "13. Зная характеристическую функцию можно определить функцию распределения {{ent}}    А. Произвольной случайной величины; {{ent}}    Б. Непрерывной случайной величины; {{ent}}    В. Простой случайной величины; {{ent}}    Г. Невозможно определить функцию распределения.",
                  "13. Двумерная случайная величина называется непрерывной, если ее функция распределения- {{ent}}    А. непрерывная, дифференцируемая по каждому из аргументов, и существует вторая смешанная производная; {{ent}}    Б. непрерывная, дифференцируемая по каждому из аргументов, и существует третья смешанная производная; {{ent}}    В. непрерывная; {{ent}}    Г. Ни один вариант не является верным.",
                  "13. Плотность распределения вероятностей непрерывной двумерной случайной величины –это {{ent}}    А. Вторая смешанная частная производная ее функции распределения; {{ent}}    Б. Сумма всех вероятностей; {{ent}}    В. Постоянная величина; {{ent}}    Г. Все варианты верные.",
                  "13. Математическое ожидание постоянной равно {{ent}}    А. Этой постоянной; {{ent}}    Б. 1; {{ent}}    В. 2; {{ent}}    Г. Нет верного варианта.",
                  "13. Для каких случайных величин справедливо свойство математического ожидания M (X + Y) = MX + MY {{ent}}    А. И для зависимых, и для независимых; {{ent}}    Б. Только для зависимых; {{ent}}    В. Только для независимых; {{ent}}    Г. Нет верного варианта.",
                  "13. Какой вероятности соответствует медиана? {{ent}}    А. 0,5; {{ent}}    Б. 1; {{ent}}    В. 0,25; {{ent}}    Г. Нет верного ответа.",
                  "13. Вставьте пропуск. {{ent}}Если Х – непрерывная случайная величина, то мода – __________________ плотности распределения {{ent}}    А. Точка локального максимума; {{ent}}    Б. Точка локального минимума; {{ent}}    В. Несуществующая точка; {{ent}}    Г. Нет верного ответа.",
                  "13. Числом, равным математическому ожиданию квадрата отклонения случайной величины от её математического ожидания называют {{ent}}    А. Дисперсию; {{ent}}    Б. Моду; {{ent}}    В. Медиану; {{ent}}    Г. Квантиль.",
                  "13. D(X+Y)= {{ent}}    А. DX+DY; {{ent}}    Б. D(XY); {{ent}}    В. DX+DY-D(XY); {{ent}}    Г. 0."]
        if a[13] == True:
            trand = random.randrange(0, len(teoria))
            print(teoria[trand])
            document.content_control_forms_and_form_fields[13].set_text(teoria[trand])

        name = 'patterns/patternNEW' + str(i+1) + '.docx'
        document.save(name)
        doc = DocxTemplate(name)
        doc.render(tasks)
        name1 = 'variants/var' + str(i+1) + '.docx'
        doc.save(name1)


eel.init('web')
eel.start('index.html', mode='chrome')

# print(abz)
# for i in range(0, abz-1):
#     print(doc.paragraphs[i].text)
# docNew = Document()
# docNew.add_p
# docNew.save('tests.docx')
