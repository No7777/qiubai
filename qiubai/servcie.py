import pymongo
from flask import Flask, render_template
from settings import MONGO_URL, MONGO_DATABASE

app = Flask(__name__)

@app.route("/")
def hello():
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DATABASE]
    jokes = db["QiubaiItem"].find()
    client.close()
    return render_template("display.html", jokes = jokes)

if __name__ == '__main__':
    app.run()
