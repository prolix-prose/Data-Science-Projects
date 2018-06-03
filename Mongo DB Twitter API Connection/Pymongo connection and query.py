# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 17:54:22 2017

@author: Scott 
"""

from pymongo import MongoClient

# Connects to Mongo Client and 'twitterdb' database

client = MongoClient()
mydb = client['twitterdb']

# Looks at the DB and counts how many tweets are in it

mydb.twitter_search.count() 
id_c = mydb.twitter_search.find({'id'})
id_c.count()

# Counts how many times 'yankees' and 'openingday' were mentioned

yankees = mydb.twitter_search.find({'text': {'$regex': 'yankees'}})
yankees.count()
opening_day = mydb.twitter_search.find({'text': {'$regex': 'openingday'}})
opening_day.count()

# Explores the top hashtags by count (Research Querying in MongoDB for more information)

mydb.twitter_search.aggregate([
    { $group: {
        _id: '$lang',
        count: {$sum: 1}
    }},
    
    {$sort: {
     count: -1
}},

{$limit: 5} 
]);
mydb.twitter_search.aggregate([ 
{$unwind: '$entities.hashtags'}, 

{ $group: { 
_id: '$entities.hashtags.text', 
tagCount: {$sum: 1} 
}}, 

{ $sort: { 
tagCount: -1 
}}, 

{ $limit: 10 }
]);