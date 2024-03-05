#!/usr/bin/env python3
"""python makepyproject.py"""
import jjcli
import jinja2
from glob import glob
import json
import os

def main():
    #project name
    nodes = glob("*.py")
    if len(nodes)>=1:
        name = nodes[0].replace(".py","")
    else:
        name = input("Modulo?")
        
    v = jjcli.qx(f"grep name '{name}'.py")
    print("debug",len(v))
    version = "0.0.1"
    pp = jinja2.Template('''    
    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{name}}"
    authors = [
        {name = "{{autor}}", email = "{{email}}"},
    ]
    version = "{{version}}"
    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]
    requires-python = ">=3.8"
    dynamic = ["description"]

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


    out = pp.render({"version":version ,"name":name,"autor":autor,"email":email})
    print("debug",out)

    file_output = open("pyproject.toml","w")
    file_output.write(out)

if __name__ == "__main__":
    main()
