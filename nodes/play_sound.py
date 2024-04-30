from .util import ComfyAnyType

class PlaySound:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any": (ComfyAnyType('*'), {}),
                "mode": (["always", "on empty queue"], {}),
                "volume": ("FLOAT", {"min": 0, "max": 1, "step": 0.1, "default": 0.5}),
                "file": ("STRING", { "default": "notify.mp3" })
            },
        }

    FUNCTION = "nop"
    OUTPUT_NODE = True
    RETURN_TYPES = tuple()
    CATEGORY = "notifications"

    def nop(self, any, mode, volume, file):
        return {"ui": {"a": []}, "result": (0, )}
