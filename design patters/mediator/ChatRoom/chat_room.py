from person import Person


class ChatRoom:
    def __init__(self) -> None:
        self.peoples: list[Person] = []

    def join(self, person: Person):
        pass

    def broadcast(self, source: str, message: str) -> None:
        pass

    def message(self, source, destination: str, message: str) -> None:
        pass