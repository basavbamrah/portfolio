from flask import Flask, request
from flask_cors import CORS
from firebase_admin import credentials, firestore, storage

import os


app = Flask(__name__)
CORS(app, origins=["*"])

# cred_file = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
# cred = credentials.Certificate(cred_file)
# admin = firebase_admin.initialize_app(credential=cred)
# db = firestore.client()


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return {
            'status': "success",
            'version': "0.0.1"
        }, 200
    else:
        return {
            'status': "error",
            'message': "Method not allowed"
        }, 405




if __name__ == "__main__":
    app.run()
