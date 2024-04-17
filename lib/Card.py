from lib.values import values


class Card:
    def __init__(self, face_value, suit) -> None:
        self.suit = suit
        self.face_value = face_value if type(face_value) is str else face_value
        self.value = values[self.face_value]

    def __repr__(self) -> str:
        return f"{self.face_value} of {self.suit}"

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
