import subprocess
from openpyxl import load_workbook

def execute_shell_commands(commands):
    for command in commands:
        subprocess.call(command, shell=True)

def get_excel_column(file_path, column):
    workbook = load_workbook(file_path)
    sheet = workbook.active
    column_values = [cell.value for cell in sheet[column]]
    return column_values[1:]  # Exclude the header

if __name__ == '__main__':
    excel_file = 'fdgjl.xlsx'
    column_letter = 'Ｙ'
    
    commands = get_excel_column(excel_file, column_letter)
    execute_shell_commands(commands)
