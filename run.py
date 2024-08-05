from pyngrok import ngrok
from app import app
import os

if __name__ == '__main__':
    # Start Flask app in a separate thread
    from threading import Thread
    flask_thread = Thread(target=lambda: app.run(port=5000))
    flask_thread.start()

    # Connect to ngrok
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")
