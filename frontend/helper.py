import pandas as pd 
import preprocesses


df, match_stats = preprocesses.final_database()
player_stats = preprocesses.player_stats()

# All Players
def fetch_all_players():
    all_batters = df['batter'].unique().tolist()
    all_bowlers = df['bowler'].unique().tolist()

    all_players = all_batters + all_bowlers
    ipl_players = []

    for player in all_players:
        if player not in ipl_players:
            ipl_players.append(player)
    
    return sorted(ipl_players)

# Total runs scored
def total_runs_scored(player):
    
    temp_players_stats = player_stats.sort_values(by='runs', ascending=False).reset_index(drop=True)
    rank = temp_players_stats[temp_players_stats['player'] == player].index[0]

    player_runs = temp_players_stats[temp_players_stats['player'] == player]['runs']

    return int(player_runs), rank + 1

# Total wickets taken
def total_wickets_taken(bowler):

    temp_player_stats = player_stats.sort_values(by='wickets', ascending=False).reset_index(drop=True)
    rank = temp_player_stats[temp_player_stats['player'] == bowler].index[0]

    player_wickets = temp_player_stats[temp_player_stats['player'] == bowler]['wickets']

    return int(player_wickets), rank + 1

# Total Overs Bowled
def total_balls_bowled(bowler):
    balls = df['bowler']
    balls = balls.value_counts().reset_index()
    total_balls = balls[balls['bowler'] == bowler]
    if total_balls.empty:
        return 0
    return int(total_balls['count'])

# Teams Played
def teams_played(player):
    bat_team = df[(df['batter'] == player)]
    teams_played1 = bat_team['batting_team'].unique().tolist()
    ball_team = df[(df['bowler'] == player)]
    teams_played1.extend(ball_team['bowling_team'].unique().tolist())
    teams_played = []
    for team in teams_played1:
        if team not in teams_played:
            teams_played.append(team)
    teams_played = pd.DataFrame(teams_played).rename(columns={0: "Teams"})
    teams_played.index = range(1, len(teams_played) + 1)

    def find_year(team, ind_player):
        new_df = match_stats[match_stats.apply(lambda row: ind_player in row['team1_players'] and row['team1'] == team, axis=1)][['team1', 'year']].reset_index(drop=True)
        team1 = new_df['year'].unique().tolist()

        new_df = match_stats[match_stats.apply(lambda row: ind_player in row['team2_players'] and row['team2'] == team, axis=1)][['team2', 'year']].reset_index(drop=True)
        team2 = new_df['year'].unique().tolist()
        years = team1 + team2
        ans = []
        for year in years:
            if year not in ans:
                ans.append(year)

        return ans
    teams_played['years_played'] = teams_played.apply(lambda row: find_year(row['Teams'], player), axis=1)
    teams_played['years_played'] = teams_played['years_played'].apply(lambda row: sorted(row))
    return teams_played

# Total matches Won
def matches_won(player):
    matches1 = match_stats[match_stats.apply(lambda row: (player in row['team1_players'] and row['result'] == 'Win') and (row['team1'] == row['winner']), axis=1)]
    matches2 = match_stats[match_stats.apply(lambda row: (player in row['team2_players'] and row['result'] == 'Win') and (row['team2'] == row['winner']), axis=1)]

    return len(matches1) + len(matches2)

# Player of Match
def player_of_match(player):
    matches = match_stats[match_stats.apply(lambda row: player in row['player_of_match'], axis=1)]
    
    return len(matches)



