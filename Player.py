class Player:
  def __init__(self, player_id):
      self.player_id = player_id
      self.score = 0

  def increase_score(self):
      self.score += 1

