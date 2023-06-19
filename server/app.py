from flask import Flask, request
import sqlite3

app=Flask(__name__)
con=sqlite3.connect("db.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rollno INTEGER, mail_id TEXT, address TEXT, no_of_arrears INTEGER, cgpa REAL, mobile_no TEXT);")
con.close()

@app.route("/data",methods=['GET'])
def datag():

    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM students")
    op=cur.fetchall()
    con.close()
    return op

@app.route("/data",methods=['POST'])
def datap():

    name=request.form.get("name")
    rollno=request.form.get("rollno")
    mail_id=request.form.get("mail_id")
    add=request.form.get("add")
    arrears=request.form.get("arrears")
    cgpa=request.form.get("cgpa")
    no=request.form.get("no")

    q=(name,rollno,mail_id,add,arrears,cgpa,no)

    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("INSERT INTO students (name, rollno, mail_id, address, no_of_arrears, cgpa, mobile_no) VALUES (?,?,?,?,?,?,?);",q)
    con.commit()
    con.close()
    return

@app.route("/dataj",methods=['POST'])
def dataj():

    json=request.json 
    name=json["name"]
    rollno=json["rollno"]
    mail_id=json["mail_id"]
    add=json["add"]
    arrears=json["arrears"]
    cgpa=json["cgpa"]
    no=json["no"]

    q=(name,rollno,mail_id,add,arrears,cgpa,no)

    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("INSERT INTO students (name, rollno, mail_id, address, no_of_arrears, cgpa, mobile_no) VALUES (?,?,?,?,?,?,?);",q)
    con.commit()
    con.close()
    
    return "Inserted"

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