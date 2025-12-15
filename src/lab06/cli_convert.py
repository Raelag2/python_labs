import csv
import json
import sys 
import os
from openpyxl import Workbook
from pathlib import Path
import argparse

def csv_2_xlsx(input_file: str|Path, output_file: str|Path = None, encoding='utf-8'):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Основной лист'

    if output_file is None:
        input_path = Path(input_file)
        output_dir = Path('data/output_stuff')
        output_file = output_dir / f'{input_path.stem}.xlsx'

    with open(input_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row_num, row_data in enumerate(reader, 1):
            for col_num, cell_value in enumerate(row_data, 1):
                worksheet.cell(row=row_num, column=col_num, value=cell_value)
    workbook.save(output_file)  

def csv_2_json(input_file: str|Path, output_file: str|Path = None, encoding='utf-8'):
    data_list = []

    with open(input_file, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data_list.append(row)
    
    if output_file is None:
        input_path = Path(input_file)
        output_dir = Path('data/output_stuff')
        output_file = output_dir / f'{input_path.stem}.json'

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, ensure_ascii=False, indent=2)

def json_2_csv(input_file: str|Path, output_file: str|Path = None, encoding='utf-8'):
    with open(input_file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    
    if output_file is None:
        input_path = Path(input_file)
        output_dir = Path('data/output_stuff')
        output_file = output_dir / f'{input_path.stem}.csv'

    with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
        headers = json_data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(json_data)    

def configure_arguments():
    parser = argparse.ArgumentParser(description='Конвертер файлов между форматами CSV, JSON и Excel')
    parser.add_argument('--mode', type=str, required=True,
                        choices=['csv2json', 'json2csv', 'csv2xlsx'],
                        help='Выбор формата конвертации: csv2json, json2csv или csv2xlsx')
    parser.add_argument('--input', type=str, required=True,
                        help='Путь к исходному файлу для конвертации')
    parser.add_argument('--output', type=str,
                        help='Путь для сохранения конвертированного файла (опционально)')
    parser.add_argument('--encoding', type=str, default='utf-8',
                        help='Кодировка файлов (по умолчанию: utf-8)')
    args = parser.parse_args()
    
    if args.mode == 'csv2json':
        csv_2_json(args.input, args.output, args.encoding)
    elif args.mode == 'json2csv':
        json_2_csv(args.input, args.output, args.encoding)
    elif args.mode == 'csv2xlsx':
        csv_2_xlsx(args.input, args.output, args.encoding)    

if __name__ == '__main__':
    configure_arguments()