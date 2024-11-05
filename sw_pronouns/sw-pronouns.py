import streamlit as st

# Define the personal pronouns in English and Swahili
pronouns = {
    "1st Person": {
        "Singular": "I (Mimi)",
        "Plural": "We (Sisi)"
    },
    "2nd Person": {
        "Singular": "You (Wewe)",
        "Plural": "You (Ninyi)"
    },
    "3rd Person": {
        "Singular": "He (Yeye - mume) / She (Yeye - mke)",
        "Plural": "They (Wao)"
    }
}

# Streamlit app title
st.title("Swahili Pronouns Quiz")

# Loop through the pronouns to create inputs
for person, forms in pronouns.items():
    col1, col2 = st.columns(2)
    
    with col1:
        singular_answer = st.text_input(f"{person} Singular", key=f"singular_{person}")
        if singular_answer:
            correct_singular = "Mimi" if person == "1st Person" else "Wewe" if person == "2nd Person" else "Yeye"
            if singular_answer.strip().lower() == correct_singular.lower():
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect (Correct: {correct_singular})")
    
    with col2:
        plural_answer = st.text_input(f"{person} Plural", key=f"plural_{person}")
        if plural_answer:
            correct_plural = "Sisi" if person == "1st Person" else "Ninyi" if person == "2nd Person" else "Wao"
            if plural_answer.strip().lower() == correct_plural.lower():
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect (Correct: {correct_plural})")

# Note: No submit button is needed since feedback is shown immediately