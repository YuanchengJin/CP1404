from musician import Musician

class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        musicians_str = ", ".join([str(musician) for musician in self.musicians])
        return f"{self.name} ({musicians_str})"

    def play(self):
        return "\n".join(musician.play() for musician in self.musicians)
