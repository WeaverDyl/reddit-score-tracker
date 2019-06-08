import praw

def authenticate():
    """Logs into Reddit through PRAW so data collection can start."""
    reddit = praw.Reddit('phrasetrend', user_agent="Phrase trend detector")
    return reddit

def run(reddit):
    pass

if __name__ == "__main__":
    reddit = authenticate()
    run(reddit)