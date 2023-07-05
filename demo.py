import speech_recognition as s
#most imp for spech reco is recoginizer it is in lib s
def take_query():
    sr=s.Recognizer()
    print("say something:")
    # m=s.Microphone()# in start of this obj call __enter__() and at end __exit__() it is like open and close of file
    # reco class has two method listen () and recognize_google(audio clip,target lang)

    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            #sr.pause_thresold=3 #if recoginizer does not pause or wait for users input
            sr.adjust_for_ambient_noise(m,duration=5)
            text=sr.recognize_google(audio,language='en-IN')
        # reco google may give the following errors 1st request Error (internet conn) 2nd unknownValueError (if it does not got what was said)
        #exception by listen()  1st waittimeout error (when wait is done by user)
            return text
        except:
            print("Exception occured")

print("you said:",take_query())