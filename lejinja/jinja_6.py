from jinja2 import Environment, FileSystemLoader, Template
from markupsafe import escape
from datetime import datetime
from time import sleep

subs = ["Anna", "Meri", "Luis", "Tim", "Bob", "Nana", "Margaret"]
print("-------------------------",'\n')

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
tm = env.get_template("ebaut2_.html")
tmsg = tm.render(list_table=subs)
print(tmsg)