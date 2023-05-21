import random
import math
import eel
import docx
from docx import Document
from docxtpl import DocxTemplate
from docx_form import DocxForm
import collections
from jinja2 import Template

@eel.expose
def makeVariants(a, b):
    print(a + b)

eel.init('web')
eel.start('index.html', mode='chrome')



doc = docx.Document('pattern.docx')
abz = len(doc.paragraphs)

document = DocxForm('pattern.docx')
document.print_all_content_controls_and_form_fields()

task1_mass = [
    random.randrange(10, 20),
    random.randrange(7, 9),
    random.randrange(3, 6),
]
task_1 = {'n11': str(task1_mass[0]),
          'm12': str(task1_mass[1]),
          't13': str(task1_mass[2]),
          'ans11' : str((math.factorial(task1_mass[0]-task1_mass[1])*math.factorial(task1_mass[2])*math.factorial(task1_mass[0]-task1_mass[2]))
                        /(math.factorial(task1_mass[2])*(task1_mass[0]-task1_mass[1]-task1_mass[2])*math.factorial(task1_mass[0])))
           }

tm = Template('')



doct = DocxTemplate('pattern.docx')
doct.render(task_1)
doct.save('tests.docx')
# print(abz)
# for i in range(0, abz-1):
#     print(doc.paragraphs[i].text)
# docNew = Document()
# docNew.add_p
# docNew.save('tests.docx')
