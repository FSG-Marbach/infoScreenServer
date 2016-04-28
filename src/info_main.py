#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import info, display_svg, chart_svg

PORT_NUMBER = 8080

class requestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(sas_info.get_html())
		return

#Text

sas_info = info.info()
sas_info.add_info("Info 1", "blasaasdads")
sas_info.add_info("Info 2", "ajsfhuas")
sas_info.add_info("Info 3", "aassaaadfsdgs")
sas_info.add_info("Info 4", "ajsfhuas")
sas_info.add_info("Info 5", "sfgd")
sas_info.add_info("Info 6", "ajsfhuas")
sas_info.add_info("Some Text", "Text")

#SVG

sas_info.add_svg("SVG 1", display_svg.draw_rect(0,0,100,100,"yellow", "green"), 200, 200)
sas_info.add_svg("SVG 2", display_svg.draw_circle(0,0,100,"yellow", "green"), 200, 200)
sas_info.add_svg("Chart Demo 1", chart_svg.chart(200, 200, [3, 40, 20, 100, 140, 200]).draw("red"), 200, 200)
sas_info.add_svg("Chart Demo 2", chart_svg.chart(200, 200, [3, 40, 20, 100, 140, 200], 2).draw("red"), 200, 200, "It is possible to add a decription to charts!<br>It also works for svgs!")

try:
	server = HTTPServer(('', PORT_NUMBER), requestHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
