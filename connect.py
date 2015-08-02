from slacker import Slacker
import plist as p


slack = Slacker(p.token)
#slack.chat.post_message('#general',"Hello, API working")

response= slack.users.list()
users = response.body['members']
print users[0]

response1=slack.channels.list()
channellist= response1.body['channels']
print channellist

#need to use channel id
response2=slack.channels.history(channel="C0657F54N")
history = response2.body['messages']
print history[1]

#Direct messages ***only for me***
response3=slack.im.list()
imlist=response3.body['ims']
print imlist

#channel id is user id
#response4=slack.im.history('D0657MRCG')
