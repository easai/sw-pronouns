import streamlit as st


class SWTest:
    def __init__(self):

        # Define a list of pronouns with corresponding sentences and their English translations
        pronouns = {
            "Mimi": ("___ ni mwanafunzi.", "I am a student."),
            "Wewe": ("___ ni daktari.", "You are a doctor."),
            "Yeye": ("___ ni mwalimu.", "He/She is a teacher."),
            "Sisi": ("___ tunapenda kujifunza.", "We love to learn."),
            "Ninyi": ("___ mnaweza kusaidia.", "You all can help."),
            "Wao": ("___ wanacheka.", "They are laughing.")
        }

        # Streamlit app layout
        st.title("Swahili Pronouns Quiz")

        # Create input fields for each pronoun
        for pronoun, (sentence, translation) in pronouns.items():
            st.write(translation)  # Show English translation

            user_answer = st.text_input(sentence, key=pronoun)
            if user_answer:
                if user_answer.strip().lower() == pronoun.lower():
                    st.success(f"Correct! The answer is '{pronoun}'.")
                else:
                    st.error(f"Incorrect! The correct answer is '{pronoun}'.")


