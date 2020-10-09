from flask import Flask, jsonify,request
import time
app = Flask(__name__);
@app.route("/")
def response():
    query = "hi"
    res = query + " " + time.ctime()
    return jsonify({"response" : res})
if __name__=="__main__":
    app.run()
