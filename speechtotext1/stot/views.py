from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    return render(request,'speechtotext.html')
def all(request):
    import speech_recognition as sr
    import os
    r=sr.Recognizer()
    print("ask what ever you want:")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source) 
        text=r.recognize_google(audio,language='eng-in')
        print('you said:',text)
        return HttpResponse(request,'speechtotext.html',{'txt':text})
    #return render(request,'speechtotext.html')
    
