#! -*- coding:utf-8 -*-
import os

from flask_cors import cross_origin,CORS

from flask import render_template, redirect, flash,url_for, request,Flask,send_from_directory
from pathlib import Path
from werkzeug.utils import secure_filename




from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField
from wtforms.validators import DataRequired, Length,ValidationError

from datetime import datetime
from flask import flash, redirect, url_for, render_template
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "sss"
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False
UPLOAD_FOLDER = './templates'



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.jinja_env.trim_blocks = True
app.config["jinja_env.trim_blocks"] = True
app.config["jinja_env.lstrip_blocks"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/notebook"
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


ALLOWED_EXTENSIONS = set(['html'])



def is_pw(msg=None):
    if msg is None:
        msg = "ちゃんと考えてみてくださいね"
    def _is_pw(form,field):
        if field.data !=2007:
            raise ValidationError(msg)
    return _is_pw


class HelloForm(FlaskForm):
    name = StringField('タッグ', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('メッセージ', validators=[DataRequired(), Length(1, 200)])
    pw = IntegerField("暗号は何だっけ？",validators=[is_pw()])
    submit = SubmitField()



# model
class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    def __repr__(self):
        return '<Tag %r>' % self.tag






# error
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('errors/404.html'), 404
#
# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('errors/500.html'), 500


# views
@app.route('/notebook', methods=['GET', 'POST'])
def nb_index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('最高です！')
        return redirect(url_for('nb_index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('nb_index.html', form=form, messages=messages)



# 因为vue和render_template的模板都是用{{  }}，所以会冲突，将flask的修改为[[  ]]


# 以下代码会影响pygal的加载？ app.jinja_env.variable_start_string = '[['
# 所以得专门把svg作图单独提出来

# yao要用jinja2以下配置不能有
# app.jinja_env.variable_start_string = '{['
# app.jinja_env.variable_end_string = ']}'
#





@app.route("/")
@cross_origin()
def top_homepage():
    return render_template("dytree.html")




@app.route("/reboot", methods=['GET', 'POST'])
@cross_origin()
def reboot():
    os.system("reboot")
    return ""




def allwed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# ファイルを受け取る方法の指定
@app.route('/upload', methods=['GET', 'POST'])
def uploads_file():
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            flash('failed')
            return redirect(request.url)
        # データの取り出し
        file = request.files['file']
        # ファイル名がなかった時の処理
        if file.filename == '':
            flash('failed')
            return redirect(request.url)
        # ファイルのチェック
        if file and allwed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            # ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # アップロード後のページに転送
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>
                Upload file 
            </title>
        </head>
        <body>
            <h1>
                Upload file 
            </h1>
            <form method = post enctype = multipart/form-data>
            <p><input type=file name = file>
            <input type = submit value = Upload>
            </form>
        </body>
'''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)




# ### 路由管理
if __name__ == '__main__':
    app.run(debug=True,port=8888)