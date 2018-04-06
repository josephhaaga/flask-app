from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': "Joe"}
	posts = [
		{
			'author':{'username':"tim"},
			'body': "Lorem ipsum dolor sit amet"
		},{
			'author':{'username':"lil pump"},
			'body': "ooou"
		}
	]
	return render_template('index.html', title="Home", user=user, posts=posts)
