from flask import Flask,request,redirect,url_for,session,Response

app=Flask(__name__)
app.secret_key='supersecret'

#hoem login page
@app.route('/',methods=['GET','POST'])

def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')

        if username=='sanskar163@gmail.com' and password=='123':
            session['user']=username #store in session
            return redirect(url_for('welcome'))
        else:
            return Response("in valid credentials.try again",mimetype='text/plain')
        #by defalut sends html so we use mimetype=text/plain

    return '''<h2>login in</h2>
    <form method='POST'>
    Username:<input type='text' name='username'><br>
    Password:<input type='text' name='password'><br>
    <input type='submit' value='Login'>
    </form>



     '''
#welcome page after login
@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f'''
        <h2>welcome,{session['user']}!</h2>
        <a href={url_for('logout')}>logout</a>
        '''

    return  redirect(url_for('login'))

#logout rpute
@app.route('/logout')
def logout():
    session.pop('user',None)
    #session['user]='sanskar'
    return redirect(url_for('login'))


    

@app.route('/about')
def about():
    return "this is about page"

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        return "you send some data"
    else:
        return "you are just viewing webpage"
   


if __name__=="__main__":
    app.run(debug=True)