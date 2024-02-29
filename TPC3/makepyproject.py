import jinja2
from glob import glob
import json
import os

#project name
nodes = glob("*.py")
if len(nodes)>=1:
    name = nodes[0].replace(".py","")
else:
    name = input("Modulo?")
    
    
pp = jinja2.Template('''
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{autor}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version", "description"]

dependencies = [
    "jjcli"
]

[project.scripts]
{{name}} = "{{name}}:main"
                     ''')

metadata_path = str(os.path.expanduser("~/.METADATA.json"))
file = open(metadata_path)
data = json.load(file)
autor = data["Username"]
email = data["Email"]


out = pp.render({"name":name,"autor":autor,"email":email})
print(out)

file_output = open("pyproject.toml","w")
file_output.write(out)