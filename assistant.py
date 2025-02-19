import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import getpass

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can change to voices[1] for a different voice

# Function to make the assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your assistant. How may I assist you?")

# Function to take microphone input from the user and return it as text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Allows for pauses in speech
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I couldn't understand. Please say that again.")
        return "None"
    return query.lower()

# Function to send email using Gmail
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        email = input("Enter your email address: ")
        password = getpass.getpass("Enter your email password: ")
        server.login(email, password)
        server.sendmail(email, to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't send the email.")

# Main function to execute commands based on user input
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play soothing music' in query or 'play music' in query:
            music_dir = r"C:\Users\fazil\Music"  # Corrected path
            try:  # Filter out non-music files, only consider .mp3 and .wav files
                songs = [song for song in os.listdir(music_dir) if song.endswith(('.mp3', '.wav'))]
                if songs:  # This block checks if there are any songs in the list
                    song_to_play = songs[0]  # You can replace this with random.choice(songs) for random selection
                    print(f"Playing: {song_to_play}")
                    os.startfile(os.path.join(music_dir, song_to_play))  # Play the music file
                else:
                    speak("No music found in the directory.") # Handle the error if the music directory is not found
            except FileNotFoundError:
                speak("Sorry, I couldn't find the music directory.") # Catch other unexpected exceptions
            except Exception as e:
                print(f"Error: {e}")
                speak("An error occurred while trying to play music.")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Code\\code.exe"  # Update this path to your code editor
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say in the email?")
                content = takeCommand()
                to = "your-email@gmail.com"  # Replace with the recipient's email
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I encountered an error while sending the email.")
