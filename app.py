#step-1 install required libraries
from twilio.rest import Client 
from datetime import datetime, timedelta
import time

#step-2 twilio credrntials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

client = Client(account_sid, auth_token)

#step-3 design send message function
def send_whatsapp_message(recepient_number, message_body):
    try:
        message = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recepient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print(f'An error occured : {e}')

#step-4 user inout
name = input('Enter the receipient name = ')
recipient_number = input('Enter the recipient Whatsapp number with country code (e.g, +12)')
message_body = input('Enter the Message {name} : ')

#step-5 parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD) : ')
time_str = input('Enter the time to send message (HH:MM in 24 hour format) : ')

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0:
    print('The specified time is in past. Please enter a future date and time : ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    #wait until the scheduled time
    time.sleep(delay_seconds)#1000

    #send the message
    send_whatsapp_message(recipient_number, message_body)
