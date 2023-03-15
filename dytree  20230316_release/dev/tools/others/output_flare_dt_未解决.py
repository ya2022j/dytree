#
#
#
#
#
# import os
#
#
# temp_json = [
#     {"name": "demo-data.js"},
#     {"name": "flare-data.js"},
#     {
#         "name": "Golang",
#         "children": [
#             {"name": 'd.pdf'}
#         ]
#
#     },
#     {
#         "name": "Python",
#         "children": [
#             {
#                 "name": "d",
#                 "children": [
#                     {"name": 't.py'},
#                     {"name": "dd"}
#                 ]
#             }
#         ]
#     }
# ]
# def tree_path_json(path):
#     dir_structure = {}
#     base_name = os.path.basename(os.path.realpath(path))
#     if os.path.isdir(path):
#         dir_structure[base_name] = [tree_path_json(os.path.join(path, file_name)) for file_name in os.listdir(path)]
#     else:
#         return os.path.basename(path)
#     return dir_structure
# # {'name': 'Golang', 'children': [{'name': 'd.pdf'}]}
# # {'name': 'Python', 'children': [{'name': 'd', 'children': [{'name': 't.py'}, {'name': 'dd'}]}]}
# d ={
#    "Pthon":[
#       {
#          "d":[
#             "t.py",
#              "dd"
#          ]
#       }
#    ]
# }
#
# # {
# #    "name":"Python",
# #    "children":[
# #       {
# #          "name":"d",
# #          "children":[
# #             {
# #                "name":"t.py"
# #             },
# #             {
# #                "name":"dd"
# #             }
# #          ]
# #       }
# #    ]
# # key_list = []
# # value_list = []
# # def iterdict(d):
# #     if type(d) == str:
# #         d_ = {}
# #         d_["name"]= d
# #         value_list.append(d_)
# #     else:
# #
# #
# #         for k,v in d.items():
# #             if isinstance(v, list) ==False:
# #                 key_list.append({"name":k})
# #                 value_list.append({"children":v})
# #             else:
# #                 iterdict(v[0])
#
# # iterdict({'Pthon': [{'d': ['t.py']}]})
# # print(key_list)
# # print(value_list)
#
#
# # def ddd(*args):
# #
# #     if type(args) == str:
# #         file_list = []
# #         file_dict = {}
# #         file_dict["name"] = args
# #         file_list.append(file_dict)
# #     elif type(args) == dict:
# #
# #
# #         for k,v in args.items():
# #             dict_list = []
# #             if type(v[0]) == dict:
# #                 for k1,v1 in v[0].items():
# #                     dd = {}
# #                     dd["name"] = k
# #                     dd["children"] = v
# #                     dict_list.append(dd)
# #                     ddd(v1[0])
# #
# #
# #             else:
# #                 ddd(v[0])
# # def nest_folder_file(item):
# #     ret_list = []
# #     if type(item) == str:
# #         str_list = []
# #         str_list.append({"name":item})
# #         ret_list.append(str_list)
# #         if type(item) == dict:
# #             for k, v in item.items():
# #                 if type(v[0]) == dict :
# #                     nest_folder_file(v[0])
# #                 elif  type(v[0]) == str :
# #                     children_list = []
# #                     kv_dict = {}
# #                     kv_dict["name"] = k
# #                     kv_dict["children"] = v
# #
# #                     children_list.append(kv_dict)
# #                     ret_list.append({"children":children_list})
# #
# #
# #
# #
# #     print(ret_list)
#         #
#
#         #     else:
#         #
#         #
#
#
#
#
# class C():
#     def __init__(self,datas):
#         self.datas = datas
#
#     def analyze_data(self,data,):
#
#         if isinstance(data,dict):
#             for k,v in data.items():
#                 self.analyze_data(v,{"name":})
#
#
#
#
# # demo-data.js
# # flare-data.js
# # {'Golang': ['d.pdf']}
# # {'Python': [{'d': ['t.py']}]}
# if __name__ =="__main__":
#     base_dir = "C:\\Users\\KSP184L\\Desktop\\開発環境構築\\印西以外の資料\\dtree_static"
#     # 1. A/B----> 2l_nested_dir
#     # 2. A/B---->  dir_string
#     # dir_list = []
#     # dir_string_list = []
#     # file_list = []
#     # path_info =""
#     # for (dirname, subdir, subfile) in os.walk(base_dir):
#     #     ret_file = [os.path.join(dirname,x) for x in subfile]
#     #     for item in ret_file:
#     #         file_list.append(item)
#     #
#     #
#     # for item in file_list:
#     #     exec_file = item.split("\\")
#     #     print(exec_file)
#     # d = tree_path_json(base_dir)
#     #
#     # for item in d.values():
#     #     for single_item in item:
#     #         if type(single_item)!=str:
#     #             for k,v in single_item.items():
#     #                 print(k,v)
#     #                 if type(v[0])
#                 # if single_item.values0] !=str:
#                 #
#                 # #     print(k,v)
#     #         nest_folder_file(single_item)
#     # nest_folder_file(["demo-data.js"])
#     # for item in temp_json:
#     #     if len(item)==1:
#     #         pass
#     #     else:
#     #         print(item)
#         # dir_sting = exec_file[2] + "/" + exec_file[3]
#         # dir_string_list.append(dir_sting)
#         # dir_path = os.path.join(os.path.join(base_dir,exec_file[2]),exec_file[3])
#         # dir_list.append(dir_path)
#     # for one_dir,one_dir_string in zip(dir_list,dir_string_list):
#     #     print(one_dir,one_dir_string)
#
#
# # ["a","b","c","d"]----> {"name":"a","children":[{"name":"b","children":[{"name":"c","children":[{"name":"d"}]}]}]}]}
# import copy
# import re
#
# json_ret = {"name":"Python","children":[{"name":"d","children":[{"name":"t.py"},{"name":"dd"}]}]}
#
# d={}
#
# if type(d["children"]) ==list and  type(d["children"][0]) == dict:


