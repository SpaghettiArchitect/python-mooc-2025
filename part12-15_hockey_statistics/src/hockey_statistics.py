import json


class Player:
    def __init__(
        self,
        name: str,
        nationality: str,
        assists: int,
        goals: int,
        penalties: int,
        team: str,
        games: int,
    ):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def get_points(self):
        return self.assists + self.goals

    def __str__(self):
        return f"{self.name:21}{self.team:4} {self.goals:2} + {self.assists:2} = {(self.get_points()):3}"


class PlayersNHL:
    def __init__(self):
        self.players: list[Player] = []

    def add_player(self, player: Player):
        self.players.append(player)

    def load_players(self, all_players: list[dict]):
        for player in all_players:
            new_player = Player(**player)
            self.add_player(new_player)

    def search_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player
        else:
            return None

    def get_teams_abbreviations(self):
        return sorted(list(set(player.team for player in self.players)))

    def get_countries_abbreviations(self):
        return sorted(list(set(player.nationality for player in self.players)))

    def get_total_players(self):
        return len(self.players)

    def get_players_by_team(self, team: str):
        players_in_team = [player for player in self.players if player.team == team]
        return sorted(
            players_in_team,
            key=lambda player: player.get_points(),
            reverse=True,
        )

    def get_players_by_country(self, country: str):
        players_in_country = [
            player for player in self.players if player.nationality == country
        ]
        return sorted(
            players_in_country,
            key=lambda player: player.get_points(),
            reverse=True,
        )

    def get_players_by_most_points(self):
        return sorted(
            self.players,
            key=lambda player: (player.get_points(), player.goals),
            reverse=True,
        )

    def get_players_by_most_goals(self):
        return sorted(
            self.players, key=lambda player: (player.goals, -player.games), reverse=True
        )


class FileHandler:
    def load_data(self, filename: str):
        with open(filename) as file:
            data = file.read()
        return json.loads(data)


class HockeyStatsApp:
    def __init__(self, storage: FileHandler, players: PlayersNHL):
        self.__storage = storage
        self.__players = players

    def load_data(self):
        filename = input("file name: ")
        data = self.__storage.load_data(filename)
        self.__players.load_players(data)
        print(f"read the data of {self.__players.get_total_players()} players")

    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_for_player(self):
        name = input("name: ")

        if player := self.__players.search_player(name):
            print(player)

    def list_teams(self):
        for team in self.__players.get_teams_abbreviations():
            print(team)

    def list_countries(self):
        for country in self.__players.get_countries_abbreviations():
            print(country)

    def list_team_of_players(self):
        team = input("team: ")
        for player in self.__players.get_players_by_team(team):
            print(player)

    def list_players_from_country(self):
        country = input("country: ")
        for player in self.__players.get_players_by_country(country):
            print(player)

    def list_players_by_most_points(self):
        n = int(input("how many: "))
        players_by_points = self.__players.get_players_by_most_points()
        for i in range(n):
            print(players_by_points[i])

    def list_players_by_most_goals(self):
        n = int(input("how many: "))
        players_by_goals = self.__players.get_players_by_most_goals()
        for i in range(n):
            print(players_by_goals[i])

    def exec(self):
        self.load_data()
        print()
        self.help()

        while True:
            print()
            command = int(input("command: "))

            if command == 0:
                break

            elif command == 1:
                self.search_for_player()

            elif command == 2:
                self.list_teams()

            elif command == 3:
                self.list_countries()

            elif command == 4:
                self.list_team_of_players()

            elif command == 5:
                self.list_players_from_country()

            elif command == 6:
                self.list_players_by_most_points()

            elif command == 7:
                self.list_players_by_most_goals()


file_handler = FileHandler()
players = PlayersNHL()
app = HockeyStatsApp(file_handler, players)
app.exec()
