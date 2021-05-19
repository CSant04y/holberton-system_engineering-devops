# 0x16. API advanced


<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png" alt="" style="">

## Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.
A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.
## Resources
**Read or watch**:
+ [Reddit API Documentation](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA)
+ [Query String](https://intranet.hbtn.io/rltoken/KtHEZIjOvJXYtufkJE1r4A)
## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/SKRGIFDOrTWPhgF4ZCZqpg), **without the help of Google**:
### General
+ How to read API documentation to find the endpoints you’re looking for
+ How to use an API with pagination
+ How to parse JSON results from an API
+ How to make a recursive API call
+ How to sort a dictionary by value
## Requirements
### General
+ Allowed editors: <code data-beeline-skip="true">vi`, <code data-beeline-skip="true">vim`, <code data-beeline-skip="true">emacs`
+ All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code data-beeline-skip="true">python3` (version 3.4.3)
+ All your files should end with a new line
+ The first line of all your files should be exactly <code data-beeline-skip="true">#!/usr/bin/python3`
+ Libraries imported in your Python files must be organized in alphabetical order
+ A <code data-beeline-skip="true">README.md` file, at the root of the folder of the project, is mandatory
+ Your code should use the <code data-beeline-skip="true">PEP 8` style
+ All your files must be executable
+ The length of your files will be tested using <code data-beeline-skip="true">wc`
+ All your modules should have a documentation (<code data-beeline-skip="true">python3 -c 'print(__import__("my_module").__doc__)'`)
+ You must use the Requests module for sending HTTP requests to the Reddit API


## 0. How many subs?
Write a function that queries the <a href="/rltoken/odMvR9obKnQCx5EaM6_YFA" title="Reddit API" target="_blank">Reddit API</a> and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Write a function that queries the [Reddit API](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:
+ Prototype: <code data-beeline-skip="true">def number_of_subscribers(subreddit)`
+ If not a valid subreddit, return 0.
+ NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```
wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
number_of_subscribers = __import__('0-subs').number_of_subscribers
if len(sys.argv) < 2:
print("Please pass an argument for the subreddit to search.")
else:
print("{:d}".format(number_of_subscribers(sys.argv[1])))
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
```


## 1. Top Ten
Write a function that queries the <a href="/rltoken/odMvR9obKnQCx5EaM6_YFA" title="Reddit API" target="_blank">Reddit API</a> and prints the titles of the first 10 hot posts listed for a given subreddit.

Write a function that queries the [Reddit API](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA) and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:
+ Prototype: <code data-beeline-skip="true">def top_ten(subreddit)`
+ If not a valid subreddit, print None.
+ NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```
wintermancer@lapbox ~/reddit_api/project $ cat 1-main.py
#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
top_ten = __import__('1-top_ten').top_ten
if len(sys.argv) < 2:
print("Please pass an argument for the subreddit to search.")
else:
top_ten(sys.argv[1])
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py this_is_a_fake_subreddit
None
wintermancer@lapbox ~/reddit_api/project $
```


## 2. Recurse it!
Write a <em>recursive function</em> that queries the <a href="/rltoken/odMvR9obKnQCx5EaM6_YFA" title="Reddit API" target="_blank">Reddit API</a> and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Write a **recursive function** that queries the [Reddit API](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:
+ Prototype: <code data-beeline-skip="true">def recurse(subreddit, hot_list=[])`
+ Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
+ If not a valid subreddit, return None.
+ NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)

```
wintermancer@lapbox ~/reddit_api/project $ cat 2-main.py
#!/usr/bin/python3
"""
2-main
"""
import sys

if __name__ == '__main__':
recurse = __import__('2-recurse').recurse
if len(sys.argv) < 2:
print("Please pass an argument for the subreddit to search.")
else:
result = recurse(sys.argv[1])
if result is not None:
print(len(result))
else:
print("None")
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py programming
932
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py this_is_a_fake_subreddit
None
```
