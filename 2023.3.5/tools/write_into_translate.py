import io
import os
import os.path
import sys
import time
from dytree_config import *
import os

import json
def linux_tree_list_dir_demo1(path, depth=0):
    if depth == 0:
        print(path)
    items = os.listdir(path)
    for item in items:
        # 输出文件夹中的文件和子文件夹名
        # ：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。
        print('|    ' * depth, end='')
        print('|----', item)
        item = os.path.join(path, item)
        if os.path.isdir(item):
            # 递归遍历子目录
            linux_tree_list_dir_demo1(item, depth + 1)


def linux_tree_list_dir_demo2(dir_name, deepth=0):
    os.chdir(dir_name)
    # text1 =
    print("|" + "----" * deepth, os.getcwd())
    child_dirs = []
    for item in os.listdir("."):
        if os.path.isdir(item):
            child_dirs.append(item)
        else:
            print("|    " * (deepth + 1), "|---- ", item, "    [ Size: ", os.path.getsize(item), "]")
    for child_dir in child_dirs:
        linux_tree_list_dir_demo2(child_dir, deepth + 1)
    os.chdir("..")


def linux_tree_list_dir(dir_name, deepth=0):
    os.chdir(dir_name)
    print("|" + "----" * deepth, os.getcwd())
    child_dirs = []
    for item in os.listdir("."):
        if os.path.isdir(item):
            child_dirs.append(item)
        else:
            print("|    " * (deepth + 1), "|---- ", item, "    [ Size: ", os.path.getsize(item), "]")
    for child_dir in child_dirs:
        linux_tree_list_dir_demo2(child_dir, deepth + 1)
    os.chdir("..")


def make_print_to_file(path="./"):
    class Logger(object):
        def __init__(self, filename="d.log", path="./"):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
            self.terminal = sys.stdout
            self.log = open(os.path.join(path, filename), "a", encoding="utf-8")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass

    sys.stdout = Logger(TRANSLATE_FILENAME, path=path)


def writeinto_htmlfile(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")


def writeinto_txtfile(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")


def readDatafile(filename):
    line_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line_list.append(line)
    return line_list


def read_txtfile_to_html(htmlname, textname):
    css_template_str = "<style>    #dir1    {background-color:#54aeff;}#dir2{color:#cf222e;}#dir3{color:#000000;}#dir4{color:#0969da;}</style>"
    writeinto_htmlfile(htmlname, css_template_str)
    big_list = []
    list_ret = readDatafile(textname)
    for item in list_ret:

        if item.count("|") == 1:
            ret = "<h4 id='dir1'>{0}</h4>".format(item)
            big_list.append(ret)
        elif item.count("|") == 2:
            ret = "<h4 id='dir2'>{0}</h4>".format(item.replace("     ", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"))
            big_list.append(ret)

        elif item.count("|") == 3:
            ret = "<h4 id='dir3'>{0}</h4>".format(item)
            big_list.append(ret)
        else:
            ret = "<h4 id='dir4'>{0}</h4>".format(item)
            big_list.append(ret)

    for item in big_list:
        writeinto_htmlfile(htmlname, item)
class Out_templates():
    def exec(self):
        templates_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), src_path)
        dytree_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), dst_path)
        static_path_json = os.path.join(dytree_path, jsonfile)
        self.output_json(static_path_json, templates_path)



    def tree_path_json(self,path):
        dir_structure = {}
        base_name = os.path.basename(os.path.realpath(path))
        if os.path.isdir(path):
            dir_structure[base_name] = [self.tree_path_json(os.path.join(path, file_name)) for file_name in os.listdir(path)]
        else:
            return os.path.basename(path)
        return dir_structure

    # 1. 先生成文件目录的列表
    # 2. 把文件目录的列表塞进json里面

    def writeinto_jsonfile(self,filename,list_data):
        with open(filename, 'w', encoding='utf-8') as fw:
            json.dump(list_data, fw, indent=2, ensure_ascii=False)
            fw.close()


    def output_json(self,jsonfile,path):
        big_dict = dict(self.tree_path_json(path))
        self.writeinto_jsonfile(jsonfile,[big_dict])
        print(big_dict)


if __name__ == "__main__":
    # read dir--->file---->read----> write into html
    jsonfile = "templates.json"
    dst_path =  "static"
    src_path = "templates"
    ins = Out_templates()
    ins.exec()

    make_print_to_file(path=os.getcwd())
    dytree_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")),"static")
    linux_tree_list_dir(dytree_path)



