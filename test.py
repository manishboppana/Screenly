from flask import Flask,render_template
app = Flask(__name__)
@app.route('/abc')
def man():
	return render_template('hello.html')
app.run()