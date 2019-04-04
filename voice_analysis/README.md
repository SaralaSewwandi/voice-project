#Voice analysis

##Installation

install docker  
install nvidia-docker

Then run following commands

git clone https://blisuru@bitbucket.org/blisuru/voice_analysis.git  
cd voice_analysis  
docker build -t bl:voiceml .  
cd VoiceToText/DeepSpeech  
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.4.1/deepspeech-0.4.1-models.tar.gz  
tar xvfz deepspeech-0.4.1-models.tar.gz  
cd ../../

##Running
nvidia-docker run -it -v ${PWD}:/app --network="host" bl:voiceml

##Sample requests

###Speech to text
http://localhost:8080/speechtotext

{  
    "InputPath":"/app/VoiceToText/DeepSpeech/test.wav",  
    "Method" : "DetNumber/DetCommand"  
}

{  
    "Text" : "1234"  
}

###Enroll users for voice recognition
http://localhost:8080/enrollspeaker

{  
    "InputPath":"/app/SpeakerRecognition/speakerrecognitionpy3/data/enroll/ann /app/SpeakerRecognition/speakerrecognitionpy3/data/enroll/taro /app/SpeakerRecognition/speakerrecognitionpy3/data/enroll/muru /app/SpeakerRecognition/speakerrecognitionpy3/data/enroll/saman",  
    "ModelPath":"/app/SpeakerRecognition/speakerrecognitionpy3/model.out"  
}

{  
    "State" : "Success/Fail"  
}

###Voice recognition
http://localhost:8080/predictspeaker

{  
    "InputPath":"/app/SpeakerRecognition/speakerrecognitionpy3/data/predict/ann/121-121726-0009.wav",  
    "ModelPath":"/app/SpeakerRecognition/speakerrecognitionpy3/model.out"  
}  

{  
    "State" : "Authorized/Unauthorized",  
    "User" : "saman"  
}
