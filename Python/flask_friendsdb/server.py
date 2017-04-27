from flask import Flask, request, redirect, request, session,render_template, flash
from mysqlconnection import MySQLConnector

app=Flask(__name__)
mysql=MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html',all_friends=friends)

@app.route('/',methods=['POST'])
def insert():
    if(len(request.form['first_name'])<=0 or len(request.form['last_name'])):
        print "Name is not entered"
        flash("Name cannot be empty!")
        return redirect('/')
    if(len(request.form['email'])<=0 or len(request.form['email'])>120 ):
        print "email is not entered"
        flash("Please enter email ")
        return redirect('/')

    print "inside insert"
    insert_query="insert into friends(first_name,last_name,occupation,email,created_at,updated_at) values(:first_name,:last_name,:occupation,:email,now(),now())"
    data={
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'occupation': request.form['occupation'],
    'email': request.form['email']
    }
    mysql.query_db(insert_query,data)

    return redirect('/')

@app.route('/friends/<id>/<flag>')
def friends(id,flag):
    select_query="select * from friends where id = :user_id"
    data={"user_id" : id}
    results=mysql.query_db(select_query,data)
    return render_template('friends.html',all_friends=results[0],flag=flag)

@app.route('/friends/update/<id>',methods=['POST'])
def update_friends(id):
    print "inside update"
    update_query="update friends SET first_name=:first_name,last_name=:last_name,occupation=:occupation,email=:email where id=:user_id"
    data={
    'user_id' : id,
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'occupation': request.form['occupation'],
    'email' : request.form['email']
    }
    print data
    flag="show"
    mysql.query_db(update_query,data)
    print "query execute"
    return redirect('friends/'+id+'/'+flag)

@app.route('/friends/delete/<id>')
def delete(id):
    print "inside delete"
    query = "DELETE FROM friends WHERE id = :user_id"
    data = {'user_id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
