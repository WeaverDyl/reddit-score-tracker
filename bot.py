import praw, csv, time

def authenticate():
    """Logs into Reddit through PRAW so data collection can start."""
    reddit = praw.Reddit('upvotetrack', user_agent="Score tracker")
    return reddit

def run(reddit, submission_url):
    try:
        submission = reddit.submission(url=submission_url)
        with open('score_history.csv', 'w', newline='') as score_file:
            writer = csv.writer(score_file)
            writer.writerow(["Time", "Score"]) # Write column names

            while True:
                writer.writerow([time.time(), submission.score])
                time.sleep(1)
    except TypeError:
        print("Invalid URL provided.")

if __name__ == "__main__":
    reddit = authenticate()
    url = None
    run(reddit, url)