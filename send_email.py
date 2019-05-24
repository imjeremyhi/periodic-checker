import json
import smtplib

def get_credentials():
    with open('credentials.json') as f:
        credentials = json.load(f)

    (gmail_user, gmail_password), = credentials.items()

    return (gmail_user, gmail_password)

def send_email_inner(gmail_user, gmail_password, email_subject, email_body):
    email_text = """
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (gmail_user, ", ".join([gmail_user]), email_subject, email_body)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, [gmail_user], email_text)
        server.close()

        print('Email sent')
    except:  
        print('Email could NOT be successfully sent')

def send_email(email_subject, email_body):
    try:
        gmail_user, gmail_password = get_credentials()
    except:
        print('Credentials file either does not exist or is not stored in the correct format. Please refer to the README')
    
    send_email_inner(gmail_user, gmail_password, email_subject, email_body)