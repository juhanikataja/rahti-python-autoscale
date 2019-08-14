from flask import Flask
import math
import time

app = Flask(__name__)

def factorial(N, R, imax):
  thesum = 0.0
  dx = R/imax
  start = time.time()
  for i in range(1,imax):
    thesum = thesum + (i*dx)**N * math.exp(-i*dx)
  thesum = thesum*dx
  end = time.time()
  return str(N) + "! =~ " + str(thesum) + "  (in " + str(end-start) +"s)"

@app.route("/")
def home():
    return factorial(5, 100.0, 1000000)

@app.route("/<int:N>/<int:I>")
def home_nri(N,I):
    return factorial(N, 100.0, 10**I)

if __name__ == "__main__":
    print(home())
    app.run(debug=True, port=8080, host='0.0.0.0')
