import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# ================= CONFIG =================
sender_email = "rkahmad987@gmail.com"
receiver_emails = ["rkahmad987@gmail.com"]   # multiple emails possible
password = "saojuhocprvpwoxx"

IP_FILE = "ip.txt"
LOG_FILE = "log.txt"

# ================= FUNCTIONS =================

def get_current_ip():
    try:
        res = requests.get("https://api.ipify.org?format=json", timeout=5)
        res.raise_for_status()
        return res.json()["ip"]
    except Exception as e:
        print("API Error:", e)
        return None


def read_old_ip():
    try:
        with open(IP_FILE, "r") as f:
            return f.read()
    except:
        return ""


def save_ip(ip):
    with open(IP_FILE, "w") as f:
        f.write(ip)


def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")


def send_email(message):
    msg = MIMEText(message)
    msg['Subject'] = "🚨 IP Alert"
    msg['From'] = sender_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)

            for email in receiver_emails:
                server.sendmail(sender_email, email, msg.as_string())

        print("Email sent successfully")
    except Exception as e:
        print("Email Error:", e)


# ================= MAIN =================

current_ip = get_current_ip()

if current_ip:
    old_ip = read_old_ip()

    if current_ip != old_ip:
        message = f"IP changed!\nNew IP: {current_ip}"

        send_email(message)
        save_ip(current_ip)
        log_event(f"IP changed to {current_ip}")

    else:
        print("No change in IP")
        log_event("No change in IP")

else:
    log_event("Failed to fetch IP")