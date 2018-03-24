from jinja2 import Template
template = Template('私は {{ name }} に入信した！')
print(template.render(name='Jinja2'))
