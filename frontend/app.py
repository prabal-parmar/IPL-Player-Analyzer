import streamlit as st
import helper
import pandas as pd 

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
