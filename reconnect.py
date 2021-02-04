import urllib.request
from socket import gethostbyname_ex
from sys import argv

def reconnect(host="fritz.box", port=49000):
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
        'Host': (host+":"+str(port)),
        'Content-Type': 'text/xml',
        'Content-Length': len(soap_body),
    }

    ctrl_url = "http://" + host + ":49000/igd2upnp/control/WANIPConn1"

    request = urllib.request.Request(ctrl_url, bytes(soap_body, "utf-8"), headers)

    try:
        return urllib.request.urlopen(request).read().decode()
    except urllib.error.HTTPError as e:
        return e.read().decode()
    except urllib.error.URLError as e:
        return str(e)

if __name__ == "__main__":

    # Process arguments
    if "--host" in argv[1:]:
        host = argv.pop(argv.index("--host")+1)
        argv.remove("--host")
    else:
        host = "fritz.box"

    if "--port" in argv[1:]:
        port = argv.pop(argv.index("--port")+1)
        argv.remove("--port")
    else:
        port = 49000

    if "--debug" in argv[1:]:
        debug = True
        argv.remove("--debug")
    else:
        debug = False

    result = reconnect(host, port)
    
    if "urlopen error" in result and ("getaddrinfo failed" in result or "Name or service not known" in result):
        print(f"Could not find", host, "\n")
        print(result)

    elif "Error" in result:
        print("Host:", host, "\nIP:", gethostbyname_ex(host)[2][0], "\nPort:", port, "\n")
        print(result)

    elif ":service:WANIPConnection:2" in result and "ForceTerminationResponse" in result:
        if debug:
            print("Host:", host, "\nIP:", gethostbyname_ex(host)[2][0], "\nPort:", port, "\n")
            print(result)
        else:
            print("Success")