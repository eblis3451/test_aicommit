import subprocess
from openpyxl import load_workbook

def execute_shell_commands(commands):
    for command in commands:
        subprocess.call(command, shell=True)

# 從Excel的某一列讀取數據
def get_excel_column(file_path, column):
    workbook = load_workbook(file_path)
    sheet = workbook.active
    return [cell.value for cell in sheet[column]][1:]

if __name__ == '__main__':
    excel_file = 'testy.xlsx'
    column_letter = 'G'  
    
    # 從Excel讀取命令並執行
    commands = get_excel_column(excel_file, column_letter)
    execute_shell_commands(commands)