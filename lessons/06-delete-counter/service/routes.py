import os
from redis import Redis
from flask import jsonify, url_for
from service import app

DATABASE_URI = os.getenv("DATABASE_URI", "redis://localhost:6379")

counter = Redis.from_url(DATABASE_URI, encoding="utf-8", decode_responses=True)

############################################################
# Index page
############################################################
@app.route("/")
def index():
    app.logger.info("Request for Base URL")
    return jsonify(
        status=200, 
        message="Hit Counter Service", 
        version="1.0.0",
        url=url_for("list_counters", _external=True)
    )

############################################################
# List counters
############################################################
@app.route("/counters", methods=["GET"])
def list_counters():
    app.logger.info("Request to list all counters...")
    counters = [dict(name=key, counter=int(counter.get(key))) for key in counter.keys('*')]
    return jsonify(counters)

############################################################
# Create counters
############################################################
@app.route("/counters/<name>", methods=["POST"])
def create_counters(name):
    app.logger.info("Request to Create counter...")
    count = counter.get(name)
    if count is not None:
        return jsonify(code=409, error="Counter already exists"), 409

    counter.set(name, 0)

    location_url = url_for('read_counters', name=name, _external=True)
    return jsonify(name=name, counter=0), 201, {'Location': location_url}

############################################################
# Read counters
############################################################
@app.route("/counters/<name>", methods=["GET"])
def read_counters(name):
    app.logger.info("Request to Read counter...")
    count = counter.get(name)
    if count is None:
        return jsonify(code=404, error="Counter {} does not exist".format(name)), 404

    return jsonify(name=name, counter=int(count))

############################################################
# Update counters
############################################################
@app.route("/counters/<name>", methods=["PUT"])
def update_counters(name):
    app.logger.info("Request to Update counter...")
    count = counter.get(name)
    if count is None:
        return jsonify(code=404, error="Counter {} does not exist".format(name)), 404

    count = counter.incr(name)
    return jsonify(name=name, counter=count)

############################################################
# Delete counters
############################################################
@app.route("/counters/<name>", methods=["DELETE"])
def delete_counters(name):
    app.logger.info("Request to Delete counter...")
    count = counter.get(name)
    if count is not None:
        counter.delete(name)

    return "", 204


############################################################
# Utility for testing
############################################################
def reset_counters():
    global counter
    if app.testing:
        counter.flushall()