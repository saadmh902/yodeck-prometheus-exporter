import http.server
import time
import requests
import json

apiKey = ""
username = ""

class MyHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

    def _set_headers_404(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
    def do_GET(self):

        if "metrics" not in self.path and "/organizations" not in self.path:
            self._set_headers_404()
            return()

        self._set_headers()
 

        if "/metrics" in self.path:
            start_time = time.monotonic()
            displayedText = "# TYPE yodeck_device_status gauge\n"
            exportString = ""
            print("Starting to collect data...")
            r=requests.get("https://app.yodeck.com/api/v1/device/?username="+username+"&api_key="+apiKey+"&format=json")
    
        
            jsonObject = json.loads(r.text)

            for count,yodeckDevice in enumerate(jsonObject["objects"]):
                if(yodeckDevice['online'] == False):
                    onlineStatus = "0"
                else:
                    onlineStatus = "1"
                exportString = ('yodeck_device_status{ID="'+str(yodeckDevice['id'])+'",name="'+yodeckDevice['name']+'",IsOnline="'+str(yodeckDevice['online'])+'"} ' + onlineStatus+"\n")
                #print(exportString)
                displayedText+=exportString



            displayedText += "# TYPE request_processing_seconds summary\n" 
            displayedText = displayedText + 'request_processing_seconds ' + str(time.monotonic() - start_time) + '\n'
            print(displayedText)
            print(("Collected {} values").format(len(jsonObject["objects"])))
            
            self.wfile.write(displayedText.encode('utf-8'))
            self.wfile.write("\n".encode('utf-8'))
            return


HTTP_BIND_IP = "localhost"
HTTP_PORT_NUMBER = 3304

server_class = MyHandler
httpd = http.server.ThreadingHTTPServer((HTTP_BIND_IP, HTTP_PORT_NUMBER), server_class)
print(time.asctime(), "Server Starts - %s:%s" % ("*" if HTTP_BIND_IP == '' else HTTP_BIND_IP, HTTP_PORT_NUMBER))
httpd.serve_forever()
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % ("localhost", HTTP_PORT_NUMBER))
