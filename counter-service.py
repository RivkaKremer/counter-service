#!flask/bin/python
from flask import Flask, request, request_started
from redis import Redis, RedisError


# Connect to Redis
redis = Redis(host="sentinel.redis.svc.cluster.local", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    global counter
    if request.method == "POST":
        try:
            requests = redis.incr("counter")
        except RedisError:
            return "<i>Cannot connect to Redis, counter disabled</i>"
        return "Hmm, Plus 1 to the counter please...\n"
    else:
        requests = redis.get("counter")
        return str(f"My counter is: {requests} ! \nYou are my great champion!\n")


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
