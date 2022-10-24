# Wikipedia Speedrun

This piece of code was a way for me to:
- practice search algorithms I learned
- learn how to use API (specifically MediaWiki API) to access other apps' data

A project simply to guide my into a new topic while also using previous knowledge of data structures and Python.

My process:
- First and foremost, I researched what I needed to download prior to working with the MediaWiki API (installing pip files).
- I started with researching MediaWiki's documentation to see the different kinds of requests and information they provide.
- Then, after I brushed up my Python knowledge to make a simple class to hold the requests.
- Following this, I researched what kind of structure Wikipedia has and quickly noticed it is a graph of article linking each other with loops.
- I looked at my previous implementation done of a search through graph structures and implemented it in Python, making sure that the bot doesn't infinitely loop through certain articles that inform each other.
- The alogrithm creates an arbitrary arity tree of pages that goes through the first path, filling the tree as the bot looks through more articles, each one having its own links.
- Due to Wikipedia's intricately connected web of articles, two articles that seemingly have no common path are linked by my bot.

Things to consider:
- This algorithm is not efficient, taking a lot of space and time. It is one thing I would change on another version of this code.
