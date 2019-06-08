import praw, csv, time, sys

def authenticate():
    """Logs into Reddit through PRAW so data collection can start."""
    try:
        reddit = praw.Reddit('upvotetrack', user_agent="Score tracker")
        return reddit
    except praw.exceptions.ClientException:
        print("Invalid praw.ini config.")
        sys.exit(1)

def run(reddit, submission_url):
    try:
        with open('score_history.csv', 'w', newline='') as score_file:
            writer = csv.writer(score_file)
            writer.writerow(["Time", "Score"]) # Write column names

            while True:
                submission = reddit.submission(url=submission_url)
                writer.writerow([time.time(), submission.score])
                time.sleep(10)
    except TypeError:
        print("Invalid URL provided.")
        sys.exit(1)

if __name__ == "__main__":
    reddit = authenticate()
    url = "https://www.reddit.com/r/formula1/comments/bybint/sebastian_vettel_takes_pole_position_at_the_2019/"
    run(reddit, url)