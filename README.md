# FRITZ!Box - Reconnect Script

This script uses UPnP to reconnect the FRITZ!Box. Tested with FRITZ!OS 7.12 and 07.20 on the FRITZ!Box 6490 Cable.

```
% python reconnect.py --debug
Host: fritz.box
IP: 192.168.178.1
Port: 49000

 <?xml version="1.0" encoding="utf-8"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body>
<u:ForceTerminationResponse xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:2"></u:ForceTerminationResponse>
</s:Body>
</s:Envelope>
```

Idea from Ferry Boender: https://www.electricmonk.nl/log/2016/07/05/exploring-upnp-with-python/
