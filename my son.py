from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Website</title>
        <style>
            body {
                background: #222;
                color: white;
                text-align: center;
                font-family: Arial;
            }
            h1 {
                color: cyan;
            }
            button {
                padding: 10px 20px;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Website!</h1>
        <p>This website is running by your father.</p>
        <button onclick="alert('my fucking son hash!')">Click Me</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)