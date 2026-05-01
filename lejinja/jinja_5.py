from jinja2 import FunctionLoader, Template, Environment, FileSystemLoader
from markupsafe import escape

from datetime import datetime
from time import sleep


file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
tm = env.get_template("page.html")
tmsg = tm.render(domain="http://127.0.0.1:5000", title="Jinja")
print(tmsg)
