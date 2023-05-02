class Item:
    def __init__(self, name: str, photo: str = '') -> None:
        self.name = name
        self.photo = photo

    def __str__(self) -> str:
        return self.name
