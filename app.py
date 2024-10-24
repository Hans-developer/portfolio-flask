from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
app = Flask(__name__)

# Looking to send emails in production? Check out our Email API/SMTP product!
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '0397d4937b85d0'
app.config['MAIL_PASSWORD'] = 'a3e1d9170e9b58'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mail", methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mesage = request.form.get("mesage")

        msg = Message(
            'Hola Hans, tienes un mensaje desde la web porfolio',
            body = f"Nombre {name}\nCorreo: <{email}> \n\nEscribio: {mesage}",
            sender=email,
            recipients=['Dev.Hans.saldias@trap.io']
        )
        mail.send(msg)
        return render_template('send_mail.html')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=False)