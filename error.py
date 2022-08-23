class Error:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        print(f"FATAL ERROR! {name}: {message}")

class WrongType(Error):
    def __init__(self, message):
        super().__init__("Wrong Type Error", message)

class MissingSprite(Error):
    def __init__(self, message):
        super().__init__("Missing Sprite Error", message)