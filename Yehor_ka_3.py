class Warrior:

    AllRanks = ["Pushover",
                "Novice",
                "Fighter",
                "Warrior",
                "Veteran",
                "Sage",
                "Elite",
                "Conqueror",
                "Champion",
                "Master",
                "Greatest"]

    NeedExpToUpLvl = 100
    MaxExp = 10000
    MaxLvl = 100
    MinLvl = 1

    def __init__(self):
        self.level = self.MinLvl
        self.experience = self.NeedExpToUpLvl
        self.rank = self.AllRanks[0]
        self.achievements = []

    def battle(self, EnemyLevel):
        if not (self.MinLvl <= EnemyLevel <= self.MaxLvl):
            result = "Invalid level"
        elif EnemyLevel == self.level:
            self.experience += 10
            result = "A good fight"
        elif EnemyLevel == self.level - 1:
            self.experience += 5
            result = "A good fight"
        elif EnemyLevel <= self.level - 2:
            result = "Easy fight"
        elif EnemyLevel >= self.level + 5 and EnemyLevel // 10 != self.level // 10:
            result = "You've been defeated"
        else:
            self.experience += 20 * pow(EnemyLevel - self.level, 2)
            result = "An intense fight"

        if self.experience >= self.MaxExp:
            self.experience = self.MaxExp
            self.level = self.MaxLvl
            self.rank = self.AllRanks[self.level // 10]
        elif self.experience - (self.level * self.NeedExpToUpLvl) >= self.NeedExpToUpLvl:
            self.level += (self.experience - (self.level * self.NeedExpToUpLvl)) // self.NeedExpToUpLvl
            self.rank = self.AllRanks[self.level // 10]

        return(result)

    def training(self, Info):
        if Info[2] > self.level:
            result = "Not strong enough"
        else:
            self.experience += Info[1]
            self.achievements.append(Info[0])
            result = Info[0]

            if self.experience >= self.MaxExp:
                self.experience = self.MaxExp
                self.level = self.MaxLvl
                self.rank = self.AllRanks[self.level // 10]
            elif self.experience - (self.level * self.NeedExpToUpLvl) >= self.NeedExpToUpLvl:
                self.level += (self.experience - (self.level * self.NeedExpToUpLvl)) // self.NeedExpToUpLvl
                self.rank = self.AllRanks[self.level // 10]

        return(result)



