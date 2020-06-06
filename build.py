#!/usr/bin/env python3

import os
from jinja2 import Environment, FileSystemLoader

PAGES = [
    'index.html',
    'rules.html',
    'faq.html',
    'documentation.html'
]

os.system('rm -rf build/*')
os.system('touch build/.keep') # don't mess up version control

print('Copying static files...')
os.system('cp -r static/* build')

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

for page in PAGES:
    print(f'Generating {page}...')
    
    template = env.get_template(page)    
    output = template.render()

    with open(f'build/{page}', 'w') as fh:
        fh.write(output)

    
