from flask import Flask,render_template,request
'''
it creates an instance of the flask class which will be our WSGI
'''
###WSGI application
app=Flask(__name__)

@app.route("/") #/ means home page
def welcome():
    return "<html><h1>welcome to flask course</h1><html>"

@app.route("/index",)
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}'
    return render_template('form.html')


if __name__=="__main__":  #entry point
    app.run(debug=True)
