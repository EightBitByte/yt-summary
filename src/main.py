# main.py
#
# Application main.

from transcript import transcripts

if __name__ == '__main__':
    vid_id = "imH01FvTssc"

    print(transcripts.getTranscriptText(vid_id))