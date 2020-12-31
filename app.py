from flask import Flask, render_template, redirect, url_for, request, session
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return "testing"

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
