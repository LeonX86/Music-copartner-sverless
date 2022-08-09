# coding=utf-8
"""
Mailer module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import smtplib
from notify.compat import Header
from notify.compat import MIMEText
from notify.compat import formatdate

def create_message(from_addr, to_addr, subject, body, encoding=None):
    """
    Create message object for sending email

    Parameters
    ----------
    from_addr : string
        An email address used for 'From' attribute
    to_addr : string
        An email address used for 'To' attribute
    subject : string
        An email subject string
    body : string
        An email body string
    encoding : string
        An email encoding string (Default: utf8)

    Returns
    -------
    object
        An instance of email.mime.text.MIMEText
    """
    if encoding == "None":
        encoding = None
    if not encoding:
        encoding = 'utf-8'
    msg = MIMEText(body.encode(encoding), 'plain', encoding)
    msg['Subject'] = Header(subject.encode(encoding), encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send_email(msg, host='localhost', port=25,
         username=None, password=None):
    """
    Send an email (via TLS when username and password are specified)

    Parameters
    ----------
    msg : object
        An instance of MIMEText. Create this with :func:`create_message`
        function.
    host : string
        A mail user agent host name (Default: localhost)
    port : int
        A mail user agent port number (Default: 25)
    username : string
        A username string used to login MUA via TLS authentication
    password : string
        A password string used to login MUA via TLS authentication
    debug : boolean
        True for displaying debug messages
    """
    s = smtplib.SMTP(host, port)
    if username and password:
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user, passwd)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.close()
