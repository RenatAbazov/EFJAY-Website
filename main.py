from flask import Flask, render_template
import os


app = Flask(__name__)
app_root = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def photo():
    return render_template("photo.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/video")
def video():
    return render_template("video.html")

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True)
