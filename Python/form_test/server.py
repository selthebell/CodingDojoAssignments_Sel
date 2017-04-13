from flask import Flask, render_template,request,redirect
app = Flask(__name__)
#our index route will handle rendering our form
@app.route('/')
def index():
    return render_template('index.html')
#handling form submission
@app.route('/users',methods=['POST'])
def create_user():
    print "get post info"
    name=request.form['name']
    location=request.form['location']
    lang=request.form['lang']
    comments=request.form['comments']
    #redirects to '/' route
    #redirect('/')
    return render_template('result.html',name=name,location=location,lang=lang,comments=comments)
#redirect on goback
@app.route('/goback')
def test():
    return redirect('/')
    #return render_template('index.html')

app.run(debug=True)#run our server
