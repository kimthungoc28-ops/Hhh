import threading
from server import run_server
import tracker

threading.Thread(target=run_server).start()
tracker.client.run()
