# summarizer.py
#
# The main summarization module for summarizing text.
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.utils import get_stop_words
from punctuator import Punctuator
from pathlib import Path
import nltk

LANGUAGE = "english"

# TODO: Punctuation

def parse_txt(text: str, sentence_count: int = 2) -> str:
    """
    Summarizes text into (sentence_count) sentences.

    Parameters -----
    text (str): Transcript text.
    sentence_count (int): The number of sentences to condense into.

    Return -----
    A str containing a summary of the transcripts.
    """
    dwn_dir = Path(__file__).parent / "data"
    nltk.download('punkt', dwn_dir) 

    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    ret_txt = ""

    for sentence in summarizer(parser.document, sentence_count):
        ret_txt += str(sentence) + " "

    return ret_txt

