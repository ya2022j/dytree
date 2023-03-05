


import openpyxl

from pandas.core.frame import DataFrame
import pandas as pd
import xlrd
import os

import csv
import shutil
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
def writeinto_detail(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        csv_out = csv.writer(f, delimiter=",")
        csv_out.writerow(data)


def output_list(list_item):
    for item in list_item:
        writeinto_detail(tsvfilename,[item])

    writeinto_detail(tsvfilename,["--"*20 + "--"*20])

def read_excel(excelfile):

    file_dt = pd.read_excel(excelfile)
    for item in file_dt.values.tolist():
        output_list(item)



def read_txtfile_to_html(htmlname,tsvfilename):


    header_html_str = '<!DOCTYPE html> \n <html>    <head>\n    <meta charset="utf-8">\n     <title>DYtree</title>\n     <link href="//cdn-images.mailchimp.com/embedcode/slim-081711.css" rel="stylesheet" type="text/css">  \n     <style type="text/css">\n       #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; }\n       /* Add your own MailChimp form style overrides in your site stylesheet or in this style block.\n      https://unicode-table.com/en/1F5C1/\n \n       folder css\n         We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */\n     </style>\n   <link rel="stylesheet" type="text/css" href="https://cdn.muzzammil.xyz/OctoCSS/">\n \n     <link rel="stylesheet" href="../static/build.css">\n     <link rel="stylesheet" href="../static/index.css">\n \n    <link rel="stylesheet" href="../static/theme_dark.css">\n \n    <link rel="stylesheet" href="../static/monokai.css">\n <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/font-awesome.css" />    <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/style.css" />\n <style> \n       .previous{\n          float:left;\n      }\n     .next {\n          float:right;\n      }\n  </style>\n    <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c1.css" />\n  <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c2.css" />\n      <link crossorigin="anonymous" media="all" rel="stylesheet" href="../static/c3.css" />\n     <link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css" media="all" />\n  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://svgsilh.com/svg/33581.svg">\n \n   </head>\n   <body>\n 	<div class="main" id="main">\n <div>\n \n   <center>\n \n     <h2> &#129303;\n   Directory "Fork me on GitHub"\n \n &#129378;\n \n     </h2><br><br><br>\n    </center>\n </div>\n <a href="https://github.com/DYtree" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="' +'  fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>\n	</div>\n        <!--End mc_embed_signup-->\n     </div>\n \n     <div id="main">\n \n \n \n \n       <div id="example">\n         <div id="editme"></div>\n         <div id="d3view"></div>\n      </div>\n \n         <div>\n \n   <center>\n     <br><br><br>\n \n     </h2>\n    '   +'<h2>&#129424;\n \n     ------------------------------- &#9986;\n -------------------------------    &#127844;\n <br>  "http://domain/dytree/filename"\n  </h2>\n       <br><br><br>\n             <div class="col middle-column-home">\n <center>\n '
    writeinto_htmlfile(htmlname, header_html_str)
    css_template_str = "<style>    #dir1    {background-color:#54aeff;}#dir2{color:#cf222e;}#dir3{color:#000000;}#dir4{color:#0969da;}</style>"
    writeinto_htmlfile(htmlname, css_template_str)
    writeinto_htmlfile(htmlname, "<h4 id='dir1'>{0}</h4>".format(title_info))

    list_ret = readDatafile(tsvfilename)
    for item in list_ret:
        writeinto_htmlfile(htmlname, "<h4 id='dir3'>{0}</h4>".format(item))
    footer_html_str = '</center> \n </div>\n    </div>\n    <script src="../static/d3.v3.min.js"></script>\n    <script src="../static/demo-bundle.js"></script>\n    <script src="../static/marked.js"></script>\n    <script src="../static/demo-data.js"></script>  \n    <script src="../static/flare-data.js"></script>\n    <script src="../static/setup.js"></script>\n\n<circle><a href="http://google.com"></a></circle>\n\n    <script>\n  '+"  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){ \n    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new \n\n    Date();a=s.createElement(o),\n   "+" m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n\n\n    ga('create', 'UA-7002862-5', 'jaredly.github.io');\n    ga('send', 'pageview');\n    </script>\n\n  \n    <br>\n</html>"


    writeinto_htmlfile(htmlname, footer_html_str)




if __name__ == "__main__":
    excelfile = "d.xlsx"
    tsvfilename = "dd.tsv"
    read_excel(excelfile)


    title_info = "Mercari---Engineer Vocabulary List"
    HTML_FILENAME  ="ss.html"

    templates_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(),"..")),"templates")
    dytree_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(),"..")),"dytree")

    read_txtfile_to_html(HTML_FILENAME,tsvfilename)

    os.system("move {0} {1}".format(HTML_FILENAME,"templates"))
    os.system("move {0} {1}".format(tsvfilename,"dytree"))




