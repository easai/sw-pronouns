import streamlit as st


class SWDesc:
    def __init__(self, pronouns_selectbox):
        if pronouns_selectbox == "Independent":
            desc = "Independent pronouns in Swahili stand alone and are used for emphasis or clarity."
        elif pronouns_selectbox == "Subject Concord Positive" or pronouns_selectbox == "Subject Concord Negative":
            desc = "Subject concords are prefixes attached to verbs to indicate the subject of the sentence. They change depending on whether the sentence is positive or negative."
        elif pronouns_selectbox == "Object Concord":
            desc = "Object concords are prefixes attached to verbs to indicate the object of the sentence."
        elif pronouns_selectbox == "Possessive":
            desc = "Possessive pronouns indicate ownership and are attached to the noun they modify."
        st.write(desc)
