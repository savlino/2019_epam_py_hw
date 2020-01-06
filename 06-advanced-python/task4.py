"""
graphic output of folder tree, works only for subfolders
"""
import os
import os.path

root_depth = os.getcwd().count(os.sep)


def path_finder(request_folder, check_path=None):
    for root, dirs, files in os.walk(os.getcwd()):
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
        curr_dirs = set()
        curr_files = []
        for root, dirs, files in os.walk(self.abspath):
            level = root.replace(self.name, '').count(os.sep) - root_depth
            if dirs == []:
                for f in files:
                    print(PrintableFile(f).__str__(level=level))
            for d in dirs:
                PrintableFolder(
                    os.path.basename(d), search_path=root
                ).__str__(level)
                del dirs[dirs.index(d)]
                for f in files:
                    print(PrintableFile(f).__str__(level=level - 1))
        return ""


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self, level):
        return f"{'|   ' * level}|-> {self.name}"


folder2 = PrintableFolder('folder1')
print(folder2)
