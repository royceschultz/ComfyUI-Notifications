from .util import ComfyAnyType
import json

class UnifiedNotification:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any": (ComfyAnyType("*"), {}),
                "mode": (["always", "on empty queue"], {}),
                "system_notification": ("BOOLEAN", {"default": True}),
                "notification_text": ('STRING', {'default': 'Your notification has triggered.'}),
                "play_sound": ("BOOLEAN", {"default": True}),
                "volume": ("FLOAT", {"min": 0, "max": 1, "step": 0.1, "default": 0.5}),
                "file": ("STRING", { "default": "notify.mp3" }),
            },
        }

    FUNCTION = "nop"
    OUTPUT_NODE = True
    RETURN_TYPES = tuple()
    CATEGORY = "notifications"

    def nop(self, *args, **kwargs):
        for k, v in kwargs.items():
            kwargs[k] = [v] # UI expects an iterable for some reason
        del kwargs['any'] # Avoid passing large objects
        kwargs['args'] = args
        return {"ui": kwargs, "result": (0, )}
