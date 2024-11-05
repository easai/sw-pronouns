import streamlit as st

# Define the personal pronouns in English and Swahili along with audio links
pronouns = {
    "1st Person": {
        "Singular": {
            "text": "I (Mimi)",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Sw-ke-mimi.flac"  # Replace with your actual FLAC file URL
        },
        "Plural": {
            "text": "We (Sisi)",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/4/45/Sw-ke-sisi.flac"  # Replace with your actual FLAC file URL
        }
    },
    "2nd Person": {
        "Singular": {
            "text": "You (Wewe)",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Sw-ke-wewe.flac"  # Replace with your actual FLAC file URL
        },
        "Plural": {
            "text": "You (Ninyi)",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/2/28/Sw-ke-ninyi.flac"  # Replace with your actual FLAC file URL
        }
    },
    "3rd Person": {
        "Singular": {
            "text": "He (Yeye - mume) / She (Yeye - mke)",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/6/64/Sw-ke-yeye.flac"  # Replace with your actual FLAC file URL
        },
        "Plural": {
            "text": "They (Wao)",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Sw-ke-wao.flac"  # Replace with your actual FLAC file URL
        }
    }
}

# Streamlit app title
st.title("Swahili Pronouns Quiz with Audio")

audio_html = f"""
<style>
.stAudio {{
    height: 30px; /* Adjust the height as needed */
}}
</style>
"""
st.markdown(audio_html, unsafe_allow_html=True)


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
        st.audio(forms["Singular"]["audio"])

    with col2:
        plural_answer = st.text_input(f"{person} Plural", key=f"plural_{person}")
        if plural_answer:
            correct_plural = "Sisi" if person == "1st Person" else "Ninyi" if person == "2nd Person" else "Wao"
            if plural_answer.strip().lower() == correct_plural.lower():
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect (Correct: {correct_plural})")
        
        # Play audio for plural
        st.audio(forms["Plural"]["audio"])

# Note: No submit button is needed since feedback is shown immediately