import sys,os,hashlib
import json

SPLUNK_HOME = os.environ.get("SPLUNK_HOME")

#dynamically load in any eggs
EGG_DIR = SPLUNK_HOME + "/etc/apps/pubnub_alert/bin/"

for filename in os.listdir(EGG_DIR):
    if filename.endswith(".egg"):
        sys.path.append(EGG_DIR + filename) 
        
from pubnubsdk import Pubnub

def callback(message):
    print >> sys.stderr, "DEBUG Callback handler for sent message %s" % message

def send_message(settings):
    print >> sys.stderr, "DEBUG Sending message to Pubnub with settings %s" % settings
    
    pub_key = settings.get('pubkey')
    sub_key  = settings.get('subkey')
    channel = settings.get('channel')
    message = settings.get('message')
  
    activation_key = settings.get('activationkey')
    app_name = "Pubnub Modular Alert"
    
    m = hashlib.md5()
    m.update((app_name))
    if not m.hexdigest().upper() == activation_key.upper():
        print >> sys.stderr, ("FATAL Activation key for App '%s' failed" % app_name)
        sys.exit(2)
        
    
    print >> sys.stderr, "INFO Sending message to Pubnub channel=%s with message=%s" % (channel,message)
  
    try:  
        pubnub = Pubnub(publish_key=pub_key,subscribe_key=sub_key)
         
        pubnub.publish(channel, message, callback=callback, error=callback) 
  
        print >> sys.stderr, "INFO Sent message to Pubnub : %s" % message
        return True  
    except Exception as tre:  
        print >> sys.stderr,tre  
        return False  
    except:  
        e = sys.exc_info()[0]  
        print >> sys.stderr, "ERROR Error sending message to Pubnub: %s" % e  
        return False  
  
  
if __name__ == "__main__":  
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":  
        payload = json.loads(sys.stdin.read())
        if not send_message(payload.get('configuration')):
            print >> sys.stderr, "FATAL Failed trying to send Message to Pubnub"
            sys.exit(2)
        else:
            print >> sys.stderr, "INFO Message successfully sent to Pubnub"
    else:
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
        sys.exit(1)
