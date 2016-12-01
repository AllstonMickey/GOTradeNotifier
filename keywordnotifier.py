import time
import praw

# Configure this section yourself
USERAGENT = "XXXXX:vX.X (by /u/XXXXX)"
BOT_USERNAME = "XXXXX"
BOT_PASSWORD = "XXXXX"
RECEIVING_USERNAME = "XXXXX"
SUBREDDIT = "XXXXX"
KEYWORD = "XXXXX".lower()

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

* implement XML file usage to store users, their keywords, and the found submissions

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
            haveChecked.append(submission.id) # append the submission to the list
            sendPM(reddit, submission) # notify the user that a thread was made

def sendPM(reddit, submission):
    message_ = "Thread containing {0} found! {1}".format(KEYWORD, submission.permalink)
    reddit.send_message(RECEIVING_USERNAME, "Keyword \"{0}\" Found!", message_);

if __name__ == "__main__":
    main()
