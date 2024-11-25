import streamlit as st


class SWTest:
    def __init__(self, pronouns):

        # Streamlit app layout
        st.title("Test Your Knowledge")

        # Create input fields for each pronoun
        for pronoun, (sentence, translation) in pronouns.items():
            st.write(translation)  # Show English translation

            user_answer = st.text_input(sentence, key=pronoun)
            if user_answer:
                if user_answer.strip().lower() == pronoun.lower():
                    st.success(f"Correct! The answer is '{pronoun}'.")
                else:
                    st.error(f"Incorrect! The correct answer is '{pronoun}'.")


