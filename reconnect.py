import urllib2

soap_body = '\r\n'.join((
    '<?xml version="1.0" encoding="utf-8"?>',
    '<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">',
    '  <s:Body>',
    '    <u:ForceTermination xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:2"/>',
    '  </s:Body>',
    '</s:Envelope>'))


soap_action = "urn:schemas-upnp-org:service:WANIPConnection:2#ForceTermination"

headers = {
    'SOAPAction': u'"%s"' % (soap_action),
    'Host': u'fritz.box:49000',
    'Content-Type': 'text/xml',
    'Content-Length': len(soap_body),
}

ctrl_url = "http://fritz.box:49000/igd2upnp/control/WANIPConn1"

request = urllib2.Request(ctrl_url, soap_body, headers)
response = urllib2.urlopen(request)

print response.read()
