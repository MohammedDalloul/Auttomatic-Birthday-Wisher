import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = input("Enter Your email : ")
MY_PASSWORD = input("Enter Your Email's Applications Password : ")

birthdates_file = pandas.read_csv("birthdays.csv")
birthdates_dicts_list = birthdates_file.to_dict(orient="records")

now = dt.datetime.now()

for dict in birthdates_dicts_list:
    if now.month == dict["month"] and now.day == dict["day"]:
        letter_num = random.randint(1, 3)
        person_name = dict["name"]
        with open(f"letter_templates/letter_{letter_num}.txt", "r") as birthdate_letter:
            text = birthdate_letter.read()
            text = text.replace("[NAME]", person_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=dict["email"],
                                msg=f"subject:Happy Birthday\n\n{text}")
















