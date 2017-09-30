import tweepy, time, sys

argfile = str(sys.argv[1])



CONSUMER_KEY = 'XDNxFmB4O56N51tJcJIKzA1Bd'
CONSUMER_SECRET = 'oeUBOsCkzStoFn3pHoEsYByADL1lEYqxpvLAh9en6YlAAg0CMU'
ACCESS_KEY = '914175664504352771-rO7iX0sFOdO1TmhSM772FjVm7Lt9kPh'
ACCESS_SECRET = 'TEuYsVRsFDGqmuWEaB5WsLUsRhPo9mvPEDSFQEghBVwLw'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile,'r')
f=filename.readlines()
filename.close()



for line in f:

    api.update_status(status=line)
    time.sleep(100)#Tweet every 15 minutes
