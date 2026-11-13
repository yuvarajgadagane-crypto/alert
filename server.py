"""
Student Sleep & Fall Alert System — Local Web Server
Runs a lightweight, zero-dependency HTTP server and automatically opens
the web application in the default browser.
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Concise logging
        sys.stdout.write(f"[{self.log_date_time_string()}] {args[0]} {args[1]}\n")

def run():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=================================================================")
        print("STUDENT SLEEP & FALL ALERT SYSTEM -- RUNNING")
        print("=================================================================")
        print(f"Local Server URL : {url}")
        print("Camera Feed      : Enabled via WebRTC MediaDevices")
        print("Buzzer Audio     : Web Audio API Synthesizer")
        print("Press Ctrl+C in this terminal to stop the server.")
        print("=================================================================")
        
        # Open in browser automatically
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server. Goodbye!")
            httpd.shutdown()

if __name__ == "__main__":
    run()
