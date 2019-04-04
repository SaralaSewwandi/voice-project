from flask import Flask, render_template, request
from werkzeug import secure_filename
import VoiceToText.DeepSpeech.native_client.python.client as v2tClient
import sys
sys.path.append('/app/SpeakerRecognition/speakerrecognitionpy3')
import speakerrecognition as srClient
from pyckson import pyckson, listtype, serialize, parse
import os
import shutil
from flask import jsonify
import nltk
 
application = Flask(__name__)  

def passNumber(sentence):
    num_words = ['one', 'two', "o" , 'three', 'the', 'plea', 'pre', 'four', 'five', 'you', 'fay', 'six', 'seven', 'sen', 'so', 'eight', 'a', 'nine', 'zero', 'see', 'sea']
    nums = ['1', '2', '2', '3', '3', '3', '3', '4', '5', '5', '5', '6', '7', '7', '7' , '8', '8', '9', '0', '0', '0']
    words = sentence.split()
    new_sentence = ""
    for word in words:
        score = 1000
        index = -1
        i = 0
        for num_word in num_words:
            dis = nltk.edit_distance(num_word, word)
            if(score > dis):
                score = dis
                index = i
            i = i + 1
        new_sentence = new_sentence + nums[index]
    print(sentence, " : ", new_sentence)
    return new_sentence

def passCommand(sentence):
    num_words = ['Yes', 'No']
    nums = ['Yes', 'No']
    words = sentence.split()
    new_sentence = ""
    for word in words:
        score = 1000
        index = -1
        i = 0
        for num_word in num_words:
            dis = nltk.edit_distance(num_word, word)
            if(score > dis):
                score = dis
                index = i
            i = i + 1
        new_sentence = new_sentence + nums[index]
    print(sentence, " : ", new_sentence)
    return new_sentence
    
          
 
@application.route('/speechtotext', methods = ['POST'])
def speechtotext():
    content = request.get_json()
    print("Request : ", content)
    newRes = ""
    res = v2tClient.mainCall(audio = content['InputPath'])
    if(content['Method'] == "DetNumber"):
        newRes = passNumber(res)
    if(content['Method'] == "DetCommand"):
        newRes = passCommand(res)
    data = {
        "Text"  : newRes
    }
    resp = jsonify(data)
    resp.status_code = 200
    print("Response : ", data)
    return resp

@application.route('/predictspeaker', methods = ['POST'])
def predictSpeaker():
    content = request.get_json()
    print("Request : ", content)
    res, score = srClient.mainCall('predict', content['InputPath'], content['ModelPath'])
    state = "Unauthorized"
    if (score > 0.859) :
        state = "Authorized"
    data = {
        "State"  : state,
        "User" : res
    }
    resp = jsonify(data)
    resp.status_code = 200
    print("Response : ", data)
    return resp

@application.route('/enrollspeaker', methods = ['POST'])
def enrollSpeaker():
    content = request.get_json()
    print("Request : ", content)
    res = srClient.mainCall('enroll', content['InputPath'], content['ModelPath'])
    data = {
        "State"  : res
    }
    resp = jsonify(data)
    resp.status_code = 200
    print("Response : ", data)
    return resp
