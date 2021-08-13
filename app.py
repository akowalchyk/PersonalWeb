import flask
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'aSldhasldkj'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



