from email.mime.text import MIMEText
msg = MIMEText("Hello there")
msg["subject"] = "A text message"
msg["from"] = "John Mueller <John@JohnMuellerBooks.com"
msg["to"] = "John Mueller <John@JohnMuellerBooks.com"
print(msg.as_string())