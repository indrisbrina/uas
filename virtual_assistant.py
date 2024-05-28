import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take command from the microphone
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        speak("maaf kontol.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

# Function to process the command
def process_command(command):
    if 'wikipedia' in command:
        speak("Searching Wikipedia...")
        command = command.replace('wikipedia', '')
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'hello' in command:
        speak("Hello! How can I help you?")
    elif 'how are you' in command:
        speak("I am fine, thank you. How are you?")
    elif 'goodbye' in command:
        speak("Goodbye!")
        return False
    else:
        speak("I can search Wikipedia or greet you. Try saying 'search Wikipedia for Python'.")
    return True

# Main loop
def main():
    speak("I am your virtual assistant. How can I help you?")
    while True:
        command = take_command()
        if command:
            if not process_command(command):
                break

if __name__ == "__main__":
    main()
