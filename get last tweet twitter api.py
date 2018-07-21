#! py -2
import base64
import json
import urllib2

### Setup access credentials

consumer_key = "M0veSnqi2FRMgPLZr7RbDtEDu"
consumer_secret = "RtnLsZkR8et4LqlxNYwM0qczmagfs1uLlZY8q8wP48smSFm1j2"

### Get the Access Token

bearer_token = "%s:%s" % (consumer_key, consumer_secret)
bearer_token_64 = base64.b64encode(bearer_token)

token_request = urllib2.Request("https://api.twitter.com/oauth2/token") 
#token_request = urllib2.Request("http://192.168.1.4:1025/") 
token_request.add_header("Content-Length", "29")
token_request.add_header("Accept-Encoding", "identity")
token_request.add_header("User-Agent", "MyTwitterApp")
token_request.add_header("Host", "api.twitter.com")
token_request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8")
token_request.add_header("Authorization", "Basic %s" % bearer_token_64)
token_request.data = "grant_type=client_credentials"

token_response = urllib2.urlopen(token_request)
token_contents = token_response.read()
#print token_contents
token_data = json.loads(token_contents)
access_token = token_data["access_token"]

### Use the Access Token to make an API request

timeline_request = urllib2.Request("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=_ahmad_saeed&count=1")
timeline_request.add_header("Authorization", "Bearer %s" % access_token)

timeline_response = urllib2.urlopen(timeline_request)
timeline_contents = timeline_response.read()
timeline_data = json.loads(timeline_contents)

print json.dumps(timeline_data[0]["text"], indent=2, sort_keys=True)

'''
for url in timeline_data["products"][0]["urls"]:
    if url["key"] == "Text":
        value = url["value"]
        break
else:
    # Some default action
    print "No url found"
    value = "http://www.url.com"

print "Value:", value
'''
