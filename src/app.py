from flask import Flask
import math
import time

app = Flask(__name__)
@app.route("/")
def home():
    thesum = 0.0
    imax = 1000000
    start = time.time()
    for i in range(1,imax):
      thesum = thesum + 1.0/(1.0 + math.exp(i/(1.0*imax)))

    end = time.time()
    return "Hello, World! The Sum is " + str(thesum) + " in " + str(end-start)
if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
