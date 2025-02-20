# Virtual-Assistant
## Personal Assistant Python Project
This is a personal assistant program built using Python. The assistant can perform various tasks such as searching Wikipedia, playing music, telling the time, opening websites, sending emails, and more. The assistant uses libraries like pyttsx3, speech_recognition, and wikipedia, among others.

## Features
Text-to-Speech (TTS) Engine:

The assistant can speak to the user, providing responses and feedback using the pyttsx3 library.
Voice Recognition:

The assistant listens to commands from the user using the speech_recognition library.
Task Automation:

Search Wikipedia for a query and provide the summary.
Open websites such as YouTube, Google, and StackOverflow.
Play soothing music from a designated folder.
Fetch the current time.
Email Functionality:

Send emails via Gmail, after the user logs in with their credentials.
Requirements
### Before running the program, make sure you have the following libraries installed:

pyttsx3 (Text-to-Speech Engine)
speech_recognition (Voice Recognition)
wikipedia (Wikipedia API)
webbrowser (Web Browser Control)
os (Operating System Interface)
smtplib (Send Emails)
getpass (Securely Enter Passwords)
You can install the necessary libraries using pip:

bash
Copy
pip install pyttsx3 speechrecognition wikipedia
List of Commands
## Here is a list of commands that your assistant understands based on the script:

### Music Commands:
"Play soothing music"
"Play music"
"Pause music"
"Resume music"
"Stop music"
### Time Commands:
"The time" (Tells the current time)
### Joke Commands:
"Tell me a joke"
"Say a joke"
### Exercise and Health Commands:
"Give me some exercises for today"
"Postpartum care"
"Breathing exercise for stress and low BP"
"Give me a breathing exercise"
### Exit Commands:
"Exit"
"Quit"
"Goodbye"
These commands trigger specific actions like playing music, telling a joke, or guiding the user through an exercise. You can always add more by modifying the if conditions in the while loop to handle new commands.

This version contains all of the commands as you requested while keeping the rest of the file unchanged. Let me know if you need further modifications!
