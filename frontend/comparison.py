import helper
import pandas as pd

def compare_players(player1, player2):
    player1_runs, player1_runs_rank = helper.total_runs_scored(player1)
    player2_runs, player2_runs_rank = helper.total_runs_scored(player2)

    player1_wickets, player1_wickets_rank = helper.total_wickets_taken(player1)
    player2_wickets, player2_wickets_rank = helper.total_wickets_taken(player2)

    if player1_wickets == 0:
        player1_wickets_rank = "NA"
    if player2_wickets == 0:
        player2_wickets_rank = "NA"
    
    player1_balls = helper.total_balls_bowled(player1)
    player2_balls = helper.total_balls_bowled(player2)

    player1_teams = helper.teams_played(player1)['Teams'].tolist()
    player2_teams = helper.teams_played(player2)['Teams'].tolist()

    player1_matches_won = helper.matches_won(player1)
    player2_matches_won = helper.matches_won(player2)

    player1_pom = helper.player_of_match(player1)
    player2_pom = helper.player_of_match(player2)

    ipl_seasons, player1_sixes = helper.number_of_sixes(player1)
    ipl_seasons,player2_sixes = helper.number_of_sixes(player2)

    player1_total_sixes = 0
    player2_total_sixes = 0
    
    ipl_seasons,player1_fours = helper.number_of_fours(player1)
    ipl_seasons,player2_fours = helper.number_of_fours(player2)

    player1_total_fours = 0
    player2_total_fours = 0


    for i in range(len(player1_sixes)):
        player1_total_sixes += player1_sixes[i]
        player2_total_sixes += player2_sixes[i]
        player1_total_fours += player1_fours[i]
        player2_total_fours += player2_fours[i]


    df = pd.DataFrame(columns=[' ', 'Player-1', 'Player-2'])

    property = ['Rank by Runs', 'Total Runs', 'Rank by Wicket', 'Total Wickets', 'Balls Bowled', 'All Teams', 'Matches Won', 'Player of Match', 'Sixes', 'Fours']
    player1_list = [str(player1_runs_rank), str(player1_runs), str(player1_wickets_rank), str(player1_wickets), str(player1_balls), ", ".join(player1_teams), str(player1_matches_won), str(player1_pom), str(player1_total_sixes), str(player1_total_fours)]
    player2_list = [str(player2_runs_rank), str(player2_runs), str(player2_wickets_rank), str(player2_wickets), str(player2_balls), ", ".join(player2_teams), str(player2_matches_won), str(player2_pom), str(player2_total_sixes), str(player2_total_fours)]
    df[' '] = property
    df['Player-1'] = player1_list
    df['Player-2'] = player2_list

    return df