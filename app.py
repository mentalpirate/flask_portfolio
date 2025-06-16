from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

# Normal Route 
@app.route("/help")
def help():
    return render_template("help.html")

# Http method
@app.post("/data")
def data():
    if request.method == "POST":
        return f"Data has been successfully submitted. please go ahead {request.form['data']}"

if __name__ == "__main__":
    app.run(debug=True)