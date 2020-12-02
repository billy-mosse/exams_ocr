import traceback

from flask import Flask
from flask import request, abort, make_response


app = Flask(__name__)
app.config["TRAP_HTTP_EXCEPTIONS"] = True


@app.route("/helloworld", methods = ['GET'])
def helloworld():
    return "Hola"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
