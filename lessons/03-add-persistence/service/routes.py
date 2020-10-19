import os
from redis import Redis
from service import app

DATABASE_URI = os.getenv("DATABASE_URI", "redis://localhost:6379")

counter = Redis.from_url(DATABASE_URI, encoding="utf-8", decode_responses=True)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/counter")
def get_counter():
    count = counter.incr("count")
    return dict(counter=count)

############################################################
# Utility for testing
############################################################
def reset_counter():
    global counter
    if app.testing:
        counter.set("count", 0)
