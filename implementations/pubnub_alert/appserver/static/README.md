## Splunk Pubnub Modular Alert v1.0

## Overview

This is a Splunk Modular Alert for sending messages to a Pubnub channel

## Dependencies

* Splunk 6.3+
* Supported on Windows, Linux, MacOS, Solaris, FreeBSD, HP-UX, AIX
* Pycrypto

## Setup

* Untar the release to your $SPLUNK_HOME/etc/apps directory
* Restart Splunk

## Pycrypto Module

You have to obtain, build and add the pycrypto package yourself :

https://pypi.python.org/pypi/pycrypto

The simplest way is to build pycrypto and drop the "Crypto" directory in $SPLUNK_HOME/etc/apps/pubnub_alert/bin.
I don't recommend installing the pycrypto package to the Splunk Python runtime's site-packages, this could have unforeseen side effects.

### Building and installing PyCrypto

I do not bundle the pycrypto module with the core release , because :

* you need to build it for each separate platform
* US export controls for encrypted software

So , here are a few instructions for building and installing pycrypto yourself :

* Download the pycrypto package from https://pypi.python.org/pypi/pycrypto

* Then run these 3 commands  (note : you will  need to use a System python 2.7 runtime , not the Splunk python runtime)

        python setup.py build
        python setup.py install
        python setup.py test
        
3) browse to where the Crypto module was installed to ie: /usr/local/lib/python2.7/dist-packages/Crypto

4) Copy the "Crypto" directory to $SPLUNK_HOME/etc/apps/pubnub_alert/bin


## Configuration

You will need a Pubnub account to use this Modular Alert.

You can sign up at pubnub.com

Once your account is setup you will then be able to obtain your Publish Key from your profile.


## Using

Perform a search in Splunk and then navigate to : Save As -> Alert -> Trigger Actions -> Add Actions -> Publish to Pubnub

On this dialogue you can enter your Pubnub  "channel" and "message"

For the message field , token substitution can be used just the same as for email alerts.

http://docs.splunk.com/Documentation/Splunk/latest/Alert/Setupalertactions#Tokens_available_for_email_notifications


## Logging

Browse to : Settings -> Alert Actions -> Publish to Pubnub -> View Log Events

Or you can search directly in Splunk : index=_internal sourcetype=splunkd component=sendmodalert action="pubnub"


## Troubleshooting

1) Is your "channel" correct ?
2) Are your alerts actually firing ?
3) Is your publish key correct ?

## Contact

This project was initiated by Damien Dallimore , ddallimore@splunk.com

