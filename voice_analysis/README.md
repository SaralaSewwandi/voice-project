#Voice analysis

##Installation

install docker  
install nvidia-docker

Then run following commands

git clone https://github.com/SaralaSewwandi/voice-project.git
cd voice_analysis  
docker build -t bl:voiceml .  


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
