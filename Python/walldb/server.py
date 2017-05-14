from flask import Flask,request, redirect, session,render_template, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from datetime import datetime

import re

app=Flask(__name__)
app.secret_key="users_secret_key"
mysql=MySQLConnector(app,'walldb')
EMAIL_REGEX=re.compile(r"(^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    #users=mysql.query_db('select * from users')
    return render_template('index.html')

@app.route('/',methods=['POST'])
def users():
    if(request.form['login']=="login"):
        if( (len(request.form['email'])<=0) or (len(request.form['email'])>120) or (not EMAIL_REGEX.match(request.form['email'])) ):
            print "email has to entered as test@tesmail.com"
            flash("Please enter email ")
        if(len(request.form['password'])<=0):
            flash("Please enter password")

        if('_flashes' in session):
            return render_template('index.html')

        email = request.form['email']
        password = request.form['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        query_data = { 'email': email }
        user = mysql.query_db(user_query, query_data) # user will be returned in a list
        #print user[0]['hashpass']
        #print password
        #print email
        if( not len(user)):
            flash('Please check email')
            return render_template('index.html')

        if('id' not in session):
            session['id']=0
            session['name']=''
        if bcrypt.check_password_hash(user[0]['hashpass'], request.form['password']):
            # login user
            print "login succesful"
            session['id']=user[0]['id']
            session['name']=str(user[0]['first_name'])+" "+str(user[0]['last_name'])
            return redirect('/wall')
        else:
            # set flash error message and redirect to login page
            flash("Please check the password")
            return redirect('/')
    else:
        return render_template('registration.html')


@app.route('/users/register',methods=['POST'])
def register():
    if(len(request.form['first_name'])<=2 or len(request.form['last_name'])<=2):
        print "Name is not entered"
        flash("Name has to be atleast 2characters!")
    if( (len(request.form['email'])<=0) or (len(request.form['email'])>120) or (not EMAIL_REGEX.match(request.form['email'])) ):
        print "email has to entered as test@tesmail.com"
        flash("Please enter email ")
    if(len(request.form['password'])<=8):
        flash("Password needs to be 8 characters long")
    if(request.form['password']<>request.form['confirm_pwd']):
        flash("Please confirm password")
    if('_flashes' in session):
        return render_template('registration.html')

    print "inside insert"
    insert_query="insert into users(first_name,last_name,email,hashpass,created_at,updated_at) values(:first_name,:last_name,:email,:hashpass,now(),now())"
    data={
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'email': request.form['email'],
    'hashpass':request.form['password']
    }
    data['hashpass']=bcrypt.generate_password_hash(data['hashpass'])
    mysql.query_db(insert_query,data)
    return render_template('success.html')

@app.route('/users/login')
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if bcrypt.check_password_hash(user[0]['hashpass'], password):
        # login user
        return render_template('success.html')
    else:
        # set flash error message and redirect to login page
        flash("Please check the password")
        return redirect('/')

@app.route('/wall')
def getMessage():
    if('id' not in session):
        flash('Please login')
        return redirect('/')

    # msg_query="select * from messages"
    # messageData=mysql.query_db(msg_query)
    # usr_query="select * from users"
    # userData=mysql.query_db(usr_query)
    #joinQuery='SELECT concat(first_name," ",last_name) as name,message,messages.users_id as users_id,messages.id as message_id,comment FROM messages join users on users.id=users_id left join comments on comments.messages_id=messages.id'
    msgQuery='SELECT concat(first_name," ",last_name) as name, message , messages.users_id as users_id, messages.id as messages_id, messages.created_at as created_at  FROM messages left join users on users.id=messages.users_id order by messages.created_at desc'
    msgData=mysql.query_db(msgQuery)
    commentQuery='SELECT concat(first_name," ",last_name) as name, comment, comments.created_at as created_at, comments.users_id as users_id,messages_id from comments,users where comments.users_id=users.id order by comments.created_at asc'
    commentData=mysql.query_db(commentQuery)
    print "from route wall",msgData
    return render_template('wall.html',messages=msgData,comments=commentData)

@app.route('/wall', methods=['POST'])
def postMessage():
    if('id' not in session):
        flash('Please login')
        return redirect('/')
    if(request.form['message']==""):
        flash('Please enter a message')
        return render_template('wall')
    data={
    "users_id":session['id'],
    "message":request.form['message'],
    }
    insert_query="insert into messages(message,created_at,updated_at,users_id) values(:message,now(),now(),:users_id)"
    mysql.query_db(insert_query,data)
    return redirect('/wall')

@app.route('/wall/comment', methods=['POST'])
def postComment():
    if('id' not in session):
        flash('Please login')
        return redirect('/')
    print "inside post comment"
    #print "comments",str(request.form['comments'])
    # if(request.form['comments'] ==""):
    #     flash('Please enter a comment')
    #     return redirect('/wall')

    mylist=request.form['comment']
    print mylist
    comment_data={
    "users_id" : session['id'],
    "messages_id" :mylist ,
    "message" : request.form['comments'+mylist],
    }
    print "inside post comment"
    insert_query="insert into comments(comment,created_at,updated_at,users_id,messages_id) values(:message,now(),now(),:users_id,:messages_id)"
    mysql.query_db(insert_query,comment_data)
    return redirect('/wall')

@app.route('/delete/<id>')
def delete(id):
    if('id' not in session):
        flash('Please login')
        return redirect('/')

    print "inside delete"
    print "id",int(id)
    delData={
    'message_id':int(id),
    }
    delcommentQry='delete from comments where messages_id=:message_id'
    deleteQuery='delete from messages where id=:message_id'
    mysql.query_db(delcommentQry,delData)
    mysql.query_db(deleteQuery,delData)
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
