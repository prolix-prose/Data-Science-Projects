# Python Tweet Listener and MongoDB backend
You need a local MongoDB client running and Twitter API credentials. 
You supply a dictionary of Words and let the listener collect tweets with a rate limiter until you kill the script
## Required Packages
[Tweepy](http://www.tweepy.org/) <br>
[PyMongo](https://api.mongodb.com/python/current/) <br>
JSON
### MongoDB
Store the Twitter data in MongoDB and query it using PyMongo connection to the DB<br>
https://docs.mongodb.com/manual/core/crud/ for more info on queries
