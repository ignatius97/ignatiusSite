from flask import Flask, render_template, url_for, request
from flask.ext.mail import Message, Mail
import smtplib

mail = Mail()

app = Flask(__name__)


app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'ignatius.aturinda@gmail.com'
app.config["MAIL_PASSWORD"] = 'ILuvdagal2u'

mail.init_app(app)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
       name = request.form.get("name")
       email = request.form.get("email")
       subject = request.form.get("subject")
       message = request.form.get("message")
       msg = Message(subject, sender=email, recipients=['ignatius.aturinda@gmail.com'])
       msg.body = """
             From: %s <%s>
             %s
             """ % (name, email, message)
       mail.send(msg)

       return 'Form posted.'
    Skills=["Reactjs","Nodejs","Html","CSS","Python Flash","Php","JavaScript"]
    return render_template('index.html',Skills=Skills)



if __name__ == "__main__":
    app.run(debug=True)