# transcript/tests.py
#
# Tests for transcripts.py

import unittest
from pathlib import Path
from transcripts import getTranscriptText

racoon_text = "the raccoons know one whole world is garbage two also garbage is delicious "

class TranscriptsTests(unittest.TestCase):
    def test_id(self):
        self.assertEqual(getTranscriptText("wNTGYSG-SFk"), racoon_text)
    
    def test_playlist_link(self):
        self.assertEqual(getTranscriptText("https://www.youtube.com/watch?v=wNTGYSG-SFk&list=PL0-euOPmh12FELJwDVeWDGV7cinZBIIqF&index=2&ab_channel=GianniMatragrano"), racoon_text)
    
    def test_short_link(self):
        self.assertEqual(getTranscriptText("https://youtu.be/wNTGYSG-SFk?si=fFklBybQKpFYPvnT"), racoon_text)

    def test_shorts(self):
        # Testing #shorts on YouTube
        self.assertEqual(getTranscriptText("https://www.youtube.com/watch?v=B0X3xburLxo&list=LL&index=4&ab_channel=PirateSoftware"),
                         "uh this is all the knowledge that I have it's what skills should you need fun fact you don't need any you don't need to be amazing artist amazing musician amazing programmer there is no best engine that doesn't exist it's easy to build a team you can do that it's easy to pick a genre for the kind of game that you want to make and why you should pick those types of games you can Finance your game and I have a whole bunch of different options for financing this I have marketing stuff for how you can Market these things I've got where you should launch your game in here if you want this knowledge it's free for you I also run multiple game jams a year the next one's going to be in January so if you need a more structured environment where you like need someone to tell you what kind of theme you should do and you need to come up with ideas out of that and when I run those there are cash prizes for it so the winners get cash prizes so they can upload their game to steam and continue their game Development Career like off and running and that's it that's what it is ")

    def test_expletives(self):
        self.assertEqual(getTranscriptText("dpTte1scAm0"), 
                         "quiet down listen immediately if there's if it's like a ton of noise that a bunch of kids like you just walk it and you just go like and they'll all go [ __ ] and they'll sit down and be like and then you have your attention that worked every [ __ ] time ")
                    
    def test_timestamp_link(self):
        self.assertEqual(getTranscriptText("https://youtu.be/ugn5kYgIqXo?si=9uG10Nhnfe59cYDo&t=11"),
                         "there were so many times I felt so defeated from programming I'm stuck on a bug I don't understand a concept I can't finish this task I'm going to get fired I wanted to quit and give up entirely that was until I learned this concept laugh at your code that's it you see whenever we laugh we release a bit of dopamine in our brain this activates and relieves our stress response which in turn lets us focus better and gives us energy it lets us continue working with a much calmer State of Mind this is popular in sports teams in the Army when the situation gets tough and someone cracks a joke it can really help energize the environment so whenever I'm too stressed out from programming I'll take a short 5-minute break watch some clips of my favorite comedians and once I'm done laughing and my mood's brightened I'm looking at the same problem with much more energy this is why I put a lot of memes in my videos because I know some of you guys are really stressed out and I want to do my best to help thank you for your time I am big box ")
    
    def test_1hr_podcast(self):
        text = ""

        with open("./test_outputs/rogan_podcast.txt") as file:
            text = file.readline()

        self.assertEqual(getTranscriptText("https://www.youtube.com/watch?v=jreBmGkuEBc&ab_channel=TheoVon"),
                         text)


if __name__ == "__main__":
    unittest.main()