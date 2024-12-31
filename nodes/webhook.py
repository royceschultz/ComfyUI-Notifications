import requests
import json

from .util import ComfyAnyType

class Webhook:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any": (ComfyAnyType("*"), {}),
                # "mode": (["always", "on empty queue"], {}), # TODO: Need a way to get queue status from main.py
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

    def hook(self, any, webhook_url, notification_text, json_format, timeout, verify_ssl):

        payload = json_format.replace("<notification_text>", notification_text)
        payload = json.loads(payload)
        res = requests.post(webhook_url, json=payload, timeout=timeout, verify=verify_ssl)
        res.raise_for_status()
        return (0, )
