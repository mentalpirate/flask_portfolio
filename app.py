from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
# loads enviroment variables
load_dotenv()

client = MongoClient(getenv('MONGO_URI'))
# database = client[getenv('MONGO_DATABASE')]
# collection = database[getenv('MONGO_COLLECTION')]
db = client['tododatabase']
collection = db['todo']


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.get("/submittodoitem")
def gettodo():
    ## fetch data from mongodb and return to user
    todo = collection.find()
    return render_template("todo.html",todos=todo)


@app.post("/submittodoitem")
def posttodo():
    ## post data to mongodb
    form_data = request.form.to_dict()
    collection.insert_one(form_data)
    return redirect(url_for('gettodo'))

@app.route("/help")
def help():
    return render_template("help.html")


@app.post("/data")
def data():
    if request.method == "POST":
        return f"Data has been successfully submitted. please go ahead {request.form['data']}"



if __name__ == "__main__":
    app.run(debug=True)