
import json
from pyfcm import FCMNotification
from firebase_admin import messaging



FCM_API_KEY = "AAAA6mcBaL8:APA91bH4ly7V_S4VOSBJBZmOf39o6bdt048uwmQTDfgurxJTlPTjD7LJJFORt9j4ca_r_Dk82FOOceOBCBgW3gFZAigJemC5hy9ZLgrFscA01GjeFAwDTnMgXGRPhOIXVEqRCcjtOpDL"

push_service = FCMNotification(api_key=FCM_API_KEY)
def send_notification(resgistration_token, title, body, link, icon, msg_type):
    data_message = {
        "link": link,
        "type" : msg_type,
    } 
    push_service.notify_single_device(
        registration_id=resgistration_token,
        message_title=title,
        message_body=body,
        message_icon= icon,
        data_message=data_message,
    )
    # print(icon)
    # message = messaging.Message(
    #     notification=messaging.Notification(title=title, body=body, image= 'http://localhost:8000' + icon),
    #     token=resgistration_token,
    # )
    # response = messaging.send(message)
    # print('Successfully sent message:', response)
 
def send(user, title="", body="", link="", icon="", type=""):
    for token in user.fcm_tokens.all():
        try:
            send_notification(token.token, title, body, link, icon, type)
        except:
            raise
