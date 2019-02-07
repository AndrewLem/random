import os

base_folder = 'test_statements'
files = os.listdir(base_folder)
grads_statements = []
rows = 4
columns = 4
tables_folder = 'html_tables'
html_header = " <html> " \
              "<head> " \
              "<style> " \
              "table, th, td { border: 1px solid black; border-collapse: collapse; } " \
              "</style> " \
              "</head>"
html_footer = '</html>'
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
for i in range(0, len(grads_statements)):
    table_string = html_header + table_header
    for j in range(0, rows):
        table_string += row_start
        for k in range(0, columns):
            d1 = (d1 + 1) % len(grads_statements)
            if d1 == 0:
                d2 = d2 + 1
            table_string += cell_start
            table_string += grads_statements[d1][d2 % len(grads_statements[d1])]
            table_string += cell_end
        table_string += row_end
    table_string += table_footer + html_footer
    with open(os.path.join(tables_folder, f"{i}.html"), 'w') as f:
        f.write(table_string)
