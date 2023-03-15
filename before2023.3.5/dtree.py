#! -*- coding:utf-8 -*-


from flask_cors import cross_origin,CORS
from flask import Flask
from flask import render_template, redirect, send_from_directory, request
from pathlib import Path








app = Flask(__name__,static_folder="dytree")
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "dytree"



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import pygal
import shutil
# 因为vue和render_template的模板都是用{{  }}，所以会冲突，将flask的修改为[[  ]]


# 以下代码会影响pygal的加载？ app.jinja_env.variable_start_string = '[['
# 所以得专门把svg作图单独提出来
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'




@app.route("/")
@cross_origin()
def top_homepage():
    return render_template("dytree.html")

@app.route("/goinfo")
@cross_origin()
def goinfo():
    return render_template("golang_info.html")



@app.route('/dytree/<filename>')
@cross_origin()
def onasdfe_type_json(filename):
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ### 路由管理
if __name__ == '__main__':
    app.run(debug=True,port=8888)