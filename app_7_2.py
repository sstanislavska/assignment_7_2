from flask import Flask, request, jsonify

app = Flask(__name__)


counter = 0
@app.get("/counter")
def count_requests():
   global counter
   counter += 1
   return jsonify(counter)


@app.post("/reset-counter")
def reset_counter():
    global counter
    counter = 0
    return jsonify(counter)


if __name__ == "__main__":
   app.run(debug=True)