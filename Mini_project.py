class Incentive:
    def __init__(self, name):
        self.driver = name[0]
        self.ID = name[1]
        self.trip = name[2]
        self.hour = name[3]

    def validator(self):
        if self.trip >= 40 and self.hour >= 40:
            print(f"You are eligible for incentive")
        else:
            if self.trip < 40:
                remaining = self.trip - 40
                print(f'plz complete {abs(remaining)} more trips for incentive')


mad = ('mad', '1A33B4', 39, 41)
ricky = ('rick', '343D3', 40, 40)
person1 = Incentive(ricky)
person1.validator()
person = Incentive(mad)
person.validator()


