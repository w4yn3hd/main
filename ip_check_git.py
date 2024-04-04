# by W4yn3HD - 19.08.2023
import subprocess
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Funktion 
def check_ip_reachability(ip_address):
    try:
        # Pingen, ACHTUNG! Bei Windows -n, bei Linux -c
        output = subprocess.check_output(["ping", "-n", "3", ip_address])
        return True
    except subprocess.CalledProcessError:
        return False

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # SMTP Server und Port angeben
    smtp_server = 'smtp_Server.com'
    port = 123

    # Verbindung zum SMTP-Server herstellen
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, sender_password)

    # create Mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server.send_message(msg)

    #Verbindung trennen
    server.quit()
     

def notify_reachability(ip_address, sender_email, sender_password, receiver_email):
    if check_ip_reachability(ip_address):
        subject = "IP-Adresse ist erreichbar"
        message = "Die IP-Adresse {ip_address} ist erreichbar."
        send_email(sender_email, sender_password, receiver_email, subject, message)
    else:
        subject = "IP-Adresse ist nicht erreichbar"
        message = f"Die IP-Adresse {ip_address} ist nicht erreichbar."
        send_email(sender_email, sender_password, receiver_email, subject, message)
    
    
if __name__ == "__main__":
    ip_address = "DestinationIP" 
    sender_email = 'SenderEmail'
    sender_password = 'Password'
    receiver_email = 'DestinationEmail'

    notify_reachability(ip_address, sender_email, sender_password, receiver_email)


#Debug Session

# Terminal Ausgabe
def print():
    if check_ip_reachability(ip_address):
       print("ip_address ist erreichbar") 
    else:
     print('ip_address ist nicht erreichbar') 