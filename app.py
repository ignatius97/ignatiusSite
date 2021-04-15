import smtplib, ssl
from flask import Flask, render_template, url_for, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
       name = request.form.get("name")
       email = request.form.get("email")
       subject = request.form.get("subject")
       msg = request.form.get("message")

       port = 465

       sender = 'ignatius.aturinda@gmail.com'
       password = 'Iluvdagal2u'

       recieve = sender

       message = """\
       
       Message is from {0} @ {1}

       {2} 

       Thank You
       """.format(name,email,msg)


       msg = MIMEMultipart()
       msg['From'] = sender
       msg['To'] = recieve
       msg['Subject'] = subject
       text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

       part1 = MIMEText(message, 'plain')

       msg.attach(part1)

       context = ssl.create_default_context()

       print("Starting to send")
       with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
           server.login(sender, password)
           server.sendmail(sender, recieve, msg.as_string())

       print("sent email!")

       return 'Form posted.'
    Skills=["Reactjs","Nodejs","Html","CSS","Python Flash","Php","JavaScript"]
    return render_template('index.html',Skills=Skills)



if __name__ == "__main__":
    app.run(debug=True)