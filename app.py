from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.player import Players, Player

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db' #postgresql://postgres:123456@localhost:5432/postgres
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
api = Api(app)

@app.before_first_request
def makeBank():
  bank.create_all()

api.add_resource(Players, '/players/')
api.add_resource(Player, '/players/<string:player_id>')

if __name__ == '__main__':
  from sqlAlchemy import bank
  bank.init_app(app)
  app.run(debug=True)
