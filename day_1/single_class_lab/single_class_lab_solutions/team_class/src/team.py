class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_to_find):
      # return self.players.count(player_to_find) > 0

      # return player_to_find in self.players

      for player in self.players:
        if player == player_to_find:
          return True
      return False

    def play_game(self, game_won):
        if game_won:
            self.points += 3
