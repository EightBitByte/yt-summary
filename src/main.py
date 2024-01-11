# main.py
#
# Application main.

from transcript import transcripts
from summary import summarizer

def get_video_summary(vid: str) -> str:
    """
    Runs the YouTube video's URL/ID through the transcript, summary pipeline.

    Parameters -----
    vid (str): The YouTube URL or video ID of the target video.

    Return -----
    A str containing a summary of the transcripts.
    """
    captions = transcripts.getTranscriptText(vid)
    summary = summarizer.parse_txt(captions)

    return summary

if __name__ == '__main__':
    vid_id = "ugn5kYgIqXo"

    print(get_video_summary(vid_id))
