import os
import smtplib
import datetime as dt
import pandas
import random
from pathlib import Path
from dotenv import load_dotenv, dotenv_values

load_dotenv()

mail=os.getenv("MAIL")
password=os.getenv("PASSWORD")

data = pandas.read_csv('birthdays.csv')
new_dic = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

today=dt.datetime.now()

if (today.month,today.day) in new_dic:

    person=new_dic[(today.month,today.day)]

    filepath=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as letter:
        cont=letter.read()
        cont = cont.replace("[NAME]",person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()  # makes connection secure
        conn.login(user=mail, password=password)
        conn.sendmail(from_addr=mail,
                      to_addrs=person["email"],
                      msg=f"Subject:Happy Birthday\n\n {cont}")  # hlo is sub and master is content


