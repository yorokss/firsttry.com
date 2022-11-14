import smtplib

import psutil

sendmail ='yorokss1@gmail.com'
recever_mail="yorokss1@gmail.com"
def get_batterystatus():
    battery_data = psutil.sensors_battery()
    print('Battery power left: {}%'.format(battery_data.percent))
    if battery_data.power_plugged:
        print(" power is plugged ")
    else:
        print("connect power plug")

def send():
    port = 587
    smtp_server_domain_name = "smtp.gmail.com"
    sender_mail = "yorokss@gmail.com"
    password = "cqesnxoyccoexlyr"
    session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_mail, password)  # login with mail_id and password
    text = " This is sample message "
    session.sendmail(sender_mail, recever_mail, text)
    session.quit()
    print('Mail Sent')
    """server = smtplib.SMTP_SSL('smtp.gmail,com', 587, context=ssl_context)
    server.login('yorokss@gmaill.com','mptrektzjkeelrvf')
    server.sendmail('yorokss@gmail.com', 'yorokss1@gmail.com',f"subject:{subject}")
    message = ('plugin your laptop')
    server = (,'587')
    smtp_server.starttls()
    smtp_server.login('yorokss@gmaill.com','mptrektzjkeelrvf')
    message = ('plugin your laptop')

    smtp_server.quit()"""
get_batterystatus()
send()



"""
if __name__ == '__main__':
    battery_data = psutil.sensors_battery()

    print('Battery power left: {}%'.format(battery_data.percent))

    if battery_data.power_plugged:
        print('Power is connected')
    else:
        print('Power is not connected')
        print('Time left on battery: {}'.format(datetime.timedelta(seconds=battery_data.secsleft)))
"""