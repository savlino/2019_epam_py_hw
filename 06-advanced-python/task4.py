"""
graphic output of folder tree, works only for subfolders
"""

import os
import os.path

root_depth = os.getcwd().count(os.sep)


def path_finder(request_folder, check_path=None):
    for root, dirs, files in os.walk(check_path):
        for d in dirs:
            if d == request_folder:
                return os.path.join(root, d)


class PrintableFolder:
    def __init__(self, name, search_path=os.getcwd(), content=[]):
        self.name = name
        self.content = content
        self.abspath = path_finder(name, check_path=search_path)

    def __str__(self, level=0):
        print(f"{'|   ' * level}|-> V {self.name}")
        for root, dirs, files in os.walk(self.abspath):
            level = root.replace(self.name, '').count(os.sep) - root_depth
            while dirs:
                d = dirs[0]
                PrintableFolder(d, search_path=root).__str__(level)
                dirs.remove(d)
            for f in files:
                print(PrintableFile(f).__str__(level=level))
        return ""


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self, level):
        return f"{'|   ' * level}|-> {self.name}"


folder1 = PrintableFolder('folder1')
print(folder1)
