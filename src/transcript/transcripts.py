# transcript/transcripts.py
#
# A command line interface module centering around getting the text of the video from URL or ID.

from unicodedata import normalize
from youtube_transcript_api import YouTubeTranscriptApi 

def get_transcript_text(link: str) -> str:
    """
    Returns a concatenated string of the transcripted text
    from the video provided.

    Preconditions -----
    TODO: Change the below precondition to check validity.
    Link is a valid YouTube URL or video ID 
    Link is non-empty

    Parameters -----
    link (str): The YouTube URL or video ID of the target video.

    Return -----
    A str containing all of the transcripted text.
    """

    format_link = link

    # If our link isn't already just the ID
    if len(format_link) > 11:
        parts = link.split('/')

        for part in parts:
            # If the link is a "header" link
            if "watch?v=" in part:
                format_link = part[8:19]
                break
            # If the link is shortened
            if "?si=" in part:
                format_link = part[0:11]
                break

    transcript_json = YouTubeTranscriptApi.get_transcript(format_link)

    text = ""

    for dictionary in transcript_json:
        text += dictionary['text'] + " "

    return normalize('NFKD', text)
