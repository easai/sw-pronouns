import streamlit as st
import pandas as pd
from swtest import SWTest
from swtable import SWTable
from swquiz import SWQuiz
from swpronouns import SWPronouns
from swdesc import SWDesc


def clear_inputs():
    for person, forms in pronouns.items():
        col1, col2 = st.columns(2)

        with col1:
            st.session_state[f"singular_{person}"] =""
        with col2:
            st.session_state[f"plural_{person}"] = ''

pronouns_selectbox = st.sidebar.selectbox("Pronouns Quizzes", ("Independent", "Subject Concord Positive",
                                          "Subject Concord Negative", "Object Concord", "Possessive"), on_change=clear_inputs)

pronouns = SWPronouns(pronouns_selectbox).pronouns

# Streamlit app title
st.title("Swahili Pronouns")
st.write("Challenge yourself with our Swahili pronouns quizzes and tests, and see how much you know! The app can test various aspects of Swahili pronouns, including independent, subject concord positive, subject concord negative, object concord, and possessive forms.")
st.subheader(pronouns_selectbox)

SWDesc(pronouns_selectbox)

# Accordion for the pronoun table
SWTable(pronouns)

SWQuiz(pronouns)

if pronouns_selectbox == "Independent":
    swquiz = SWTest()
