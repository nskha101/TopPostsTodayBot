#! python3
import praw
import pandas as pd

def pullredall():
    #reddit = -- use praw here to sign in. 

    subreddit = reddit.subreddit('all')

    top_subreddit = subreddit.top("day", limit=200)

    

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
    return topics_dict


