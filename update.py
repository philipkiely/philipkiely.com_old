import os
from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    os.system("cp -r ../theme/static/ theme/")
    os.system("cp ../theme/templates/base.html .")
    env = Environment(autoescape=False, loader=FileSystemLoader("/Users/Philip/Code/web/philipkiely.com/philipkiely/"), trim_blocks=False)
    html = env.get_template("source.html").render()
    with open("index.html", "w") as f:
        f.write(html)
