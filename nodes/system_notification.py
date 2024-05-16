from .util import ComfyAnyType

class SystemNotification:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any": (ComfyAnyType("*"), {}),
                "mode": (["always", "on empty queue"], {}),
                "notification_text": ('STRING', {'default': 'Your notification has triggered.'}),
            },
        }

    FUNCTION = "nop"
    OUTPUT_NODE = True
    RETURN_TYPES = tuple()
    CATEGORY = "notifications"

    def nop(self, any, mode, notification_text):
        return {"ui": {"notification_text": [notification_text]}, "result": (0, )}
