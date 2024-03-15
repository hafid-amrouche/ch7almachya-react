
import json
from pyfcm import FCMNotification


FCM_API_KEY = "AAAA1kBgl_Q:APA91bHszWCi9ItE_y-F9ngHJAr3q70cCoxVowQgs8rmDeH5pXoYP6FN_XYNezI3mjxt790NchStphjZaV95FSuTG3pIgXp_RRzVYppoBpoOCkYo_kUG1g5_Hu_iZTVB0uonqqrAwzFh"

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
 
def send(user, title="", body="", link="", icon="", type=""):
    for token in user.fcm_tokens.all():
        send_notification(token.token, title, body, link, icon, type)
