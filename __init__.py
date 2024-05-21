from .nodes.play_sound import PlaySound
from .nodes.system_notification import SystemNotification
from .nodes.unified_notification import UnifiedNotification
from .nodes.webhook import Webhook

NODE_CLASS_MAPPINGS = {
    "Notif-PlaySound": PlaySound,
    "Notif-SystemNotification": SystemNotification,
    "Notif-UnifiedNotification": UnifiedNotification,
    "Notif-Webhook": Webhook,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Notif-PlaySound": "Play Sound",
    "Notif-SystemNotification": "System Notification",
    "Notif-UnifiedNotification": "Unified Notification",
    "Notif-Webhook": "Webhook",
}

WEB_DIRECTORY = "./web"
