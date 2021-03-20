from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def index():
    Skills=["Reactjs","Nodejs","Html","CSS","Python Flash","Php","JavaScript"]
    return render_template('index.html',Skills=Skills)

if __name__ == "__main__":
    app.run(debug=True)