from jinja2 import FunctionLoader, Template, Environment, FileSystemLoader
from markupsafe import escape

from datetime import datetime
from time import sleep

persons = [
    {"name": "Anna", "age": 23, 'weight': 50},
    {"name": "Meri", "age": 23, "weight": 60},
    {"name": "Luis", "age": 23, "weight": 70},
    {"name": "Tim", "age": 23, "weight": 80},
    {"name": "Bob", "age": 23, "weight": 90},
    {"name": "Nana", "age": 23, "weight": 100},
    {"name": "Margaret", "age": 23, "weight": 110},]

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
tm = env.get_template("main.html")
tmsg = tm.render(users=persons)
print(tmsg)

print("------------------")
print("Function Loader")

def loadTpl(patch):
    if patch == 'index':
        return ''' name {{u.name}} age {{u.age}} weight {{u.weight}}'''
    else:
        return ''' daty {{u}}}'''
    
file_loader_f = FunctionLoader(loadTpl)    
env_f = Environment(loader=file_loader_f)
tm_f = env_f.get_template('index')
tmsg_f = tm_f.render(u=persons[0])
print(tmsg_f)
