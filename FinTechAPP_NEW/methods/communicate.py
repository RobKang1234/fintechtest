import os
from twilio.rest import Client
def send_whatsapp(msg: str, accountSid, token, from_num, to_num):
    account_sid = accountSid
    auth_token = token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body=msg,
                              from_=from_num,
                              to=to_num
                            )

def send_text_message(msg: str, accountSid, token, from_num, to_num):
    account_sid = accountSid
    auth_token = token
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=msg,
                     from_=from_num,
                     to=to_num
                )


              

                
                
                
