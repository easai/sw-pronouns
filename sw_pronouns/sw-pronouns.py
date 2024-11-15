import streamlit as st
import pandas as pd 

# Define the personal pronouns in English and Swahili along with audio links
pronouns = {
    "1st Person": {
        "Singular": {
            "text": "I (Mimi)",
            "answer": "Mimi",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Sw-ke-mimi.flac"  
        },
        "Plural": {
            "text": "We (Sisi)",
            "answer": "Sisi",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/4/45/Sw-ke-sisi.flac"  
        }
    },
    "2nd Person": {
        "Singular": {
            "text": "You (Wewe)",
            "answer":"Wewe",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Sw-ke-wewe.flac"  
        },
        "Plural": {
            "text": "You (Ninyi)",
            "answer": "Ninyi",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/2/28/Sw-ke-ninyi.flac"  
        }
    },
    "3rd Person": {
        "Singular": {
            "text": "He (Yeye - mume) / She (Yeye - mke)",
            "answer": "Yeye",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/6/64/Sw-ke-yeye.flac"  
        },
        "Plural": {
            "text": "They (Wao)",
            "answer": "Wao",
            "audio": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Sw-ke-wao.flac"  
        }
    }
}

def clear_inputs():
    for person, forms in pronouns.items():
        col1, col2 = st.columns(2)
        
        with col1:
            st.session_state[f"singular_{person}"] = ''
        with col2:
            st.session_state[f"plural_{person}"] = ''

pronouns_selectbox = st.sidebar.selectbox( "Pronouns", ("Independent", "Subject Concord Positive", "Subject Concord Negative", "Possessive"), on_change=clear_inputs)

if pronouns_selectbox=="Subject Concord Positive":
    pronouns = {
        "1st Person": {
            "Singular": {
                "text": "I (ni-)",
                "answer": "ni",
                "audio": ""  
            },
            "Plural": {
                "text": "We (tu-)",
                "answer": "tu",
                "audio": ""  
            }
        },
        "2nd Person": {
            "Singular": {
                "text": "You (u-)",
                "answer": "u",
                "audio": ""  
            },
            "Plural": {
                "text": "You (mu-)",
                "answer": "mu",
                "audio": ""  
            }
        },
        "3rd Person": {
            "Singular": {
                "text": "He/She (yu-)",
                "answer": "yu",
                "audio": ""  
            },
            "Plural": {
                "text": "They (wa-)",
                "answer": "wa",
                "audio": ""  
            }
        }
    }
elif pronouns_selectbox=="Subject Concord Negative":
    pronouns = {
        "1st Person": {
            "Singular": {
                "text": "I (si-)",
                "answer": "si",
                "audio": ""  
            },
            "Plural": {
                "text": "We (hatu-)",
                "answer":"hatu",
                "audio": ""  
            }
        },
        "2nd Person": {
            "Singular": {
                "text": "You (hu-)",
                "answer": "hu",
                "audio": ""  
            },
            "Plural": {
                "text": "You (ham-)",
                "answer": "ham",
                "audio": ""  
            }
        },
        "3rd Person": {
            "Singular": {
                "text": "He/She (ha-)",
                "answer": "ha",
                "audio": ""  
            },
            "Plural": {
                "text": "They (hawa-)",
                "answer": "hawa",
                "audio": ""  
            }
        }
    }
elif pronouns_selectbox=="Possessive":
    pronouns = {
        "1st Person": {
            "Singular": {
                "text": "I (-angu)",
                "answer": "angu",
                "audio": ""  
            },
            "Plural": {
                "text": "We (-etu)",
                "answer":"etu",
                "audio": ""  
            }
        },
        "2nd Person": {
            "Singular": {
                "text": "You (-ako)",
                "answer": "ako",
                "audio": ""  
            },
            "Plural": {
                "text": "You (-enu)",
                "answer": "enu",
                "audio": ""  
            }
        },
        "3rd Person": {
            "Singular": {
                "text": "He/She (-ake)",
                "answer": "ake",
                "audio": ""  
            },
            "Plural": {
                "text": "They (-ao)",
                "answer": "ao",
                "audio": ""  
            }
        }
    }

# Streamlit app title
st.title("Swahili Pronouns Quiz with Audio")

audio_html = f"""
<style>
.stAudio {{
    height: 30px; 
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
            correct_singular = forms["Singular"]["answer"]
            if singular_answer.strip().lower() == correct_singular.lower():
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect (Correct: {correct_singular})")
        if forms["Singular"]["audio"]:
            st.audio(forms["Singular"]["audio"])

    with col2:
        plural_answer = st.text_input(f"{person} Plural", key=f"plural_{person}")
        if plural_answer:
            correct_plural = forms["Plural"]["answer"]
            if plural_answer.strip().lower() == correct_plural.lower():
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect (Correct: {correct_plural})")
        
        # Play audio for plural
        if forms["Plural"]["audio"]:
            st.audio(forms["Plural"]["audio"])


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

