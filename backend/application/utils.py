from jinja2 import Template 

def prepare_template( filename , html_data):
    with(open(filename, "r")) as file:
        temp = Template(file.read())
        output= temp.render(data = html_data)
        return output