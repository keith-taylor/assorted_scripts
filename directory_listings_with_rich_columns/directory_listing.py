import os
import sys
from rich import print
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
import pathlib

directory_path = os.path.abspath(sys.argv[1])

def get_directory_contents(directory):
    dir_contents = []
    try:
        for item in os.listdir(directory):
            if item[0] == '.':  # remove hidden files
                continue
            elif os.path.isfile(os.path.join(directory, item)):
                if item[-3:] == '.py' or item[-4] == '.pyc':
                    file_type = 'file (.py)'
                else:
                    file_type = 'file'
                temp_dic = {'name': str(item), 'type': str(file_type)}
                dir_contents.append(temp_dic)
            else:
                temp_dic = {'name': str(item), 'type': 'folder'}
                dir_contents.append(temp_dic)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {directory}")
    except OSError as e:
        print(f"An OS error occurred: {e}")
    return dir_contents


def get_content(item):
    object_type = item['type']
    object_name = item['name']
    if object_type == 'file':
        return f"📄 [b]{object_type}[/b]\n[grey]{object_name}"
    elif object_type == 'file (.py)':
        return f"🐍 [b][grey]{object_type}[/b]\n{object_name}"
    else:
        return f"📂 [yellow][b]{object_type}[/b]\n{object_name}"


console = Console()
directory_contents = get_directory_contents(directory_path)
dir_renderables = [Panel(get_content(item), expand=True) for item in directory_contents]
console.print(Columns(dir_renderables))
