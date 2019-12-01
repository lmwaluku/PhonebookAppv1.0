'''

Developer: Lloyd Mwaluku
Application: Phone Book
Year: December 2019

'''

from flask import Flask,render_template,g,redirect,request,session,url_for,json
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")
	
@app.route('/register', methods=['POST'])
def register():
		name_ = request.form['name']
		email_ = request.form['email']
		phone_ = request.form['phone']	

		g.db = sqlite3.connect("C:/Users/Lloyd/Anaconda3/PhonebookAppv1.0/App/database.db")
		g.db.execute("INSERT INTO details (name,email,phone) VALUES (?,?,?)",(name_,email_,phone_))
		g.db.commit()
		return render_template('success.html')
		g.db.close()
		
@app.route('/reports')
def reports():
		g.db = sqlite3.connect("C:/Users/Lloyd/Anaconda3/PhonebookAppv1.0/App/database.db")
		data = g.db.execute("SELECT * FROM details").fetchall()
		return render_template('reports.html', data=data)
		g.db.close()

@app.route("/search")
def search():
    return render_template("search.html")

@app.route('/results', methods=['POST'])
def results():
		if request.method == "POST":
			search_item = request.form['search_item']
			g.db = sqlite3.connect("C:/Users/Lloyd/Anaconda3/PhonebookAppv1.0/App/database.db")
			data = g.db.execute('SELECT * FROM details where name = ?', [search_item]).fetchall()
			if not data:
				return render_template('noresults.html')
				g.db.close()
			else:
				return render_template('results.html', data=data)
				g.db.close()
		
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500
	
if __name__ == '__main__':
	app.run(debug=False)