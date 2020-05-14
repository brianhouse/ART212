#!/usr/local/bin/python3

import os, yaml, markdown, jinja2

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "content.yaml"))

with open(path) as f:
    projects = yaml.safe_load(f)

projects.sort(key = lambda p: p['name'])

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html")), 'w') as f:
    template = os.path.join(os.path.dirname(__file__), "template.html")
    renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(".")).get_template(template)
    output = renderer.render({'projects': projects})
    f.write(output)
