from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
from model import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route("/")
def template ():
	return render_template("template.html")

@app.route("/yogatypes")
def yogatypes():
	return render_template("yogatypes.html")

@app.route("/readingmaterial")
def readingmaterial():
	return render_template("readingmaterial.html")

@app.route("/findlessons")
def findlessons():
	return render_template("findlessons.html")

@app.route("/startpracticing")
def startpracticing():
	return render_template("startpracticing.html")

@app.route("/Q&A",  methods=['GET', 'POST'])
def QandA():
	if request.method == 'GET':
		
		list_q = query_all()

		return render_template('Q&A.html', list_q=list_q)
	else: #request.method == 'post'
		content = request.form['content']
		writer = request.form['writer']

		list_q = query_all()
		
		add_question(content, writer)        
		return render_template('Q&A.html', list_q=list_q)


@app.route("/asking_f")
def asking_f():
	return render_template("asking_f.html")


if __name__ == '__main__':
	app.run(debug=True, threaded=False, port=5020)