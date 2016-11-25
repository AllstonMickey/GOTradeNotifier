import time
import praw

# Configure this section yourself
USERAGENT = "XXXXX:vX.X (by /u/XXXXX)"
USERNAME = "XXXXX"
PASSWORD = "XXXXX"
SUBREDDIT = "XXXXX"
KEYWORD = "XX".lower()


def main():
    r = praw.Reddit(user_agent = USERAGENT)
    r.login(USERNAME, PASSWORD);
    submissions = r.get_subreddit(SUBREDDIT).get_new(limit=10)
    
    haveChecked = []
    checkSubmissions(r, haveChecked)

"""
1. read inbox
    a. get the user and add them to an array
    b. each message from that user is another keyword, add the word into an array specific to the user
2. scan the new posts
    a. check if the submission contains the keyword
        i) if it does, relate the permalink to the keyword in the user's database
           !) add the permalink to haveChecked specific to the user's keyword
        ii) if not, continue to the next submission
"""

def hasKeyword(content, keyword):
    result = content.find(str, 0, len(string))
    if result != -1:
        return True
    
def checkSubmissions(reddit, checked):
    submissions = reddit.get_subreddit(SUBREDDIT).get_new(limit=10)
    for submission in submissions:
        title_ = submission.title.encode("utf8")
        text_ = submission.selftext.encode("utf8")
        if submission.id not in haveChecked and \
           (hasKeyword(title_.lower, KEYWORD) or hasKeyword(text_.lower(), KEYWORD)):
            haveChecked.append(submission.id)
            sendPM(reddit, submission)

def sendPM(reddit, submission):
    message_ = "Thread containing %s found! %s" % (KEYWORD, submission.permalink)
    # still build on this

if __name__ == "__main__":
    main()
