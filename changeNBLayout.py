from IPython.core.display import HTML, display

display(HTML('''
    <style>
    @import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');
    </style> '''))

# Change the default cell width for all cell types (code, raw, markdown, mathJax)
display(HTML('<style> .container {width: 90%} </style>'))

display(HTML('''
    <style> .CodeMirror {font-size: 10.5pt !important} </style>'''))

display(HTML('''
    <style> div.cell.selected{border: 0px};</style>'''))

# Change the font used by markdown cells
# Change the line-spacing between text lines
# Change the size of body text in markdown cells
display(HTML('''<style> 
    .text_cell_render {
        font-family: "Roboto Condensed"; 
        line-height: 145%; 
        font-size: 14pt} </style>'''))

# Change the size of text in code-cell output
display(HTML('''<style> 
    .output_area {font-size: large} </style>'''))
