from flask import Flask, request, abort, make_response
import json

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.mimetype = "application/json"
  response.headers["Server"] = "FakeSUMOServer"
  response.headers["Access-Control-Allow-Methods"] = "GET"
  response.headers["Access-Control-Allow-Origin"] = "*"
  response.headers["Access-Control-Allow-Headers"] = "x-requested-with"
  response.headers["Access-Control-Expose-Headers"] = "Content-Length, X-Content-Hash"
  return response

@app.route("/offline/get-bundle")
def get_bundle():
  if "product" not in request.args or "locale" not in request.args:
    return abort(400)

  locale, product = request.args["locale"], request.args["product"]

  with open("files/bundles/{}-{}.json".format(locale, product)) as f:
    r = f.read()

  with open("files/meta/{}-{}.json".format(locale, product)) as f:
    content_hash = json.load(f)["hash"]

  response = make_response(r)
  response.headers["X-Content-Hash"] = content_hash
  return response

@app.route("/offline/bundle-meta")
def bundle_meta():
  if "product" not in request.args or "locale" not in request.args:
    return abort(400)

  locale, product = request.args["locale"], request.args["product"]

  with open("files/meta/{}-{}.json".format(locale, product)) as f:
    r = f.read()

  return make_response(r)

@app.route("/offline/get-languages")
def get_languages():
  with open("files/languages.json") as f:
    r = f.read()

  return make_response(r)

@app.route("/")
def yay():
  return "\"Yay fake server.\""

if __name__ == "__main__":
  app.run(debug=True)
