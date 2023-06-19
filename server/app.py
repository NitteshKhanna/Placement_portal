from flask import Flask, request
import sqlite3

app=Flask(__name__)
con=sqlite3.connect("db.db")
cur=con.cursor()
cur.execute("CREATE TABLE students (name TEXT, rollno INTEGER, mail_id TEXT, address TEXT, no_of_arrears INTEGER, cgpa REAL, mobile_no TEXT);")
con.close()

@app.route("data",methods=['GET'])
def datag():

    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM students")
    op=cur.fetchall()
    con.close()
    return op

@app.route("data",methods=['POST'])
def datap():
    json=request.form.get()

    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("INSERT INTO students (name, rollno, mail_id, address, no_of_arrears, cgpa, mobile_no) VALUES ('John Doe', 123456, 'johndoe@example.com', '123 Main St, City', 2, 3.5, '123-456-7890');")
    con.commit()
    con.close()
    return

@app.get("/test")
def test():
    return "works"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if(__name__=="__main__"):
    app.run(debug=True)