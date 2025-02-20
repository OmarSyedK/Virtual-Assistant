import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pygame
import random
import time  # For adding pauses between breathing exercise steps

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can change to voices[1] for a different voice

# Initialize pygame mixer for controlling music
pygame.mixer.init()

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

    speak("I am your assistant. How may I assist you today?")

# Function to take microphone input from the user and return it as text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Allows for pauses in speech
        audio = r.listen(source)

    try:
        print("........")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I couldn't understand. Please say that again.")
        return "None"
    return query.lower()

# Function to tell a joke
def tellJoke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t eggs tell jokes? Because they might crack up.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "Why don't some couples go to the gym? Because some relationships don’t work out."
    ]
    joke = random.choice(jokes)  # Randomly select a joke from the list
    speak(joke)

# Function to provide exercises for the day
def dailyExercise():
    exercises = [
        "Start with a 5-minute warm-up, like light walking or stretching.",
        "Do some squats, 3 sets of 10 reps.",
        "Try some gentle yoga poses like downward dog, child's pose, and cat-cow for flexibility.",
        "Try some pelvic floor exercises to strengthen your muscles, like kegel exercises.",
        "End with a relaxing 5-minute cool-down stretch."
    ]
    speak("Here are your exercises for today:")
    for exercise in exercises:
        speak(exercise)

# Function to provide postpartum care tips
def postpartumCare():
    care_tips = [
        "Stay hydrated and eat nourishing foods.",
        "Take time for yourself to rest, even if it's just a few minutes during the day.",
        "Make sure to do pelvic floor exercises to help strengthen your muscles after childbirth.",
        "If you're experiencing any pain, don't hesitate to contact your healthcare provider.",
        "Engage in bonding time with your baby, and remember that it's okay to ask for help from others."
    ]
    speak("Here are some postpartum care tips:")
    for tip in care_tips:
        speak(tip)

# Function to give a dynamic breathing exercise for stress and low BP
def breathingExercise():
    speak("Let's do a breathing exercise to help with stress and low blood pressure.")
    
    # Inhale step (4 seconds)
    speak("Inhale deeply through your nose for a count of four.")
    time.sleep(4)  # Pause for 4 seconds while the user inhales
    
    # Hold breath (4 seconds)
    speak("Hold your breath for a count of four.")
    time.sleep(4)  # Pause for 4 seconds while the user holds breath
    
    # Exhale step (6 seconds)
    speak("Exhale slowly through your mouth for a count of six.")
    time.sleep(6)  # Pause for 6 seconds while the user exhales
    
    # Repeat the process for a few more breaths
    speak("Let's repeat this process for a few more breaths. Inhale through your nose.")
    time.sleep(4)  # Pause for inhalation
    
    speak("Hold your breath.")
    time.sleep(4)  # Pause for holding breath
    
    speak("Exhale slowly through your mouth.")
    time.sleep(6)  # Pause for exhalation
    
    # End with a calm statement
    speak("Great job! Focus on your breath, and relax your body.")

# Function to play music from the specified directory
def playMusic():
    music_dir = r"C:\Users\fazil\Music"  # Corrected path
    try:
        songs = [song for song in os.listdir(music_dir) if song.endswith(('.mp3', '.wav'))]
        if songs:
            song_to_play = songs[0]  # You can replace this with random.choice(songs) for random selection
            print(f"Playing: {song_to_play}")
            pygame.mixer.music.load(os.path.join(music_dir, song_to_play))
            pygame.mixer.music.play()
        else:
            speak("No music found in the directory.")  # Handle the error if the music directory is not found
    except FileNotFoundError:
        speak("Sorry, I couldn't find the music directory.")  # Catch other unexpected exceptions
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred while trying to play music.")

# Function to pause music
def pauseMusic():
    pygame.mixer.music.pause()
    speak("Music paused.")

# Function to resume music
def resumeMusic():
    pygame.mixer.music.unpause()
    speak("Resuming music.")

# Function to stop music
def stopMusic():
    pygame.mixer.music.stop()
    speak("Music stopped.")

# Main function to execute commands based on user input
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if 'play soothing music' in query or 'play music' in query:
            playMusic()

        elif 'pause music' in query:
            pauseMusic()

        elif 'resume music' in query:
            resumeMusic()

        elif 'stop music' in query:
            stopMusic()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'tell me a joke' in query or 'say a joke' in query:
            tellJoke()

        elif 'give me some exercises for today' in query:
            dailyExercise()

        elif 'postpartum care' in query:
            postpartumCare()

        elif 'breathing exercise for stress and low bp' in query or 'give me a breathing exercise' in query:
            breathingExercise()

        elif 'exit' in query or 'quit' in query or 'goodbye' in query:
            speak("Goodbye! Have a nice day.")
            break
