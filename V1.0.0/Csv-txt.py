import csv
import unicodedata
import re


csv_file_path = "Table generated for you.csv"
output_txt_path = "Txt file generated for you.txt"
encoding = "utf-8-sig"
col_sep_space = "    "

def clean_cell(text: str) -> str:
    invisible_pattern = re.compile(r'[\u200b-\u200f\uFEFF\u202a-\u202e\n\t\r]')
    return invisible_pattern.sub('', text).strip()

def get_real_display_width(text: str) -> int:
    width = 0
    for char in text:
        char_width_type = unicodedata.east_asian_width(char)
        if char_width_type in ('F', 'W', 'A'):
            width += 2
        else:
            width += 1
    return width

table_data = []
with open(csv_file_path, "r", encoding=encoding, newline='') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        cleaned_row = [clean_cell(cell) for cell in row]
        table_data.append(cleaned_row)


max_col_count = max(len(row) for row in table_data)
for row in table_data:
    if len(row) < max_col_count:
        row.extend([""] * (max_col_count - len(row)))


col_total = len(table_data[0])
max_col_widths = [0] * col_total
for col_index in range(col_total):
    col_cell_widths = [get_real_display_width(row[col_index]) for row in table_data]
    max_col_widths[col_index] = max(col_cell_widths)


formatted_content = []
for row in table_data:
    formatted_cells = []
    for col_index, cell in enumerate(row):
        cell_width = get_real_display_width(cell)

        fill_space = " " * (max_col_widths[col_index] - cell_width)
        formatted_cells.append(cell + fill_space)

    formatted_line = col_sep_space.join(formatted_cells)
    formatted_content.append(formatted_line)


with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(formatted_content))

print("The Txt file has been saved to:{}".format(output_txt_path))