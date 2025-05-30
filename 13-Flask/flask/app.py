from flask import Flask
'''
it creates an instance of the flask class which will be our WSGI
'''
###WSGI application
app=Flask(__name__)

@app.route("/") #/ means home page
def welcome():
    return "welcome to best flask course.This should be an amazing course"

@app.route("/index")
def index():
    return "welcome to index page"

if __name__=="__main__":  #entry point
    app.run(debug=True)
