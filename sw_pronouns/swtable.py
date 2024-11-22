import streamlit as st
import pandas as pd

class SWTable:
    def __init__(self, pronouns):
        # Accordion for the pronoun table
        with st.expander("Show Pronoun Table"):
            # Create a DataFrame for the pronouns
            pronoun_data = []
            for person, forms in pronouns.items():
                pronoun_data.append([person, forms["Singular"]["text"], forms["Plural"]["text"]])
            
            # Define column names
            columns = ["Person", "Singular", "Plural"]
            
            # Create a DataFrame
            df = pd.DataFrame(pronoun_data, columns=columns)
            
            # Display the pronoun table without index
            st.dataframe(df, use_container_width=True, hide_index=True)