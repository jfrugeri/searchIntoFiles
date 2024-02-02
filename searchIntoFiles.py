import os
import time
import argparse
from termcolor import colored
import sys

def display_banner():
    banner = '''
+-----------------------------------------------+
| SEARCH INTO FILES                      	|
|                                        	|	
| Author: Juan Frugeri                   	|
| Github: jfrugeri                              |
|                                        	|
| Description: Python script for keyword search |
| in text files across directories.             |
+-----------------------------------------------+
'''
    print(banner)

def read_file(file_path, keyword):
    encodings = ['utf-8', 'iso-8859-1', 'latin1']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                for line in f:
                    if keyword in line:
                        return line
        except UnicodeDecodeError:
            continue
    return None

def search_keyword(directory, keyword):
    start_time = time.time()
    found_files = []
    total_files = 0
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                total_files += 1
                full_path = os.path.join(folder, file)
                line_content = read_file(full_path, keyword)
                if line_content:
                    found_files.append((full_path, line_content))

    print()
    if found_files:
        print(colored('Keyword found in the following files:', 'green', attrs=['bold']))
        for path, line in found_files:
            print(colored(f'Path: {path}'))
            print(colored(f'Line: {line}', 'green'))
            print()
    else:
        print(colored('Keyword not found in any file.', 'red', attrs=['bold']))

    end_time = time.time()
    print(colored(f'Total files processed: {total_files}', 'blue', attrs=['bold']))
    if found_files:
        print(colored(f'Total files containing the keyword: {len(found_files)}', 'green', attrs=['bold']))
    print(colored(f'Total execution time: {end_time - start_time:.2f} seconds', 'white', attrs=['bold']))

def main():
    try:
        parser = argparse.ArgumentParser(prog='python3 searchIntoFiles.py', description='Search for a keyword in .txt files from a specific directory.')
        parser.add_argument('-k', '--keyword', required=True, help='Keyword to be searched. Exemple: -k keyword')
        parser.add_argument('-p', '--path', required=True, help='Exemple: -p "/home/user/exemple/directories/"')

        args = parser.parse_args()
        print()
        print(colored('LOADING......', 'blue', attrs=['bold']))
        search_keyword(args.path, args.keyword)

    except (argparse.ArgumentError, SystemExit):
        display_banner()
        parser.print_help()
        sys.exit(2)

if __name__ == '__main__':
    main()
