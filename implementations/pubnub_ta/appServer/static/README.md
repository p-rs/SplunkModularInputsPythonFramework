# Splunk Pubnub Modular Input v1.1

## Overview

This is a Splunk modular input add-on for subscribing to Pubnub channels

## Dependencies

* Splunk 6.3+
* Supported on Windows, Linux, MacOS, Solaris, FreeBSD, HP-UX, AIX
* Pycrypto

## Setup

* Untar the release to your $SPLUNK_HOME/etc/apps directory
* Restart Splunk
* Browse to Manager -> Data Inputs -> Pubnub and setup your inputs

## Activation Key

You require an activation key to use this App. Visit http://www.baboonbones.com/#activation to obtain a free,non-expiring key

## Pycrypto Module

You have to obtain, build and add the pycrypto package yourself :

https://pypi.python.org/pypi/pycrypto

The simplest way is to build pycrypto and drop the "Crypto" directory in $SPLUNK_HOME/etc/apps/pubnub_ta/bin.
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

4) Copy the "Crypto" directory to $SPLUNK_HOME/etc/apps/pubnub_ta/bin


## Configuration

You will need a Pubnub account to use this Modular Alert.

You can sign up at pubnub.com

Once your account is setup you will then be able to obtain your Subscribe Key from your profile.


### Custom Response Handlers

You can provide your own custom Response Handler. This is a Python class that you should add to the 
rest_ta/bin/responsehandlers.py module.

You can then declare this class name and any parameters in the REST Input setup page.


## Logging

Any log entries/errors will get written to $SPLUNK_HOME/var/log/splunk/splunkd.log


## Troubleshooting

* You are using Splunk 5+
* Look for any errors in $SPLUNK_HOME/var/log/splunk/splunkd.log
* Is you channel name correct ?
* Is your subscription key correct ?

## Contact

This project was initiated by Damien Dallimore
<table>

<tr>
<td><em>Email</em></td>
<td>damien@baboonbones.com</td>
</tr>

</table>