import http.server
import socketserver
import random

PORT = 8000

# Sample data
memes = [
    "https://i.imgflip.com/1g8my4.jpg",  # Example meme image
    "https://i.imgflip.com/1h7in3.jpg",
]
emojis = ["😀", "😂", "🥺", "🎉", "🔥"]
ascii_emojis = [
    "(¬‿¬)",
    "(╯°□°）╯︵ ┻━┻",
    "╰(°▽°)╯",
]

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        choice = random.choice(["meme", "emoji", "ascii-emoji"])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if choice == "meme":
            meme = random.choice(memes)
            response = f'<html><body><img src="{meme}" alt="Random Meme" style="max-width:100%;"/></body></html>'
        elif choice == "emoji":
            emoji = random.choice(emojis)
            response = f'<html><body><h1>{emoji}</h1></body></html>'
        else:  # ascii-emoji
            ascii_emoji = random.choice(ascii_emojis)
            response = f'<html><body><pre>{ascii_emoji}</pre></body></html>'

        self.wfile.write(response.encode('utf-8'))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
