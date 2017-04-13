from flask import Flask, render_template,request,redirect,session
app=Flask(__name__)
app.secret_key="the secret key"
@app.route('/')
def index():
    counter=1
    if('counter' in session):
        session['counter']+=counter
    else:
        session['counter']=counter
    return render_template('index.html')

@app.route('/',methods=['POST'])
def counter():
    #session['counter']+=1
    print "ninjas",request.form['ninjas']
    #print request.form['reset']
    #if(request.form['ninjas']):
    val=request.form['counter']
    val = int(val)
    print type(val)
    session['counter']+=val
    print type(session['counter'])
    #else:
    #session['counter']=0;
    return render_template('index.html')

@app.route('/reset')
def reset():
    if('counter' in session):
        session['counter']=0;
    return render_template('index.html')
app.run(debug=True)