# key_list = []
# value_list = []
#
# def nest_list_dict(dict_list):
#     for k,v in dict_list[0].items():
#
#
#         key_list.append({"name":k})
#         value_list.append({"children":v})
#
#         if type(v[0]) ==dict:
#             nest_list_dict(v)


# 1 所有元素都变成{"name":item} 的value
# 2 所有的list[]都变成{"children":item}的value
# 也就是递归遍历所有元素？ 用正则匹配字符串和列表处理吧

# old_dt = [{"python":[{"d":["dd","t.py"]}]}]
#
# ret_list = []
# def nest_dd(list_dict):
#
#
#     if type(list_dict)==list and type(list_dict[0]) == dict:
#         d = {}
#         getkey = lambda x: [x for x in list_dict[0].keys()][0]
#         getvalue = lambda x: [x for x in list_dict[0].values()][0]
#         d["name"] = getkey(list_dict)  # k
#         d["children"] = getvalue(list_dict)  #
#
#         if type(d["children"]) ==list and  type(d["children"][0]) == dict:
#             nest_dd(d["children"])
#         ret_list.append(d)
#     # 使用lambda表达式，也就是用匿名函数简化取字典key,value的步骤
# nest_dd(old_dt)
# print(ret_list)
# print(ret_list[0])
# print(ret_list[1])
# print(len(ret_list))
# for item in ret_list:
#
#     getkey = lambda x: [x for x in item.keys()][0]
#     getvalue = lambda x: [x for x in item.values()][0]
#     getallvalue = lambda x:[x for x item.items)]
#     print(item,getvalue(item))



# python  [{'d': ['dd', 't.py']}]}
# d ['dd', 't.py']
# # pattern_str = re.compile("(".*?"),re.S)
# ret = []
# def nest_re(string):
#
#     pattern_list = re.compile('\[(.*?)\]',re.S)
#     items = re.findall(pattern_list,string)
#     print(items)
#     print(items[0])
#     # ret_string = '[{0}]'.format(items[0])
#     # ret.append(ret_string)
#     # if ":" in items[0]:
#     #     nest_re(items[0])
#
# nest_re(old_dt)
# print(ret)
#


## 2023.1.27

# getkey = lambda x: [x for x in a.keys()][0]
#         getvalue = lambda x: [x for x in a.values()][0]


# {'ab': [{'ac': 1}]}

#==> 'ab' ---> "name":"ab"

#{"name":"ab","children":[{"name":'ac', "children":[{"name":1}]}]}

# [{'ac': 1}]--->"children":[{"name":'ac', "children":[{"name":1}]}]

# {'ac': 1} ---> {"name":'ac', "children":[{"name":1}]}

# "ab"---->"name":'ac'
# 1 ---> "children":[{"name":1}]

# key----> d["name"] = getkey
# value ----> d["children"] = [{""}]
dd = {}
def nest_(dict_item):
    if type(dict_item) == dict:
        getkey = lambda x: [x for x in dict_item.keys()][0]
        getvalue = lambda x: [x for x in dict_item.values()][0]
        dd["name"] = getkey
        dd["children"] = getvalue
        if type(dd["children"][0]) == dict :
            nest_(dd["children"][0])
    print(dict_item)

d = {'ab': [{'ac': 1}]}
nest_(d)
print(dd)