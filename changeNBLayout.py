import IPython.core.display as dis
from IPython.core.display import HTML, display

# Change the default cell width for all cell types (code, raw, markdown, mathJax)
display(HTML('<style> .container {width: 90% !important} </style>'))

display(HTML('''
    <style> .CodeMirror {font-size: 10.5pt !important} </style>'''))

display(HTML('''
    <style> div.cell.selected{border-left-width: 5px !important}</style>'''))

# Change the focnt used by markdown cells
# Change the line-spacing between text lines
# Change the size of body text in markdown cells
display(HTML('''<style> 
    .text_cell_render {
        font-family: "roboto condensed"; 
        line-height: 145%; 
        font-size: 13pt} </style>'''))

# Change the size of text in code cells
# Change the size of text in code-cell output
display(HTML('''<style> 
    .CodeMirror {font-size: large} 
    .output_area {font-size: large} </style>'''))

display(HTML('''<style> MathJax.Hub.Config {
  "HTML-CSS": {
    preferredFont: "Tex"}}</style>'''))