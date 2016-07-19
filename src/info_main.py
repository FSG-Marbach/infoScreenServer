#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import info, display_svg, chart_svg, pickle

PORT_NUMBER = 8080

class requestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(uss_info.get_html())
		return

uss_info = info.info()
f = open("data/infos.ussinfos", "rb")
infos = pickle.load(f)
f.close()
for i in infos:
        uss_info.add_info(i[0], i[1])

try:
	server = HTTPServer(('', PORT_NUMBER), requestHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
