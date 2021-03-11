class Client:
    def __init__(self, firstName, lastName, egn):
        self.firstName = firstName
        self.lastName = lastName
        self.egn = egn

    def printClient(self):
        print(f'Client name is {self.firstName} {self.lastName} with EGN {self.egn}')

    @classmethod
    def from_strings(cls, fullName, egn):
        firstName, lastName = fullName.split(' ')
        return cls(firstName, lastName, egn)
