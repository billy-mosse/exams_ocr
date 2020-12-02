import traceback

from flask import Flask
from flask import request, abort, make_response


app = Flask(__name__)
app.config["TRAP_HTTP_EXCEPTIONS"] = True

import sys
@app.route("/process", methods = ['POST'])
def process():
    file_path = request.form.get("file_path")
    print(file_path)
    sys.stdout.flush()

    return "Hola"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
