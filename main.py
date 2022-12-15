from flask import Flask, request, render_template, jsonify, redirect, url_for
import os
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/
@app.route('/upload',methods=['POST','GET'])
def upload_kanryou():
    # if request.method=='GET':
    #     return render_template('upload_page.html')
    if request.method=='POST':
        # file=request.files=['test']
        # file.save(os.path.join('./static'),'a')
        return render_template("upload_page.html",message="アップロード完了")

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("upload_page.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
