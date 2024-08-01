from  app import app
from modeller.modeller import model
from flask import request

obj=model()
@app.route("/user/read")
def read():
    return obj.read()

@app.route("/user/add", methods=["Post"])
def add():
    return obj.add(request.form)

@app.route("/user/update", methods=["PUT"])
def update():
    return obj.update(request.form)

@app.route("/user/delete", methods=["DELETE"])
def delete():
    return obj.delete(request.form)
