#!flask/bin/python
from flask import Flask, request, request_started
import configparser

config = configparser.ConfigParser()
config.read("counter-value.ini")
counter = int(config.get("counter_val", "counter"))

app = Flask(__name__)
@app.route('/', methods=["POST", "GET"])
def index():
    global counter
    if request.method == "POST":
        counter+=1
        config.set('counter_val', 'counter', str(counter))

        return "Hmm, Plus 1 to the counter please...\n"
    else:
        return str(f"My counter is: {counter} ! \nYou are my great champion!\n")


if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
