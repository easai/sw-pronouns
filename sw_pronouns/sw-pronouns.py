import streamlit as st
import pandas as pd
from test import PronounTest
from table import PronounTable
from quiz import PronounQuiz
from data import PronounData
from const import TITLE, DESC

st.set_page_config(
    page_title=TITLE,
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="auto",
)


def clear_ending_with_input():
    for key in list(st.session_state.keys()):
        if key.endswith("_input"):
            st.session_state[key] = ""


pronounData = PronounData()
menu = pronounData.get_menu()
selected_item = st.sidebar.selectbox(
    TITLE, menu, on_change=clear_ending_with_input)
menuIndex = menu.index(selected_item)
table = pronounData.get_table(menuIndex)

# Streamlit app title
st.title(TITLE)
st.write(DESC)
st.subheader(selected_item)

# Side menu
st.write(pronounData.get_desc(menuIndex))

# Accordion for the pronoun table
PronounTable(table)

# Pronouns table quiz
PronounQuiz(table)

# Fill-in-the-box test
test = pronounData.get_test(menuIndex)
if test != "":
    PronounTest(test)
