# summarizer.py
#
# The main summarization module for summarizing text.
from transformers import pipeline

def summarize(text: str) -> str:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    ARTICLE = """
        A server room is a room, usually air-conditioned, devoted to the continuous operation of computer servers. An entire building or station devoted to this purpose is a data center.
        The computers in server rooms are usually headless systems that can be operated remotely via KVM switch or remote administration software, such as Secure Shell, VNC, and remote desktop.[1][2][3][4][5]
        Climate is one of the factors that affects the energy consumption and environmental impact of a server room. In areas where climate favours cooling and an abundance of renewable electricity, the environmental effects will be more moderate. Thus, countries with favourable conditions such as Canada,[6] Finland,[7] Sweden,[8] and Switzerland[9] are trying to attract companies to site server rooms there.
    """

    print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))

if __name__ == '__main__':
    summarize('lol')