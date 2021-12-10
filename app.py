from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/static/<path:path>')
def send_file(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()