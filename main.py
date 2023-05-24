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
def build(a):
    document = DocxForm('pattern.docx')
    document.print_all_content_controls_and_form_fields()
    print(a)
    if a[1] == '0':
        document.content_control_forms_and_form_fields[0].set_text(' ')
        print(document.content_control_forms_and_form_fields[0].text)
    if a[2] == '0':
        document.content_control_forms_and_form_fields[1].set_text(' ')
        print(document.content_control_forms_and_form_fields[1].text)
    if a[3] == '0':
        document.content_control_forms_and_form_fields[2].set_text(' ')
        print(document.content_control_forms_and_form_fields[2].text)
    # if a[4] == '0':
    #     document.content_control_forms_and_form_fields[3].set_text(' ')
    #     print(document.content_control_forms_and_form_fields[3].text)
    # if a[5] == '0':
    #     document.content_control_forms_and_form_fields[4].set_text(' ')
    #     print(document.content_control_forms_and_form_fields[4].text)
    # if a[6] == '0':
    #     document.content_control_forms_and_form_fields[5].set_text(' ')
    #     print(document.content_control_forms_and_form_fields[5].text)
    # if a[7] == '0':
    #     document.content_control_forms_and_form_fields[6].set_text(' ')
    #     print(document.content_control_forms_and_form_fields[6].text)
    # if a[8] == '0':
    #     document.content_control_forms_and_form_fields[7].set_text(' ')
    #     print(document.content_control_forms_and_form_fields[7].text)
    # if a[9] == '0':
    #     document.content_control_forms_and_form_fields[8].set_text(' ')
    #     print(document.content_control_forms_and_form_fields[8].text)
    # if a[10] == '0':
    #     document.content_control_forms_and_form_fields[9].set_text(' ')
    #     print(document.content_control_forms_and_form_fields[9].text)

    document.save('patternNEW.docx');

    task1_mass = [
        random.randrange(10, 20),
        random.randrange(7, 9),
        random.randrange(3, 6),

    ]

    task2_mass = [
        random.randrange(0,1)+2,

    ]


    tasks = {
        'n11': str(task1_mass[0]),
        'm12': str(task1_mass[1]),
        't13': str(task1_mass[2]),
        # (math.factorial(task1_mass[0] - task1_mass[1]) * math.factorial(
        # task1_mass[2]) * math.factorial(task1_mass[0] - task1_mass[2]))
        # / (math.factorial(task1_mass[2]) * (
        #         task1_mass[0] - task1_mass[1] - task1_mass[2]) * math.factorial(task1_mass[0]))
        'ans11': '5',
        'ent' : '\n',
        'n21' : task2_mass[0]
    }

    doc = DocxTemplate('patternNEW.docx')
    doc.render(tasks)
    doc.save('tests.docx')


eel.init('web')
eel.start('index.html', mode='chrome')

# print(abz)
# for i in range(0, abz-1):
#     print(doc.paragraphs[i].text)
# docNew = Document()
# docNew.add_p
# docNew.save('tests.docx')
