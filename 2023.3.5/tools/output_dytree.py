#! -*- utf-8 -*-
import io
import os
import os.path
import sys
import time

import os

import json

############################################################
TRANSLATE_FILENAME = "dytree.html"  ##################
TRANSLATE_FILENAME_HTML = "templates"     ##################
HTML_FILENAME = "dytree.html"##################
jsonfile = "templates.json"               ##################
dst_path = "templates"                    ##################
src_path = "templates"                    ##################
linux_path = "/home/d_tree/templates"##################

############################################################

import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def linux_tree_list_dir_demo2(dir_name, deepth=0):
    os.chdir(dir_name)
    text1 = "".join("<h4 id='dir1'>" + "    " * deepth+ str(os.getcwd())+ "</h4>")
    print(type(text1),text1)
    print("\n")
    print("-"*100)
    writeinto_htmlfile("dytree.html", text1)
    writeinto_htmlfile("dytree.html", "\n")
    writeinto_htmlfile("dytree.html", "-" * 100)


    child_dirs = []
    for item in os.listdir("."):
        if os.path.isdir(item):
            child_dirs.append(item)
        else:
            if ".js" not in item and ".css" not in item :
                file_href= "/"+ os.getcwd().split("/")[-2]+"/"+os.getcwd().split("/")[-1]+"/"+"".join(item)
                file_href = file_href.replace("/static","")
                text2  = "    " * (deepth + 1)+"<a href='{0}'><h4 id='dir3'>    ".format(file_href)+"".join(item)+"</h4></a>"
                print(text2)
                writeinto_htmlfile("dytree.html", text2)
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



    def writeinto_jsonfile(self,filename,list_data):
        with open(filename, 'w', encoding='utf-8') as fw:
            json.dump(list_data, fw, indent=2, ensure_ascii=False)
            fw.close()


    def output_json(self,jsonfile,path):
        big_dict = dict(self.tree_path_json(path))
        self.writeinto_jsonfile(jsonfile,[big_dict])



if __name__ == "__main__":
    # read dir--->file---->read----> write into html

    ins = Out_templates()
    ins.exec()

    #  {% include "hp_base.html"%}
    writeinto_htmlfile("dytree.html", '{% include "hp_base.html"%}')
    make_print_to_file(path=os.getcwd())
    dytree_path = "/opt/resources"
    linux_tree_list_dir_demo2(dytree_path)

    # os.system(" mv /home/d_tree/tools/dytree.html /home/d_tree/templates")




