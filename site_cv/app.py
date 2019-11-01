from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os 



app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['TESTING'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'oscartematio@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASS')
app.config['MAIL_USERNAME'] = 'oscartematio@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route('/' ,  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        phone_number = request.form['num']
        subject = request.form['subject']
        message = request.form['message']
        g_message = message + "\n" + "Nom: " + name + " " +  lname  + "\n" + \
            "Email: " + email + "\n" + "Telephone: " + phone_number
        Answer =  "Hello "+name+"," + "\n" + "Your message has been sent to me, I recontact you as soon as I have read"+"\n"+"Best Regards"+"\n"+"Oscar Tematio"
        msg = Message(subject, recipients=[
                      'omtematio@gmail.com'], body=g_message)
        mail_answer=Message("----DO not Reply----", recipients=[email],body=Answer)
        
        
        mail.send(msg)
        mail.send(mail_answer)

        return redirect(url_for('home'))
    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

