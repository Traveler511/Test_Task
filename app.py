# -*- coding: utf-8 -*-
from func import Answer
from flask import Flask, jsonify, request
import sched
import time
from flask_cors import CORS
from flask import Flask, redirect, url_for, request, json


# from flask import render_template

import func

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS

CORS(app)

# sanity check route


@app.route('/result', methods=['GET', 'POST'])
def Result():
# @app.route('/result/Result/<filial>/<problem>/<themeSelect>/<themeInput>', methods=['POST'])
# def Result(filial=None, problem=None, themeSelect=None, themeInput=None):
    if request.method == 'POST':
        # fillial = request.form['filial']
        # problem = request.form['problem']
        # themeSelect = request.form['themeSelect']
        # themeInput = request.form['themeInput']

        # answer = func.Answer(1)
        # a = {'filial': filial, 'problem': problem, 'themeSelect': themeSelect,
        #      'themeInput': themeInput, 'answer': answer}
        # print(a)
        # return json.dumps(a, ensure_ascii=False)
        # return True
        print('true')


if __name__ == '__main__':
    app.run()
