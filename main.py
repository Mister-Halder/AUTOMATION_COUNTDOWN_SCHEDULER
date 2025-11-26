# step-1 install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time
#step-2 twilio credentials
account_sid = 'ACeacca8c93d4863b776d8c3231c392700'
auth_token = 'f00137d23f9a77bddfa153337f2d5c6d'
client = Client(account_sid, auth_token)
#step-3 define send message function
def send_whatsapp_message(recipient_number, message_body) :
    try : 
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message Sent Successfully! Message SID{message.sid}')
    except Exception as e :
        print('An Error Occurred')
#step-4 countdown timer
def countdown_timer(delay_seconds):
    import sys
    while delay_seconds > 0:
        mins, secs = divmod(int(delay_seconds), 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        print(f"\rTime Remaining To Send: {timeformat}", end="")
        sys.stdout.flush()
        time.sleep(1)
        delay_seconds -= 1
    print("\nTime Reached! Sending Message...")        
#step-5 user input
name = input('Enter The Recipient Name = ')
recipient_number = input('Enter The Recipient Whatsapp Number With Country Code (e.g, +91) : ')
message_body = input(f'Enter The Message You Want To Send To {name} : ')
#step-6 parse date/time and calculate delay
date_str = input('Enter The Date To Send The Message (YYYY-MM-DD) : ')
time_str = input('Enter The Time To Send The Message (HH:MM in 24 hour format) : ')
#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
#calculate delay
time_difference = (schedule_datetime - current_datetime)
delay_seconds = time_difference.total_seconds()
if delay_seconds <= 0 :
    print('The Specified Time Is In The Past. Please Enter A Future Date And Time : ')
else :
    print(f'Message Scheduled To Be Sent To {name} at {schedule_datetime}.')
    #wait until the scheduled time
    countdown_timer(delay_seconds) #1000
    #send the message
    send_whatsapp_message(recipient_number, message_body)
    