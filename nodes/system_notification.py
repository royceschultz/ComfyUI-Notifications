from .util import ComfyAnyType

class SystemNotification:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any": (ComfyAnyType("*"), {}),
                "mode": (["always", "on empty queue"], {}),
            },
        }

    FUNCTION = "nop"
    OUTPUT_NODE = True
    RETURN_TYPES = tuple()
    CATEGORY = "notifications"

    def nop(self, any, mode):
        return {"ui": {"a": []}, "result": (0, )}
