import streamlit as st
import pandas as pd
from swtest import SWTest
from swtable import SWTable
from swquiz import SWQuiz
from swpronouns import SWPronouns


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

if pronouns_selectbox=="Independent":
    desc = "Independent pronouns in Swahili stand alone and are used for emphasis or clarity."
elif pronouns_selectbox=="Subject Concord Positive" or pronouns_selectbox=="Subject Concord Negative":
    desc = "Subject concords are prefixes attached to verbs to indicate the subject of the sentence. They change depending on whether the sentence is positive or negative."
elif pronouns_selectbox=="Object Concord":
    desc = "Object concords are prefixes attached to verbs to indicate the object of the sentence."
elif pronouns_selectbox=="Possessive":
    desc = "Possessive pronouns indicate ownership and are attached to the noun they modify."
st.write(desc)

# Accordion for the pronoun table
SWTable(pronouns)

SWQuiz(pronouns)

if pronouns_selectbox == "Independent":
    swquiz = SWTest()
