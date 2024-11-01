from flask import Flask, render_template_string
import random

app = Flask(__name__)

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

@app.route('/')
def random_response():
    choice = random.choice(["meme", "emoji", "ascii-emoji"])
    if choice == "meme":
        meme = random.choice(memes)
        return render_template_string(f'<img src="{meme}" alt="Random Meme" style="max-width:100%;"/>')
    elif choice == "emoji":
        emoji = random.choice(emojis)
        return render_template_string(f'<h1>{emoji}</h1>')
    else:  # ascii-emoji
        ascii_emoji = random.choice(ascii_emojis)
        return render_template_string(f'<pre>{ascii_emoji}</pre>')

if __name__ == '__main__':
    app.run(debug=True)
