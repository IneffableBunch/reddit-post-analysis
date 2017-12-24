import praw
import textwrap
import tabulate
from datetime import datetime

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

table = []
for submission in reddit.subreddit('all-The_Donald').top(time_filter="hour", limit=20):
    if submission.num_comments < 10:
        table.append([submission.shortlink,
                      textwrap.fill(submission.title, width=80),
                      submission.score,
                      submission.num_comments,
                      str(datetime.utcnow() - datetime.utcfromtimestamp(submission.created_utc))[2:4] + " minutes ago"])

table.sort(key=lambda x: x[2], reverse=True)

print(tabulate.tabulate(table,
                        headers=["Link", "Title", "Score", "Comments", "Time Posted"],
                        tablefmt="rst",
                        numalign="left"))
