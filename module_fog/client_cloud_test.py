def cloud_client(ip, port):
	import requests
	#import json
	#import simplejson
	from signal import signal, SIGPIPE, SIG_DFL
	import sys
	signal(SIGPIPE, SIG_DFL)
	j = 0
	params1 = sys.argv[1]
	params2 = sys.argv[2]

	payload = {'node_id': 1, 'type': 'cloud',
            'module' : params1,
            'measure' : params2}
	headers = {'Content-Type': 'application/x-www-form-urlencoded', 
			'Content-Length': str(len(payload))}
	r = requests.post('http://%s:%d' %(ip, port), data=payload, headers=headers)


if __name__ == "__main__":
	ip = '192.168.0.1'
	port = 50000
	cloud_client(ip, port)	
	
