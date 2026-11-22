'''15. Sports Management
Player
CricketPlayer
Captain(CricketPlayer)

Add captain-specific functionality.

'''

class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class CricketPlayer(Player):
    def __init__(self, name, role):
        super().__init__(name)
        self.__role = role

    def get_role(self):
        return self.__role


class Captain(CricketPlayer):
    def __init__(self, name, role, team):
        super().__init__(name, role)
        self.__team = team

    def captain_details(self):
        print("----- Captain Details -----")
        print(f"Name : {self.get_name()}")
        print(f"Role : {self.get_role()}")
        print(f"Team : {self.__team}")

    def lead_team(self):
        print(f"{self.get_name()} is leading the team.")


captain1 = Captain("Rohit Sharma", "Batsman", "India")

captain1.captain_details()
captain1.lead_team()