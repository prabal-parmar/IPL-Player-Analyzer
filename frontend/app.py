import streamlit as st
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="IPL Players Analysis",
    layout="wide",
    initial_sidebar_state="expanded")


st.header("IPL Players Analysis")

all_players = helper.fetch_all_players()

option = st.selectbox(
    "Select a Player",
    all_players,
    index=None,
    placeholder="Select any player",
)

show_analysis = st.button("Show Analysis")


if show_analysis:

    if option == None:
        st.title("Select any player")
        st.stop()

    st.title(option)

    col1, col2, col3 = st.columns(3)
 
    # Total Runs
    with col1:
        st.header("Total Runs Scored")
        total_runs, rank = helper.total_runs_scored(option)
        st.header(total_runs)
        if rank <= 50:
            st.write("Rank-" +str(rank))

    # Total overs bowled
    with col2:
        st.header("Total Balls Bowled")
        total_balls = helper.total_balls_bowled(option)
        st.header(total_balls)

    # Total Wickets
    with col3:
        st.header("Total Wickets ")
        total_wickets, rank = helper.total_wickets_taken(option)
        st.header(total_wickets)
        if rank <= 50:
            st.write("Rank-"+str(rank))
    
    # teams played from with year
    st.header("Teams " + option + " played from")
    teams = helper.teams_played(option)
    st.dataframe(teams)

    # Total Matches Won
    col1, col2 = st.columns(2)
    with col1:
        st.header("Total Matches Won")
        matches_won = helper.matches_won(option)
        st.header(matches_won)

    with col2:
        st.header("Player of Match")
        pom = helper.player_of_match(option)
        st.header(pom)

    
    ## Batting Statistics
    st.title("Batting Statistics")

    # Total sixes and fours
    col1, col2 = st.columns(2)

    with col1:
        st.header("Sixes Analysis")
        years, all_sixes = helper.number_of_sixes(option)
        seasons = [str(year) for year in years]
    
        fig, ax = plt.subplots()
        plt.xticks(rotation='vertical')
        bars = ax.bar(seasons, all_sixes)
        ax.bar_label(bars)
        plt.xlabel("Years")
        plt.ylabel("Sixes")
        st.pyplot(fig)

    with col2:
        st.header("Fours Analysis")
        years, all_fours = helper.number_of_fours(option)
        seasons = [str(year) for year in years]
    
        fig, ax = plt.subplots()
        plt.xticks(rotation='vertical')
        bars = ax.bar(seasons, all_fours)
        ax.bar_label(bars)
        plt.xlabel("Years")
        plt.ylabel("Fours")
        st.pyplot(fig)

    # Year wise performance of player
    st.header("Year Wise Performance")
    years, year_wise_runs = helper.runs_per_year(option)
    seasons = [str(year) for year in years]
    fig, ax = plt.subplots()
    plt.xticks(rotation='vertical')
    bars = ax.bar(seasons, year_wise_runs)
    ax.bar_label(bars)
    plt.xlabel("Years")
    plt.ylabel("Runs")
    st.pyplot(fig)


    ## Bowling Statistics
    if total_wickets > 0:
        st.title("Bowling Statistics")
        years, year_wise_wickets = helper.total_number_of_wickets(option)
        seasons = [str(year) for year in years]
        fig, ax = plt.subplots()

        plt.xticks(rotation='vertical')
        bars = ax.bar(seasons, year_wise_wickets)
        ax.bar_label(bars)
        plt.xlabel("Years")
        plt.ylabel("Wickets")
        st.pyplot(fig)

    # over per runs Analysis
    ipl_seasons = [year for year in range(2008,2025)]
    st.header("Over wise analysis")
    over_wise_data = helper.over_wise_stats(option)
    fig, ax = plt.subplots()
    sns.heatmap(over_wise_data, annot=True, cmap='hot')
    ax.set_yticks([i for i in range(len(ipl_seasons))])
    ax.set_yticklabels([season for season in ipl_seasons], rotation=0)
    ax.set_title("Over-wise analysis of " + option)
    ax.set_xlabel("Overs")
    ax.set_ylabel("IPL Season")
    st.pyplot(fig)
