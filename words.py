
import random
import stanza
from tkinter import messagebox as msg

stanza.download("cs")
stanza.download("en")
# Open the pipes at the initialization and keep them open for faster word selecting
nlp_cs = stanza.Pipeline("cs")
nlp_en = stanza.Pipeline("en")

def get_random_word(length: int, language: str) -> str:
    """
    Get random word from a text file (from word_list folder).

    Files are named as languages (english.txt)
    """
    # Set path to word list based on language
    if language == "English":
        path = "word_lists/english.txt"
    elif language == "Czech":
        path = "word_lists/czech.txt"
    else:
        raise Exception("Unsupported language")
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            words = file.readlines()
            # Remove whitespace characters
            words = [word.strip() for word in words]
            
            if not words:
                # Empty file
                return None
            
            # Loop for finding right word
            while(True):
                word = random.choice(words)

                if len(word) == length and is_noun(word, language):
                    return word
    
    except FileNotFoundError:
        msg.showerror("Words file error", f"Error: The file '{path}' was not found.")
        return None
    
    except IOError:
        msg.showerror("Words file error", f"Error: Could not read from the file '{path}'.")
        return None
    
    finally:
        file.close()



def is_noun(word: str, language: str) -> bool:
    """
    Checks if the word is noun.
    """

    if language == "English":
        analyze = nlp_en(word)
        return analyze.sentences[0].words[0].upos == "NOUN"
    
    elif language == "Czech":
        analyze = nlp_cs(word)
        # Check for noun and czech "pád"
        return analyze.sentences[0].words[0].upos == "NOUN" and "Case=Nom" in analyze.sentences[0].words[0].feats
    
    else:
        raise Exception("Unsupported language.")