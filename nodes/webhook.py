import requests
import json
from server import PromptServer

from .util import ComfyAnyType

class Webhook:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any": (ComfyAnyType("*"), {}),
                "mode": (["always", "on empty queue"], {}),
                "webhook_url": ("STRING", {'default': 'http://localhost:5000/'}),
                "verify_ssl": ("BOOLEAN", {"default": True}),
                "notification_text": ('STRING', {'default': 'Your notification has triggered.'}),
                "json_format": ('STRING', {'default': '{"text": "<notification_text>"}'}),
                "timeout": ('FLOAT', {'default': 3, 'min': 0, 'max': 60}),
            },
        }

    FUNCTION = 'hook'
    OUTPUT_NODE = True
    RETURN_TYPES = tuple()
    CATEGORY = "notifications"

    def hook(self, any, mode, webhook_url, notification_text, json_format, timeout, verify_ssl):
        if mode == 'on empty queue':
            queue = PromptServer.instance.prompt_queue.queue
            queue_len = len(queue)
            if queue_len > 0:
                print(f'[Webhook Notificaton] Not sending notification, queue is not empty (size: {queue_len})')
                return (0, )
        payload = json_format.replace("<notification_text>", notification_text)
        payload = json.loads(payload)
        res = requests.post(webhook_url, json=payload, timeout=timeout, verify=verify_ssl)
        res.raise_for_status()
        return (0, )
