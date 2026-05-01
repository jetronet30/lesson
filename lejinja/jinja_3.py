from jinja2 import Template
from markupsafe import escape
from datetime import datetime
from time import sleep

cars = [
    {"id": 1, "name": "BMW", "price": 23000},
    {"id": 2, "name": "Audi", "price": 15000},
    {"id": 3, "name": "Mercedes", "price": 18000},
    {"id": 4, "name": "Honda", "price": 10000},
    {"id": 5, "name": "Toyota", "price": 12000},
    {"id": 6, "name": "Volkswagen", "price": 11000},
    {"id": 7, "name": "Hyundai", "price": 9000},
]

tpl = "sum  cars price  {{cs | sum(attribute='price')}}"

tm = Template(tpl)

tmsg = tm.render(cs=cars)

print(tmsg)


# sum(iterable, atribute=None,start=0)

print("----------------")

digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tpl_1 = """ sum all digits  {{dd | sum}}"""

tm_1 = Template(tpl_1)

tmsg_1 = tm_1.render(dd=digit)

print(tmsg_1)


print("----------------")

tpl_2 = """ sum all digits  {{(maxPrice | max(attribute='price'))}}"""

tm_2 = Template(tpl_2)

tmsg_2 = tm_2.render(maxPrice=cars)

print(tmsg_2)


print("----------------")

tpl_3 = """ sum all digits  {{(cars | random)}}"""

tm_3 = Template(tpl_3)

tmsg_3 = tm_3.render(cars=cars)

print(tmsg_3)


print("----------------")

tpl_4 = """ sum all digits  {{(cars | replace('M', '0'))}}"""

tm_4 = Template(tpl_4)

tmsg_4 = tm_4.render(cars=cars)

print(tmsg_4)


print("----------------")

persons = [
    {"name": "Anna", "age": 23, 'weight': 50},
    {"name": "Meri", "age": 23, "weight": 60},
    {"name": "Luis", "age": 23, "weight": 70},
    {"name": "Tim", "age": 23, "weight": 80},
    {"name": "Bob", "age": 23, "weight": 90},
    {"name": "Nana", "age": 23, "weight": 100},
    {"name": "Margaret", "age": 23, "weight": 110},
]

tpl_5 = """
{%- for u in users -%}
{% filter upper %}{{u.name}} {% endfilter %}
{%- endfor -%}
"""

tm_5 = Template(tpl_5)

tmsg_5 = tm_5.render(users=persons)

print(tmsg_5)


print("----------------")

tpl_6 = """
{%- for u in users -%}
{% filter lower %}{{u.name}} {% endfilter %}
{%- endfor -%}
"""

tm_6 = Template(tpl_6)

tmsg_6 = tm_6.render(users=persons)

print(tmsg_6)


print("----------------")


html = ''' 
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{type}}" name="{{name}}" value="{{value | e}}" size="{{size}}"/>
{%- endmacro %}


<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password', type='password') }}
<p>{{ input('password', type='password', size=40) }}


'''

tm_7 = Template(html)
msg_7 = tm_7.render()

print(msg_7)


print("----------------")

persons_a = [{'name': 'Tim', 'age': 23, 'weight': 50}, 
             {'name': 'Anna', 'age': 23, 'weight': 60}, 
             {'name': 'Luis', 'age': 23, 'weight': 70},
             {'name': 'Tim', 'age': 23, 'weight': 80},
             {'name': 'Bob', 'age': 23, 'weight': 90},
             {'name': 'Nana', 'age': 23, 'weight': 100},
             {'name': 'Margaret', 'age': 23, 'weight': 110}]

html_1 = ''' 
{% macro list_users(users_of_users) -%}
<ul>
{% for u in users_of_users -%}
    <li>{{ u.name }} {{ caller(u) }}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
        <li>age : {{ user.age }}</li>
        <li>weight : {{ user.weight }}</li>
    </ul>
{% endcall %}

'''

tm_8 = Template(html_1)
msg_8 = tm_8.render(users=persons_a)

print(msg_8)