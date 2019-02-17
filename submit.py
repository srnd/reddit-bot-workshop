import praw
reddit = praw.Reddit('codeday_bot')
subreddit = reddit.subreddit('codeday')
title = "CodeDay is awesome!"
selftext = "It is so cool"
subreddit.message(title, 'test')