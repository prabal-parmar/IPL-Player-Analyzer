import pandas as pd 
import datetime


df = pd.read_csv('../deliveries.csv')
match_stats = pd.read_csv('../Match_Info.csv')


# Fetch all platers
def fetch_all_players():
    all_batters = df['batter'].unique().tolist()
    all_bowlers = df['bowler'].unique().tolist()

    all_players = all_batters + all_bowlers
    ipl_players = []

    for player in all_players:
        if player not in ipl_players:
            ipl_players.append(player)
    
    return sorted(ipl_players)

# Upgraded Datasets 
def final_database():
    date = match_stats['match_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").date()).tolist()
    year = [x.year for x in date]
    match_stats['year'] = year

    return df, match_stats

# Player Stats Dataset
def player_stats():
    ipl_players = fetch_all_players()
    players_df = pd.DataFrame({'player': ipl_players, 'runs': [0]*len(ipl_players), 'wickets': [0]*len(ipl_players)})
    temp = df[['batter', 'batsman_runs']]

    bowlers_stats = df[['bowler', 'is_wicket', 'dismissal_kind']]
    bowlers_stats = bowlers_stats[~bowlers_stats['dismissal_kind'].isin(['run out', 'None', 'retired hurt', 'retired out', 'obstructing the field'])]

    def find_total_score(player):
        new_df = temp[temp['batter'] == player]
        runs = 0
        for run in new_df['batsman_runs']:
            runs += int(run)
        return int(runs)
    
    def find_total_wickets(bowler):
        new_df = bowlers_stats[bowlers_stats['bowler'] == bowler]
        wickets = 0
        for w in new_df['is_wicket']:
            wickets += int(w)
        return int(wickets)
    
    for i in range(len(players_df)):
        total_score = find_total_score(players_df.iloc[i,0])
        total_wickets = find_total_wickets(players_df.iloc[i,0])
        players_df.at[i, 'runs'] = total_score
        players_df.at[i, 'wickets'] = total_wickets
    
    return players_df

def fetch_merged_df():
    temp_df = df
    temp_match_stats = match_stats
    temp_match_stats['match_id'] = temp_match_stats['match_number']
    temp_match_stats = temp_match_stats.drop(columns=['match_number'])

    merged_df = pd.merge(temp_df, temp_match_stats, on='match_id')

    return merged_df


    
