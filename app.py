from flask import Flask, send_file, jsonify
from make_profile import make_profile

app = Flask(__name__)

canvas_size = 400
pixel_size = 50


@app.route("/")
def index():
    return jsonify({"name": "profile-picture-from-username", "description": "Generate unique profile picture from username and use it everywhere with connecting Flask server.", "license": "MIT", "developer": "orhanemree", "github": "https://github.com/profile-picture-from-username"})


@app.route("/<username>")
def username(username):
    try:
        profile = make_profile(username, canvas_size, pixel_size)
        return send_file(profile, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": "417 Expectation Failed", "message": str(e)}), 417


if __name__ == '__main__':
    app.run(port=5500)
