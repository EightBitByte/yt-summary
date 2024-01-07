# main.py
#
# Application main.

from transcript import transcripts
from summary import summarizer

def get_video_summary(vid: str) -> str:
    captions = transcripts.getTranscriptText(vid)
    summary = summarizer.summarize(captions)

    return summary

if __name__ == '__main__':
    vid_id = "ugn5kYgIqXo"

    print(get_video_summary(vid_id))