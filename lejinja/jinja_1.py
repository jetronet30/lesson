from jinja2 import Template

name = "Suzie"
age = 23

tm = Template("Hello {{name.upper()}} your age is {{age*12}}")

tmsg = tm.render(name=name ,age=age)

print(tmsg)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        

per = Person("Tim", 23)    

tm_1 = Template("Hello {{per.name}} your age is {{per.age}}")

tmsg_1 = tm_1.render(per=per)

print(tmsg_1)


print("------------------")

person_2 = {"name": "Janet", "age": 22}

tm_2 = Template("Hello {{p.name}} your age is {{p.age}}")

tmsg_2 = tm_2.render(p=person_2)

print(tmsg_2)
