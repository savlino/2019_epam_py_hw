"""
graphic output of folder tree
"""
import os
import os.path


def path_finder(request_folder):
    for root, dirs, files in os.walk("/home"):
        for d in dirs:
            if d == request_folder:
                return os.path.join(root, d)


class PrintableFolder:
    def __init__(self, name, content=[]):
        self.name = name
        self.content = content
        self.abspath = path_finder(name) or None

    def __str__(self, level=0):
        print(f"{'|   ' * level}|-> V {self.name}")
        curr_dirs = set()
        curr_files = []
        for root, dirs, files in os.walk(self.abspath):
            level = root.replace(self.name, '').count(os.sep) - 4
            if dirs == []:
                for f in files:
                    print(PrintableFile(f).__str__(level=level))
            for d in dirs:
                PrintableFolder(os.path.basename(d)).__str__(level)
                del dirs[dirs.index(d)]
                for f in files:
                    print(PrintableFile(f).__str__(level=level - 1))
        return ""


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self, level):
        return f"{'|   ' * level}|-> {self.name}"


folder1 = PrintableFolder('folder1')
print(folder1)
