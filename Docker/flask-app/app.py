from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images
images = [
	"https://i.gifer.com/2GU.mp4",
	"https://i.gifer.com/7z7c.mp4",
	"https://i.gifer.com/HEMz.mp4",
	"https://i.gifer.com/Se8X.mp4",

            ]
@app.route('/')
def index():
	url = random.choice(images)
	return render_template('index.html', url=url)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
