class Client:
    def __init__(self, firstName, lastName, egn):
        self.firstName = firstName
        self.lastName = lastName
        self.egn = egn

    def getEgn(self):
        return self.egn

    def print(self):
        print(f'Client name is {self.firstName} {self.lastName} with EGN {self.egn}')

    @classmethod
    def from_strings(cls, clientData):
        firstName, lastName, egn = clientData.split(' ')
        return cls(firstName, lastName, egn)
