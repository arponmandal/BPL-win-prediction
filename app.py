import streamlit as st
import pandas as pd
import pickle

# Declaring the teams


#st.write("Made_By_Arpon_Mandal")
st.set_page_config(
    page_title="BPL Win Predictor",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
    <h2 style='text-align: center'>
    BPL Win Predictor
    </h2>
    <h6 style='text-align: center'>
    Made_By_Arpon_Mandal
    </h6>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style='text-align: center'>
    <a href='https://github.com/arponmandal/BPL-win-prediction' target='_blank'>https://github.com/arponmandal/BPL-win-prediction</a>
    <br />
    Follow me for more! <a href='https://www.facebook.com/arpon0007' target='_blank'> <img src="https://img.icons8.com/color/48/000000/facebook.png" height="30"></a><a href='https://github.com/arponmandal' target='_blank'><img src="https://img.icons8.com/fluency/48/000000/github.png" height="27"></a><a href='https://www.linkedin.com/in/arponmandal' target='_blank'><img src="https://img.icons8.com/fluency/48/000000/linkedin.png" height="30"></a> 
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("##")

teams = ['Comilla Victorians',
         'Fortune Barishal',
         'Chattogram Challengers',
         'Khulna Tigers',
         'Minister Dhaka',
         'Sylhet Sunrisers',
         'Rajshahi Royals',
         'Rangpur Rangers'
         ]

# declaring the venues

cities = ['Chattogram', 'Khulna', 'Dhaka', 'Sylhet']


pipe = pickle.load(open('pipe.pkl', 'rb'))
#st.title('BPL Win Predictor')


col1, col2 = st.columns(2)

with col1:
    battingteam = st.selectbox('Select the batting team', sorted(teams))

with col2:

    bowlingteam = st.selectbox('Select the bowling team', sorted(teams))


city = st.selectbox(
    'Select the city where the match is being played', sorted(cities))


target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')

with col4:
    overs = st.number_input('Overs Completed')

with col5:
    wickets = st.number_input('Wickets Fallen')


if st.button('Predict Probability'):

    runs_left = target-score
    balls_left = 120-(overs*6)
    wickets = 10-wickets
    currentrunrate = score/overs
    requiredrunrate = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team': [battingteam], 'bowling_team': [bowlingteam], 'city': [city], 'runs_left': [runs_left], 'balls_left': [
                            balls_left], 'wickets': [wickets], 'total_runs_x': [target], 'cur_run_rate': [currentrunrate], 'req_run_rate': [requiredrunrate]})

    result = pipe.predict_proba(input_df)
    lossprob = result[0][0]
    winprob = result[0][1]

    st.header(battingteam+"- "+str(round(winprob*100))+"%")

    st.header(bowlingteam+"- "+str(round(lossprob*100))+"%")
