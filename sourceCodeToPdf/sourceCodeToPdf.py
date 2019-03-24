from pygments import highlight
""" CLexer CppLexer PythonLexer """
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
"""from html import escape"""
import sys
from weasyprint import CSS, HTML

if len(sys.argv) != 3:
    sys.exit("Usage: python3 sourceCodeToPdf.py INPUT OUTPUT")

input = sys.argv[1]
output = sys.argv[2]

with open(input, "r") as file:
    lines = file.read()

markup = "<!DOCTYPE>\n"
markup += "<html>\n"
markup += "<head>\n"
markup += "<style>\n"
markup += "</style>\n"
markup += "</head>\n"
markup += "<body>\n"
markup += "<pre>\n"
markup += highlight(lines, PythonLexer(), HtmlFormatter(linenos="inline"))
markup += "</pre>\n"
markup += "</body>\n"
markup += "</html>\n"

properties = "@page { margin: .5in; size: letter landscape; }"
properties += "pre { font-size: 10pt; overflow-wrap: break-word; white-space: pre-wrap; }"
properties += ".highlight { background: inherit; }"
properties += ".lineno { color: gray; }"

css1 = CSS(string=properties)
css2 = CSS(string=HtmlFormatter().get_style_defs(".highlight"))

html = HTML(string=markup)
html.write_pdf(output, stylesheets=[css2, css1])

print("Done!")
