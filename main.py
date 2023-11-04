from flask import Flask, render_template
import util
app = Flask(__name__)
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'
@app.route('/api/update_basket_a/')
def update_basket_a():
	cursor, connection = util.connect_to_db(username, password, host, port, database)
	try:
		cursor.execute("INSERT INTO basket_a VALUES('Cherry');")
	except Exception as e:
		return str(e)
	util.disconnect_from_db(connection,cursor)
	return render_template('update_basket_a.html')
@app.route('/api/unique')
def unique_fruits():
	cursor, connection = util.connect_to_db(username, password, host, port, database)
	try:
		basket_a_unique = util.run_and_fetch_sql(cursor, "SELECT DISTINCT fruit_a FROM basket_a;")
		basket_b_unique = util.run_and_fetch_sql(cursor, "SELECT DISTINCT fruit_b FROM basket_b;")
	except Exception as e:
		return str(e)
	util.disconnect_from_db(connection, cursor)
	return render_template('unique_fruits.html', basket_a=basket_a_unique, basket_b=basket_b_unique)
if __name__ == '__main__':
	app.debug = True
	ip = '127.0.0.1'
	app.run(host=ip)
