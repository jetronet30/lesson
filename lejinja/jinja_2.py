from jinja2 import Template
from markupsafe import escape

data = '''

Hello {{name}}, your age is {{age*12}}

'''

tm = Template(data)

tmsg = tm.render(name='Tim', age=23)

print(tmsg)

termit = '{{carName}} is a good car'

tm_2 = Template(termit)

tmsg_2 = tm_2.render(carName='BMW')

print(tmsg_2)   

print("------------------")

data_2 = '''{% raw %}
Hello {{name}}, your age is {{age*12}}
{% endraw %}
'''

tm_3 = Template(data_2)

tmsg_3 = tm_3.render(name='Tim', age=23)

print(tmsg_3)

print("------------------")

link = '<a href="https://www.google.com">Google</a>'

tm_4 = Template(link)

tmsg_4 = tm_4.render()

print(tmsg_4)

print("------------------")

link_1 = '<a href="https://www.google.com">Google</a>'

tm_5 = Template("{{link_1 | e}}")

tmsg_5 = tm_5.render(link_1=link_1)

print(tmsg_5)

print("------------------")

link_2 = '<a href="https://www.google.com">Google</a>'

msg_6 = escape(link_2)

print(msg_6)