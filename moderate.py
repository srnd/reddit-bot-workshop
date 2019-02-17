import praw
reddit = praw.Reddit('codeday_bot')
subreddit = reddit.subreddit('codeday')
bad_words = ['jerk','stupidface','stupid','dummy','idiot','loser']
very_bad_words = ['heck','poopyhead','i like php']
for comment in subreddit.stream.comments():
	print(comment.body)
	if comment.banned_by: #Returns string if comment has been removed, None if it has not. https://www.reddit.com/r/redditdev/comments/2eo3po/praw_can_you_check_if_a_comment_has_been_removed/ck1bqrs/
		print('Comment already removed')
	elif any(word in comment.body.lower() for word in very_bad_words): #https://stackoverflow.com/a/6531704/4991969
		comment.reply('#BE FRIENDLY AND SUPPORTIVE')
		comment.mod.remove()
	elif any(word in comment.body.lower() for word in bad_words):
		comment.reply('#BE FRIENDLY AND SUPPORTIVE')
		comment.mod.remove()
		subreddit.banned.add(comment.author.name) #Does not work on moderators, however no error is thrown and the resulting message won't be sent. See https://github.com/praw-dev/praw/issues/1026
		title = 'report'
		body = comment.author.name + ' was not being friendly and supportive'
		subreddit.message(title,body)