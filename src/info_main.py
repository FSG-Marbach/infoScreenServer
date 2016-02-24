#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import info, display_svg

PORT_NUMBER = 8080

class requestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(sas_info.get_html())
		return

sas_info = info.info()
sas_info.add_info("info1", "blasaasdads")
sas_info.add_info("info2", "ajsfhuas")
sas_info.add_info("SAS Project1", "bla\nbla\n\bla")
sas_info.add_svg("info3", display_svg.draw_rect(0,0,100,100,"yellow", "green"), 200, 200)
sas_info.add_svg("info4", display_svg.draw_circle(0,0,100,"yellow", "green"), 200, 200)

try:
	server = HTTPServer(('', PORT_NUMBER), requestHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
