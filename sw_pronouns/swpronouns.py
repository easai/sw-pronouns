class SWPronouns:
    def __init__(self, selection):
        self.selection = selection
        # Define the personal pronouns in English and Swahili along with audio links
        self.pronouns = {
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
                    "answer": "Wewe",
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

        if selection == "Subject Concord Positive":
            self.pronouns = {
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
        elif selection == "Subject Concord Negative":
            self.pronouns = {
                "1st Person": {
                    "Singular": {
                        "text": "I (si-)",
                        "answer": "si",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (hatu-)",
                        "answer": "hatu",
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
        elif selection == "Possessive":
            self.pronouns = {
                "1st Person": {
                    "Singular": {
                        "text": "I (-angu)",
                        "answer": "angu",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (-etu)",
                        "answer": "etu",
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
        elif selection == "Object Concord":
            self.pronouns = {
                "1st Person": {
                    "Singular": {
                        "text": "I (-ni-)",
                        "answer": "ni",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (-tu-)",
                        "answer": "tu",
                        "audio": ""
                    }
                },
                "2nd Person": {
                    "Singular": {
                        "text": "You (-ku-)",
                        "answer": "ku",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "You (-wa-)",
                        "answer": "wa",
                        "audio": ""
                    }
                },
                "3rd Person": {
                    "Singular": {
                        "text": "He/She (-m-)",
                        "answer": "m",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "They (-wa-)",
                        "answer": "wa",
                        "audio": ""
                    }
                }
            }

    def test(self):
        lst = {}
        if self.selection == "Independent":
            lst = {
                "Mimi": ("___ ni mwanafunzi.", "I am a student."),
                "Wewe": ("___ ni daktari.", "You are a doctor."),
                "Yeye": ("___ ni mwalimu.", "He/She is a teacher."),
                "Sisi": ("___ tunapenda kujifunza.", "We love to learn."),
                "Ninyi": ("___ mnaweza kusaidia.", "You all can help."),
                "Wao": ("___ wanacheka.", "They are laughing.")
            }
        elif self.selection == "Subject Concord Positive":
            lst = {
                "Ni": ("__naenda sokoni.", "I am going to the market."),
                "U": ("_nakula chakula.", "You are eating food."),
                "A": ("_nasoma kitabu.", "He/She is reading a book."),
                "Tu": ("__nacheza mpira.", "We are playing football."),
                "M": ("_napika chakula.", "You all are cooking food."),
                "Wa": ("__nakimbia haraka.", "They are running fast.")
            }
        elif self.selection == "Subject Concord Negative":
            lst = {
                "Si": ("__endi sokoni.", "I am not going to the market."),
                "Hu": ("__li chakula.", "You are not eating food."),
                "Ha": ("__somi kitabu.", "He/She is not reading a book."),
                "Hatu": ("____chezi mpira.", "We are not playing football."),
                "Ham": ("___piki chakula.", "You all are not cooking food."),
                "Hawa": ("____kimbii haraka.", "They are not running fast.")
            }
        return lst
