from flask import render_template ,send_file,request,make_response
from app import app
import requests
import json
import sys
from six.moves import urllib
#app = Flask(__name__)

# TASK 1
@app.route('/')
def task1():
    return 'This is Erik'
# TASK 2
@app.route('/users')
def task2a():
    uri = 'https://jsonplaceholder.typicode.com/users'
    uri_data = urllib.request.urlopen(uri)
    user = json.loads(uri_data.read().decode())
    return render_template('user.html',user=user)

@app.route('/posts')
def task2b():
    uri = 'https://jsonplaceholder.typicode.com/posts'
    uri_data = urllib.request.urlopen(uri)
    post = json.loads(uri_data.read().decode())
    return render_template('post.html',post=post)

@app.route('/count')    
def task2c():
    uri_auth = 'https://jsonplaceholder.typicode.com/users'
    uri_post = 'https://jsonplaceholder.typicode.com/posts' 
    uri1 = urllib.request.urlopen(uri_auth)
    auth_data = json.loads(uri1.read().decode())

    uri2 = urllib.request.urlopen(uri_post)
    post_data = json.loads(uri2.read().decode())

    tot = []
    
    
    for i in auth_data:
        totp = 0
        for j in post_data:
            if j["userId"] == i["id"]:
                totp += 1
        tot.append(totp)    

    respstr = ""
    for i in auth_data:
        respstr += "Author: {}".format(i["name"])
        respstr += "</br>"
            
    respstr += "Total posts in order of the user"

    for i in range(0,10):
        respstr += "&nbsp"*5
        respstr += "</br>"
        respstr += "Total Posts: {}".format(tot[i])        
    return respstr

# TASK 3
@app.route('/setcookie')
def cook():
    return render_template('cook.html')

@app.route('/set',methods = ['POST','GET'])
def setcook():
    if request.method == 'POST':
        user_details1=request.form['Name']
        user_details2=request.form['Age']
        

    resp=make_response(render_template('read_cookie.html'))
    resp.set_cookie('Name',user_details1)
    resp.set_cookie('Age',user_details2)
   
    return resp 

# TASK 4
@app.route('/getcookie')
def getcook():
    name = request.cookies.get('Name')
    age = request.cookies.get('Age')
    #print name
    return name+' is in '+age+'s'           

# TASK 5
@app.route('/robots')
def error():
    file = 'error.txt'
    return send_file(file,mimetype='text/plain')

# TASK 6
@app.route('/image')
def image():
    filename = 'download.jpg'
    return send_file(filename,mimetype='image/jpg')

# TASK 7
@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/log',methods = ['POST','GET'])
def log():
    if  request.method == 'POST':
        message = request.form['Anything']
    ffile = open('store.log','w')
    ffile.write(message)
    print(message, sys.stdout)
    
    ffile.close()
    
    return 'Your message have been recorded'

    
#if __name__=="__main__":
#    app.run(debug=True)


