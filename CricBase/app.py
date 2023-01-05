
from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
from player import Player
from batting_analysis import BattingAnalysis
from bowling_analysis import BowlingAnalysis
from dismissal import Dismissal
from matches import Match
from team import Team
from tournament import Tournament
from fielding_analysis import FieldingAnalysis

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "root123"
app.config['MYSQL_DATABASE_DB'] = 'CRICBASE'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
# player 
@app.route('/player/<int:player_id>', methods=['GET'])
def get_players(player_id):
    conn = mysql.connect()
    player = Player.read_from_database(conn, player_id)
    if player is None:
        return "No Player found", 404
    return player.to_json(), 200

@app.route('/player', methods=['POST'])
def create_player():
    conn = mysql.connect()
    data = request.get_json()
    player = Player.from_json(data)
    Player.write_to_database(conn, player)
    return jsonify({'message': 'Player created successfully'}), 201

@app.route('/player/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    conn = mysql.connect()
    Player.delete_from_database(conn, player_id)
    return jsonify({'message': 'Player deleted successfully'}), 200

#teams 
@app.route('/team/<int:team_id>', methods=['GET'])
def get_team(team_id):
    conn = mysql.connect()
    team = Team.read_from_database(conn, team_id)
    return team.to_json(), 200

@app.route('/team', methods=['POST'])
def create_team():
    conn = mysql.connect()
    data = request.get_json()
    team = Team.from_json(data)
    Team.write_to_database(conn, team)
    return jsonify({'message': 'Team created successfully'}), 201

@app.route('/team/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    conn = mysql.connect()
    Team.delete_from_database(conn, team_id)
    return jsonify({'message': 'Team deleted successfully'}), 200

# tournament
@app.route('/tournament/<int:tournament_id>', methods=['GET'])
def get_tournament(tournament_id):
    conn = mysql.connect()
    tournament = Tournament.read_from_database(conn, tournament_id)
    return tournament.to_json(), 200

@app.route('/tournament', methods=['POST'])
def create_tournament():
    conn = mysql.connect()
    data = request.get_json()
    tournament = Tournament.from_json(data)
    Tournament.write_to_database(conn, tournament)
    return jsonify({'message': 'Tournament created successfully'}), 201

@app.route('/tournament/<int:tournament_id>', methods=['DELETE'])
def delete_tournament(tournament_id):
    conn = mysql.connect()
    Tournament.delete_from_database(conn, tournament_id)
    return jsonify({'message': 'Tournament deleted successfully'}), 200

# matches
@app.route('/matches/<int:match_id>', methods=['GET'])
def get_match(match_id):
    conn = mysql.connect()
    match = Match.read_from_database(conn, match_id)
    return match.to_json(), 200

@app.route('/matches', methods=['POST'])
def create_match():
    conn = mysql.connect()
    data = request.get_json()
    match = Match.from_json(data)
    Match.write_to_database(conn, match)
    resp = jsonify({'message': 'Match created successfully'})
    resp.status_code = 201
    return resp

@app.route('/matches/<int:match_id>', methods=['DELETE'])
def delete_match(match_id):
    conn = mysql.connect()
    Match.delete_from_database(conn, match_id)
    resp = jsonify({'message': 'Match deleted successfully'})
    resp.status_code = 200
    return resp


# batting analysis
@app.route('/batting_analysis/<int:player_id>/<int:match_id>/<int:team_id>', methods=['GET'])
def get_batting_analysis(player_id, match_id, team_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    battingAnalysis = BattingAnalysis.read_from_database(conn, player_id, match_id, team_id)
    return battingAnalysis.to_json(), 200

@app.route('/batting_analysis', methods=['POST'])
def create_batting_analysis():
    conn = mysql.connect()
    data = request.get_json()
    battingAnalysis = BattingAnalysis.from_json(data)
    BattingAnalysis.write_to_database(conn, battingAnalysis)
    resp = jsonify({'message': 'Batting analysis created successfully'})
    resp.status_code = 200
    return resp

@app.route('/batting_analysis/<int:player_id>/<int:match_id>/<int:team_id>', methods=['DELETE'])
def delete_batting_analysis(player_id, match_id, team_id):
    conn = mysql.connect()
    BattingAnalysis.delete_from_database(player_id, match_id, team_id)
    resp = jsonify({'message': 'Batting analysis deleted successfully'})
    resp.status_code = 200
    return resp

# bowling analysis
@app.route('/bowling_analysis/<int:player_id>/<int:match_id>/<int:team_id>', methods=['GET'])
def get_bowling_analysis(player_id, match_id, team_id):
    conn = mysql.connect()
    bowlingAnalysis = BowlingAnalysis.read_from_database(conn, player_id, match_id, team_id)
    return bowlingAnalysis.to_json(), 200

@app.route('/bowling_analysis', methods=['POST'])
def create_bowling_analysis():
    conn = mysql.connect()
    data = request.get_json()
    bowlingAnalysis = BowlingAnalysis.from_json(data)
    BowlingAnalysis.write_to_database(conn, bowlingAnalysis)
    resp = jsonify({'message': 'Bowling analysis created successfully'})
    resp.status_code = 201
    return resp

@app.route('/bowling_analysis/<int:player_id>/<int:match_id>/<int:team_id>', methods=['DELETE'])
def delete_bowling_analysis(player_id, match_id, team_id):
    conn = mysql.connect()
    BowlingAnalysis.delete_from_database(conn, player_id, match_id, team_id)
    resp = jsonify({'message': 'Bowling analysis deleted successfully'})
    resp.status_code = 200
    return resp

# fielding analysis 
@app.route('/fielding_analysis/<int:player_id>/<int:match_id>/<int:team_id>', methods=['GET'])
def get_fielding_analysis(player_id, match_id, team_id):
    conn = mysql.connect()
    fielding = FieldingAnalysis.read_from_database(conn, player_id, match_id, team_id)
    return fielding.to_json(), 200

@app.route('/fielding_analysis', methods=['POST'])
def create_fielding_analysis():
    conn = mysql.connect()
    data = request.get_json()
    fielding = FieldingAnalysis.from_json(data)
    FieldingAnalysis.write_to_database(conn, fielding)
    resp = jsonify({'message': 'Fielding analysis created successfully'})
    resp.status_code = 201
    return resp

@app.route('/fielding_analysis/<int:player_id>/<int:match_id>/<int:team_id>', methods=['DELETE'])
def delete_fielding_analysis(player_id, match_id, team_id):
    conn = mysql.connect()
    FieldingAnalysis.delete_from_database(conn, player_id, match_id, team_id)
    resp = jsonify({'message': 'Fielding analysis deleted successfully'})
    resp.status_code = 200
    return resp

# dismissal table 
@app.route('/dismissals/<int:match_id>/<int:batter_id>', methods=['GET'])
def get_dismissal(match_id, batter_id):
    conn = mysql.connect()
    dismissal = Dismissal.read_from_database(conn, match_id, batter_id)
    return dismissal.to_json(), 200

@app.route('/dismissals', methods=['POST'])
def create_dismissal():
    conn = mysql.connect()
    data = request.get_json()
    dismissal = Dismissal.from_json(data)
    Dismissal.write_to_database(conn, dismissal)
    resp = jsonify({'message': 'Dismissal created successfully'})
    resp.status_code = 201
    return resp

@app.route('/dismissals/<int:match_id>/<int:batter_id>', methods=['DELETE'])
def delete_dismissal(match_id, batter_id):
    conn = mysql.connect()
    Dismissal.delete_from_database(conn, match_id, batter_id)
    resp = jsonify({'message': 'Dismissal deleted successfully'})
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run(debug=True)