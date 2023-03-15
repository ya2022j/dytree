
import requests
import os
import re

from bs4 import BeautifulSoup
from lxml import etree


def writeinto_txtfile(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")
        f.close()



def output_text(trans_filename,url):
    ret_list = []

    resp = requests.get(url)
    if "github.com" in url :

        element = etree.HTML(resp.text)

        xpath1 = element.xpath('/html/body/main/article/div/div/div[2]/div/div/section[2]/ul/li/a/text()')
        xpath2 = element.xpath('/html/body/main/article/div/div/div[2]/div/div/section[2]/ul/li/ul/li/a/text()')
        for item in xpath1:
            ret_list.append(item)
        for item in xpath2:
            ret_list.append(item)

        for item in ret_list:

            writeinto_txtfile(trans_filename, item)
    else:
        element = etree.HTML(resp.text)

        xpath1 = element.xpath('/html/body/main/article/div/div/div[1]/div[2]/div/section[2]/ul/li/a/text()')
        xpath2 = element.xpath('/html/body/main/article/div/div/div[1]/div[2]/div/section[2]/ul/li/ul/li/a/text()')
        for item in xpath1:
            ret_list.append(item)
        for item in xpath2:
            ret_list.append(item)

        for item in ret_list:

            writeinto_txtfile(trans_filename, item)

















class Output_Golang_FITM():


    def exec(self):
        writeinto_txtfile(htmlfile,header)
        self.dt_standby(datafile)
        self.output_method()
        self.output_indepent_func() # ok
        self.output_IT() # ok

        writeinto_txtfile(htmlfile,footer)
        if os.path.exists(src_file):
            os.remove(src_file)




    def dt_standby(self,datafile):
        ret = self.readDatafile(datafile)
        for item in ret:
            if "type " in item:
                type_list.append(item.split("type ")[1])
                pass  # interface  or struct
            elif "func" in item and "func (" not in item:
                independent_func_list.append(item)
                # indepent func 在整理独立函数或者方法时，可以把接口或者类型的关系也加入进去

            elif "func (" in item:  # 1.接收器的角度
                method_list.append(item)  # 2. 以方法的实际编写，尤其是返回值的角度




    def output_indepent_func(self):
        func_title  = '<li><a href="/">' + '&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145;  &nbsp;&nbsp;func:'+str(len(independent_func_list))+'&nbsp;&nbsp; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; ' + '</a></li> <br>'
        writeinto_txtfile(htmlfile,func_title)

        for item in independent_func_list:
            ret = self.get_corre_item_func(item, type_list)
            writeinto_txtfile(htmlfile,'<li><a href="/">&nbsp;&nbsp;' + self.bold_text_indepent(ret) + "&nbsp;&nbsp;</a></li> <br>")

            writeinto_txtfile(htmlfile,"\n")

    def output_IT(self):
        type_title = '<li><a href="/">' +'&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145;&nbsp;&nbsp;  type nums:'+str(len(type_list))+'&nbsp;&nbsp;&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; '+ '</a></li> <br>'
        writeinto_txtfile(htmlfile,type_title)
        for item in type_list:
            print(item)
            writeinto_txtfile(htmlfile,'<li><a href="/">' + item  + "</a></li> <br>")

    def output_method(self):
        try:
            method_ret_list = self.method_dt_standby()
            final_list = []
            for item in type_list:
                item_list = [item]
                for value in method_ret_list:

                    if self.bold_text_type_str(value) == item or self.bold_text_type_str(value) == "*"+item:
                        item_list.append(value)
                final_list.append(item_list)
            for one_type_methods in final_list:
                for item in one_type_methods:
                    if len(one_type_methods[1:]) !=0:

                        if item in type_list:
                            writeinto_txtfile(htmlfile,
                                '<li><a href="/">' + '&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145 &nbsp;&nbsp; {0} : Nums {1}&nbsp;&nbsp; &#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145 '.format(
                                    one_type_methods[0], len(one_type_methods[1:])) + '</a></li> <br>')
                        else:
                            writeinto_txtfile(htmlfile,item)
        except Exception as e:
            raise e


    def bold_text_method(self,old_string):
        # func URLFilters<        (filters ...*regexp.Regexp) CollectorOption
        # --->
        # func <strong>URLFilters</strong>              (filters ...*regexp.Regexp) CollectorOption
        pattern = re.compile('\)(.*?)\(', re.S)
        items = re.findall(pattern, old_string)
        new_string = old_string.replace(items[0], "<strong>{0}</strong>".format(items[0]))

        return new_string

    @staticmethod
    def readDatafile(filename):
        line_list = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip("\n")
                line_list.append(line)
        return line_list


    def get_corre_item_method(self,string_item,type_list):

        corre_type_list = []
        for type_item in type_list:
            if type_item in string_item:
                corre_type_list.append(type_item)
        if corre_type_list == []:
            ret_corre_item = ""
        else:
            ret_corre_item =  str(corre_type_list)[1:-1]
        ret  =  string_item + " &nbsp;&nbsp;   &#129320; |  &#10145 &nbsp;&nbsp; " + ret_corre_item
        return ret

    def get_corre_item_func(self,string_item,type_list):

        corre_type_list = []
        for type_item in type_list:
            if type_item in string_item:
                corre_type_list.append(type_item)
        if corre_type_list == []:
            ret_corre_item = ""
        else:
            ret_corre_item =  "<strong>" +str(corre_type_list)[1:-1] +"</strong>"
        ret  =  string_item + " &nbsp;&nbsp;   &#129320; |  &#10145 &nbsp;&nbsp; " + ret_corre_item
        return ret


    def bold_text_indepent(self,old_string):
        # func URLFilters<        (filters ...*regexp.Regexp) CollectorOption
        # --->
        # func <strong>URLFilters</strong>              (filters ...*regexp.Regexp) CollectorOption
        pattern = re.compile('func (.*?)\(',re.S)
        items = re.findall(pattern,old_string)
        new_string = old_string.replace(items[0],' &nbsp &nbsp <strong>{0}</strong> &nbsp &nbsp'.format(items[0]))

        return new_string


    def bold_text_type_str(self,string_item):
        method_str_pattern = re.compile("\(.*?\)",re.S)
        items = re.findall(method_str_pattern,string_item)[0]

        if " " in items:
            method_str = items.split(" ")[1].split(")")[0]
        else:
            method_str = items.replace("(","")
            method_str = method_str.replace(")","")
        return method_str

    def method_dt_standby(self):

        method_ret_list = []
        type_ret_list = []
        for item in method_list:
            ret = self.get_corre_item_method(item, type_list)
            method_ret_list.append('<li><a href="/">' + self.bold_text_method(ret) + "</a></li> <br>")
            type_pattern = re.compile("\(.*?\)",re.S)
            one_type = re.findall(type_pattern,'<li><a href="/">' + self.bold_text_method(ret) + "</a></li> <br>")[0]
            type_ret_list.append(one_type)

        return method_ret_list

def get_htmlfile(url_info):
    #  https://pkg.go.dev/crypto@go1.20
    # https://pkg.go.dev/github.com/gin-gonic/gin
    url_list = url_info.split("/")
    if "github.com" in url_info:
        ret_str = url_list[url_list.index("github.com" )+1]
    else:
        ret_str = url_list[url_list.index("pkg.go.dev" )+1]

    return ret_str








if __name__ =="__main__":
    pkg_hp_html = "pkg_go_hp"
    url = "https://pkg.go.dev/unsafe@go1.20"
    src_file = "trans_file"
    htmlfile = get_htmlfile(url) + ".html"
    htmlfilename = get_htmlfile(url)
    header = '<!DOCTYPE html>  ' \
 '\n  <html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system">  ' \
' \n  <head>  ' \
'   \n  <meta charset="utf-8">  ' \
 '\n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/font-awesome.css" />  ' \
' \n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/style.css" />  ' \
'\n    <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c1.css" />  ' \
' \n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c2.css" />  ' \
' \n  <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c3.css" />  ' \
 '\n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/default.css" />  ' \
 '\n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/igor.css" />  ' \
' \n  <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/material.css" />  ' \
' \n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/native.css" />  ' \
' \n   <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/monokai.css" />  ' \
' \n   <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://svgsilh.com/svg/33581.svg">  ' \
' \n     <link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css" media="all" />  ' \
' \n   </head>  ' \
' \n   <body class="logged-in env-production page-responsive page-blob" style="word-wrap: break-word;">  ' \
'  \n    <div class="position-relative js-header-wrapper ">  ' \
'    \n               <header class="Header js-details-container Details px-3 px-md-4 px-lg-5 flex-wrap flex-md-nowrap" role="banner">  ' \
'\n  <div class="Header-item mt-n1 mb-n1  d-none d-md-flex">  ' \
'  \n     <a class="Header-link" href="/pkg" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">  ' \
'  \n  <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark- v-align-middle">  ' \
'  \n    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-2.82.64-.18 12.44 1.1.16 1.92.08 2.12.5115.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>  ' \
'\n  </svg>  ' \
' \n </a>  ' \
' \n    </div>  ' \
  '\n        <nav id="global-nav" class="d-flex flex-column flex-md-row flex-self-stretch flex-md-self-auto" aria-label="Global">  ' \
  '\n    <a class="Header-link py-md-3 d-block d-md-none py-2 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">Dashboard</a>  ' \
 '\n &nbsp;&nbsp;&nbsp;  ' \
  '  \n     <form class="js-site-search-form" role="search" aria-label="Site" data-unscoped-search-url="https://pkg.go.dev/search" action="https://pkg.go.dev/search" accept-charset="UTF-8" method="get">  ' \
  ' \n      <label class="form-control header-search-wrapper input-sm p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">  ' \
  ' \n         <input type="text"  ' \
  ' \n           class=" js-site-search-focus header-search-input jump-to-field js-jump-to-field"  ' \
  ' \n           data-hotkey=s,/  ' \
 '\n           name="q"  ' \
  '   \n         data-test-selector="nav-search-input"  ' \
  ' \n            value=""  ' \
  ' \n          placeholder="Search "  ' \
  '  \n         data-unscoped-placeholder="Search"  ' \
  '  \n         data-scoped-placeholder="Search "  ' \
  '\n          autocapitalize="off"  ' \
  ' \n          role="combobox"  ' \
  ' \n          aria-haspopup="listbox"  ' \
  '\n          aria-expanded="false"  ' \
  '  \n         aria-autocomplete="list"  ' \
  '  \n         aria-controls="jump-to-results"  ' \
  '\n          aria-label="Search"  ' \
  '  \n         spellcheck="false"  ' \
  '  \n         autocomplete="off"  ' \
  ' \n        >  ' \
  ' \n      </label></form>  ' \
 '\n &nbsp;&nbsp;&nbsp;  ' \
 ' \n  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' \
 ' \n  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' \
 ' \n  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' \
 '\n   <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' \
 '\n   <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' \
 ' \n  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' \
 ' \n   <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' \
 ' \n   <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade"   href="/pkg">&#128293;</a>  ' '\n  </div>  ' \
 ' \n <div class="page main">  ' \
 '  \n   <div class="horizon">  ' \
'\n  <div class="col middle-column-home">  ' \
             '  <section class="Documentation-index">                   \n      <h3 id="pkg-index" class="Documentation-indexHeader"> <a href="#pkg-index"></a></h3>' \
             '         \n<div>                    \n           <br> \n                    <br> ' + '   \n                     <a class="previous"  style="text-align: left;" href="/{0}.html">&nbsp&nbspBack</a>'.format(pkg_hp_html) + \
                          '    \n                   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '     \n                 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '      \n               &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '       \n             &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '        \n           &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '        \n         <a class="next"   style="text-align: right;" href="/{1}">{0}</a></div><br>'.format(htmlfilename,htmlfile) + \
             '\n <br>  \n                   <ul class="Documentation-indexList"> '

    footer = "</ul> \n                     </section> \n         </div> \n </div> \n </body> \n    </html>"

    output_text(src_file,url)
    independent_func_list = []
    type_list = []
    method_list = []
    datafile = src_file

    abc = Output_Golang_FITM()
    abc.exec()

