import praw, csv, time, sys
from prawcore import PrawcoreException

def authenticate():
    """Logs into Reddit through PRAW so data collection can start."""
    try:
        reddit = praw.Reddit('upvotetrack', user_agent="Score tracker")
        return reddit
    except praw.exceptions.ClientException:
        raise

def run(reddit, submission_url):
    print("Starting!")
    try:
        with open('score_history.csv', 'w', newline='') as score_file:
            writer = csv.writer(score_file)
            writer.writerow(["Time", "Score"]) # Write column names

            while True:
                submission = reddit.submission(url=submission_url)
                writer.writerow([time.time(), submission.score])
                print(f"Wrote {time.time()}, {submission.score}")
                time.sleep(10)
    except PrawcoreException as e:
        raise e
    except TypeError:
        raise

if __name__ == "__main__":
    try:
        reddit = authenticate()
        url = ""
        run(reddit, url)
    except praw.exceptions.ClientException:
        print("There's an error in your `praw.ini` file.")
    except PrawcoreException as e:
        print("Error:", e, ". Check your link or `praw.ini` file.")
    except TypeError:
        print("Invalid URL provided.")
    # set up args for url
