# Reappear-the-AI-form

## Project Overview
This project contains two Python scripts to streamline the processing of AI-generated table data, compatible with all common Python editors (Visual Studio, VS Code, PyCharm, Jupyter Notebook).

- `Editor.py`: Converts text copied from AI-generated tables into a standard CSV file
- `Csv_text.py`: Converts the generated CSV file into a TXT file

All generated CSV and TXT files will be saved in the same folder as the scripts.

## Usage Instructions
### Generate CSV file from AI table
1.  Open the project folder in your Python editor via the "Open File" option to access the source code
2.  Select and run the `Editor.py` file
3.  Paste the text copied from the AI-generated table into the runtime console (you can either paste the plain text directly, or use the copy button in the top-right corner of the AI table if available)
4.  Press Enter, input `generate` in the new line, then press Enter again to complete the generation.

### Generate TXT file from CSV
1.  Select and run the `Csv_text.py` file
2.  The TXT file will be generated automatically after the script finishes running.

## Important Notes
- The scripts will generate two files by default: `Table generate for you.csv` and `Txt file generate for you.txt`
- Existing files with the same names will be **automatically overwritten** when you re-run the scripts. If you need to retain previous results, please rename the existing files before re-running
- The scripts will automatically create the above two files on the first run, or when no files with matching names exist in the folder
- This project does not support LaTeX formula conversion. If the AI-generated table contains mathematical formulas, the output file will not be compiled correctly.

## BUG Handling & Limitations
- This project is compatible with 90% of AI-generated tables from Doubao and DeepSeek, but not with tables from Qianwen
- The script uses spaces to determine which string belongs to which table cell. If there are spaces inside a single cell of the AI-generated table, the output CSV/TXT file will be disorganized
- Fix for space-related errors:
  1.  Copy the table text to another place first, delete unnecessary spaces, then paste it into the runtime console; OR
  2.  After pasting the text and modifying the spaces in the runtime console, copy the revised full text, terminate the current run, start a new run, and paste the revised text into the new runtime console.
