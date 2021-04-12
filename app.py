from flask import Flask, render_template, url_for, request
from flask.ext.mail import Message, Mail
import smtplib

import sendgrid
import os
from sendgrid.helpers.mail import *



mail = Mail()

app = Flask(__name__)


sg = sendgrid.SendGridAPIClient('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')
myMail = 'ignatius.aturinda@gmail.com'

mail.init_app(app)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":

       name = request.form.get("name")
       email = request.form.get("email")
       subject = request.form.get("subject")
       message = request.form.get("message")
       mail = Mail(myMail, myMail, subject, message)
       response = sg.client.mail.send.post(request_body=mail.get())

       return 'Form posted.'
    Skills=["Reactjs","Nodejs","Html","CSS","Python Flash","Php","JavaScript"]
    return render_template('index.html',Skills=Skills)



if __name__ == "__main__":
    app.run(debug=True)