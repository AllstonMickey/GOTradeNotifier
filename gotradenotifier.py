import praw
user_agent = "GOTradeNotifier:v0.1 (by /u/GOTradeNotifier)"
r = praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit("globaloffensivetrade").get_new(limit=5)

i = 1
for submission in subreddit:
    print ">>>>>>>>>> START OF POST ", i, " >>>>>>>>>>"
    print "Title: ", submission.title.encode("utf8")
    print "Text: ", submission.selftext.encode("utf8")
    print "Score: ", submission.score
    print ">>>>>>>>>> END OF POST ", i, "<<<<<<<<<<\n\n"
    i += 1
