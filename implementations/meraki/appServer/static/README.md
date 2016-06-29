## Splunk Cisco Meraki Modular Input v0.7

## Overview

This is a Splunk modular input add-on for Cisco Meraki that allows you to receive 
JSON probe events from the Meraki Presence Cloud.


## Dependencies

* Splunk 5.0+
* Supported on Windows, Linux, MacOS, Solaris, FreeBSD, HP-UX, AIX

## Setup

* Untar the release to your $SPLUNK_HOME/etc/apps directory
* Restart Splunk
* Browse to the Meraki App and enter the Meraki Secret and Validator in the setup screen.
* navigate to Data inputs -> Meraki to setup a new Meraki HTTP server to listen for event data


## Logging

Any log entries/errors will get written to $SPLUNK_HOME/var/log/splunk/splunkd.log


## Troubleshooting

* You are using Splunk 5+
* Look for any errors in $SPLUNK_HOME/var/log/splunk/splunkd.log