import os
from random import shuffle

base_folder = 'test_statements'
files = os.listdir(base_folder)
grads_statements = []
rows = 4
columns = 4
tables_folder = 'html_tables'
html_header = """ 
<html> 
    <head> 
        <style> 
            table{ 
                border: 1px solid black; 
                border-collapse: collapse;
                width: 100%;
            } 
            td{
                border: 1px solid black;
                padding: 5px;
                padding-bottom: 180px;
                width: 25%;
                text-align: left;
            }
            body{
                background-image: url("background_stone.jpg");
                background-repeat: no-repeat;
                background-size: auto;
            }
        </style> 
    </head>
"""
intro = """
    <body>
        <h1>2019 Graduate Canberra Tour People Bingo!</h1>
        Hi %s!<p>
        Can you fill in your bingo sheet? Match true statements to people's names!<p> 
        You'll notice there's 16 squares and only 13 other people, 
        so 3 people will appear on your sheet twice!<p>
        Share your favourite true statements/stories at the end of the day!<p>
        """
html_footer = '</body></html>'
table_header = '<table>'
table_footer = '</table>'
row_start = '<tr>'
row_end = '</tr>'
cell_start = '<td>'
cell_end = '</td>'

for file in files:
    with open(os.path.join(base_folder, file), 'r') as f:
        lines = f.readlines()
    grads_statements.append(lines)

d1 = -1
d2 = -1
output_lists = []
for i in range(0, len(grads_statements)):
    output_list = []
    for j in range(0, rows):
        for k in range(0, columns):
            d1 = (d1 + 1) % len(grads_statements)
            if d1 == 0:
                d2 = d2 + 1
            if d1 == i:
                d1 = (d1 + 1) % len(grads_statements)
            output_list.append(grads_statements[d1][d2 % len(grads_statements[d1])])
    output_lists.append(output_list)


i = 0
j = 0
for output_list in output_lists:
    shuffle(output_list)
    table_string = html_header + intro % files[j].replace('.txt', '') + table_header
    for output in output_list:
        if i % columns == 0:
            table_string += row_start
        i += 1
        table_string += cell_start
        table_string += output
        table_string += cell_end
        if i % columns == 0:
            table_string += row_end
    table_string += table_footer + html_footer
    j += 1
    with open(os.path.join(tables_folder, f"{j}.html"), 'w') as f:
        f.write(table_string)
