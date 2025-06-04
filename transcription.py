     pip install SpeechRecognition pydub
     import speech_recognition as sr
     
     r = sr.Recognizer()
     with sr.AudioFile('audio.wav') as source:
         audio_data = r.record(source)
         try:
             text = r.recognize_google(audio_data)
             print(text)
         except sr.UnknownValueError:
             print("Could not understand audio")
         except sr.RequestError as e:
             print(f"Could not request results from service; {e}")
    

     import assemblyai as aai
     
     aai.settings.api_key = "YOUR_API_KEY"
     
     transcriber = aai.Transcriber()
     transcript = transcriber.transcribe("./audio.wav")
     
     print(transcript.text)