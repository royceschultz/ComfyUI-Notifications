from .nodes.play_sound import PlaySound
from .nodes.system_notification import SystemNotification

NODE_CLASS_MAPPINGS = {
    "Notif-PlaySound": PlaySound,
    "Notif-SystemNotification": SystemNotification,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Notif-PlaySound": "Play Sound",
    "Notif-SystemNotification": "System Notification",
}

WEB_DIRECTORY = "./web"
