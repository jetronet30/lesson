from jinja2 import Template
from markupsafe import escape
from datetime import datetime
from time import sleep


data = ''' test  test  test  
generate {{name}} test test 
test test'''

tm = Template(data)

tmsg = tm.render(name="Suzie")

print(escape(tmsg))

 

# data_1 = ''' test  test  test  
# generate {{time}} test test 
# test test'''

# tm_1 = Template(data_1)



# for i in range(10):
#     tmsg_1 = tm_1.render(time=datetime.now())
#     sleep(1)
#     print(tmsg_1)


data_2 = '''{% raw %} test  test  test  
generate {{time}} test test 
test test {% endraw %}'''

msg_2 = Template(data_2).render(time=datetime.now())

print(msg_2)

print("-------------")

link = ''' Html link this is <a href="https://www.google.com">Google</a>'''

msg_3 = Template(link).render()

print(msg_3)

print("-------------")
print("-------------")
link_1 = ''' Html link this is <a href="https://www.google.com">Google</a>'''

tm_2 = Template("{{link_1 | e}}")

msg_4 = tm_2.render(link_1=link_1)

print(msg_4)


print("-------------")
print("-------------")
link_2 = ''' Html link this is <a href="https://www.google.com">Google</a>'''

msg_5 = escape(link_2)

print(msg_5)


print("-------------")

#for

cities = [{'id': 1, 'name': 'Tbilisi'}, 
          {'id': 2, 'name': 'Batumi'}, 
          {'id': 3, 'name': 'Kutaisi'},
          {'id': 4, 'name': 'Rustavi'}]
link_3 = '''<select name="cities">
{% for city in cities -%}
    <option value="{{city.id}}">{{city.name}}</option>
{% endfor -%}
</select>'''

tm_3 = Template(link_3)

msg_6 = tm_3.render(cities=cities)

print(msg_6)


print("-------------")
print("########################################")

# if

cities_l = [{'id': 1, 'name': 'Tbilisi'},
            {'id': 2 ,'name': 'London'},
            {'id': 3, 'name': 'Batumi'},
            {'id': 4, 'name': 'Kutaisi'},
            {'id': 5, 'name': 'Rustavi'},
            {'id': 6, 'name': 'New York'},
            {'id': 7, 'name': 'San Francisco'}]

link_select = '''<select name="cities">
{% for city in cities -%}
{% if city.id >= 6 -%}
        <option value="{{city.id}}">{{city.name}}</option>
{% endif -%}
{% endfor -%}
</select>'''

tm_4 = Template(link_select)

msg_7 = tm_4.render(cities=cities_l)

print(msg_7)


print("-------------")
print("-------------")

cities_la = [{'id': 1, 'name': 'Tbilisi'},
             {'id': 2 ,'name': 'London'},
             {'id': 3, 'name': 'Batumi'},
             {'id': 4, 'name': 'Kutaisi'},
             {'id': 5, 'name': 'Rustavi'},
             {'id': 6, 'name': 'New York'},
             {'id': 7, 'name': 'San Francisco'},
             {'id': 8, 'name': 'Los Angeles'},
             {'id': 9, 'name': 'Chicago'},
             {'id': 10, 'name': 'Houston'},
             {'id': 11, 'name': 'Dallas'},
             {'id': 12, 'name': 'Philadelphia'},
             {'id': 13, 'name': 'Miami'}]

link_selector = '''<select name="cities">
{% for city in cities -%}
        <option value="{{city.id}}" {% if city.id == 8 %} selected {% endif %} >{{city.name}}</option>
{% endfor -%}
</select>'''

tm_5 = Template(link_selector)

msg_8 = tm_5.render(cities=cities_la)

print(msg_8)