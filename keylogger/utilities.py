import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config
from .templates import get_template

def response_writer(status: str, code: int, data: dict, message: str) -> dict:
    return {
        "status": status,
        "code": code,
        "data": data,
        "message": message
    }

def check_bad_words(text: str) -> str:

    url = "https://api.apilayer.com/bad_words?censor_character=*"

    payload = text.encode("utf-8")
    headers= {
    "apikey": "QIemzVNzsfiZ1wXX9HxhtE8P8nI1J24k"
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.json())
    return response.json()


def send_email(bad_words_list: list) -> None:
    port = 465  # For SSL

    sender_email = "abhiramjoshivit@gmail.com"
    receiver_email = "abhiramjoshivit@gmail.com"
    password = config("GMAIL_PASSWORD")

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    # text = """
    # Hi,
    # How are you?
    # Real Python has many great tutorials:
    # www.realpython.com"""

    # with open(r"../templates/parental_email.html", "r") as file:
    # with open(r"parental_email.html", "r") as file:
    #     html = file.read()

    # html = data["parental_email"]
    html = get_template(bad_words_list)

    # part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # The email client will try to render the last part first
    # message.attach(part1)
    message.attach(part2)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        # content = "Hemlom from keylogger\n\n"

        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        

if __name__ == "__main__":
    # ecc = ECC(p=23, a=1, b=1)
    # print(ecc.check_point(x_value=1, y_value=2))
    # check_bad_words("sex and the city porn")
    send_email("asdk")
    # for i in range(10000):
    #     pass
    # pass