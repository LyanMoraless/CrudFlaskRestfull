from flask_restful import Resource, reqparse

from models.player import PlayerModel

class Players(Resource): 
  def get(self):
    return {'players': [player.json() for player in PlayerModel.query.all()]}

class Player(Resource):

  arguments = reqparse.RequestParser()
  arguments.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank") 
  arguments.add_argument('rating', type=float, required=True, help="The field 'rating' cannot be left blank")
  arguments.add_argument('shirt', type=str, required=True, help="The field 'shirt' cannot be left blank")
  arguments.add_argument('position', type=str, required=True, help="The field 'position' cannot be left blank")
  arguments.add_argument('team', type=str, required=True, help="The field 'team' cannot be left blank")
  arguments.add_argument('nacionality', type=str, required=True, help="The field 'nacionality' cannot be left blank")
  arguments.add_argument('goals', type=str, required=True, help="The field 'goals' cannot be left blank")

  def get(self, player_id):
    player = PlayerModel.findPlayer(player_id)
    if player:
      return player.json()
    return {'message': 'Player not found'}, 404

  def put(self, player_id):
 
    dates = Player.arguments.parse_args()
    playerFounded = PlayerModel.findPlayer(player_id)
    if playerFounded:
      playerFounded.updatePlayer(**dates)
      playerFounded.savePlayer()
      return playerFounded.json(), 200
    player = PlayerModel(player_id, **dates)
    try:
      player.savePlayer()
    except:
      return {'message': 'An internal error ocurred trying to save player.'}, 500
    return player.json(), 201

  def post(self, player_id):
    dates = Player.arguments.parse_args()
    player = PlayerModel(player_id, **dates)
    try:
      player.savePlayer()
    except:
      return {'message': 'An internal error ocurred trying to save player.'}, 500
    return player.json()
    
  def delete(self, player_id):
    player = PlayerModel.findPlayer(player_id)
    if player:
      try:
        player.deletePlayer()
      except:
        return {'message': 'An error ocurred trying to delete player'}, 500
      return {"message:" 'Player deleted'}
    return {"message": 'Player not found'}, 404
