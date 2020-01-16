"""
graphic output of folder tree, works only inside current working directory
"""

import os
import os.path
import sys
from contextlib import suppress

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

    def __repr__(self, level=0):
        print(f"{'|   ' * level}|-> V {self.name}")
        for root, dirs, files in os.walk(self.abspath):
            level = root.replace(self.name, '').count(os.sep) - root_depth
            globals()[self.name] = []
            while dirs:
                d = dirs[0]
                PrintableFolder(d, search_path=root).__repr__(level)
                globals()[self.name].append(d)

                dirs.remove(d)
            for f in files:
                globals()[f] = None
                globals()[self.name].append(globals()[f])
                print(PrintableFile(f, level=level).__repr__())
        return ""


class PrintableFile:
    def __init__(self, name, level):
        self.name = name

        self.level = level

    def __repr__(self):
        return f"{'|   ' * self.level}|-> {self.name}"


folder1 = PrintableFolder('folder1')
print(folder1)

print(file3 in folder2)
