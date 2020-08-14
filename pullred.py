#! python3
import praw
import pandas as pd

reddit = praw.Reddit(client_id='X9IB4gITcE_UDg', \
                     client_secret='35ZjTEHOGXGf2wYXx8OBwkekz24', \
                     user_agent='nithsapi', \
                     username='number2inqueue', \
                     password='Theboynextdoor25!')

subreddit = reddit.subreddit('all')

top_subreddit = subreddit.top(limit=500)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)

topics_dict = { "title":[], 
                "score":[], 
                "id":[], 
                "url":[], 
                "comms_num": [], 
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["body"].append(submission.selftext)


topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('FILENAME.csv', index=False) 


