class Band:

    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        # get all band members
        # for each of the band members ask to play solo
        # in order of joining band
        solos = []
        for members in self.members:
            solos.append(members.play_solo())
        return solos

    # https://www.programiz.com/python-programming/list-comprehension
    # def play_solos(self):
    #     return [member.play_solo() for member in self.members]

    # class method - https://www.programiz.com/python-programming/methods/built-in/classmethod
    # create class method to_list that returns a list of previously created Band instances

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician(Band):
    pass


class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
