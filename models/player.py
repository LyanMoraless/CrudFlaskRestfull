from sqlAlchemy import bank

class PlayerModel(bank.Model):
  __tablename__ = 'players'
  player_id = bank.Column(bank.String, primary_key=True)
  name = bank.Column(bank.String(20))
  rating = bank.Column(bank.Float(precision=1))
  shirt = bank.Column(bank.String(2))
  position = bank.Column(bank.String(20))
  team = bank.Column(bank.String(30))
  nacionality = bank.Column(bank.String(20))
  goals = bank.Column(bank.String(3))


  def __init__(self, player_id, name, rating, shirt, position, team, nacionality, goals):
    self.player_id = player_id
    self.name = name
    self.rating = rating
    self.shirt = shirt
    self.position = position
    self.team = team
    self.nacionality = nacionality
    self.goals = goals

  def json(self):
    return {
      'player_id': self.player_id,
      'name': self.name,
      'rating': self.rating,
      'shirt': self.shirt,
      'position': self.position,
      'team': self.team,
      'nacionality': self.nacionality,
      'goals': self.goals
    }
  
  @classmethod
  def findPlayer(cls, player_id):
    player = cls.query.filter_by(player_id=player_id).first()
    if player:
      return player
    return None

  def savePlayer(self):
    bank.session.add(self)
    bank.session.commit()

  def updatePlayer(self, name, rating, shirt, position, team, nacionality, goals):
    self.name = name
    self.rating = rating
    self.shirt = shirt
    self.position = position
    self.team = team
    self.nacionality = nacionality
    self.goals = goals

  def deletePlayer(self): 
    bank.session.delete(self)
    bank.session.commit()