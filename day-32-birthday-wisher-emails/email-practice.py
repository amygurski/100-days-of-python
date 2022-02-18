import smtplib

my_email = "example@gmail.com"
password = "abcd1234"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="to_person@gmail.com", 
        msg="Subject:Hello\n\nThis is the body of my email."
    )
