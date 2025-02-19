# Virtual-Assistant
# Personal Assistant Python Project

This is a personal assistant program built using Python. The assistant can perform various tasks such as searching Wikipedia, playing music, telling the time, opening websites, sending emails, and more. The assistant uses libraries like `pyttsx3`, `speech_recognition`, and `wikipedia`, among others.

## Features

1. **Text-to-Speech (TTS) Engine:**
   - The assistant can speak to the user, providing responses and feedback using the `pyttsx3` library.
   
2. **Voice Recognition:**
   - The assistant listens to commands from the user using the `speech_recognition` library.

3. **Task Automation:**
   - Search Wikipedia for a query and provide the summary.
   - Open websites such as YouTube, Google, and StackOverflow.
   - Play soothing music from a designated folder.
   - Fetch the current time.

4. **Email Functionality:**
   - Send emails via Gmail, after the user logs in with their credentials.
   
## Requirements

Before running the program, make sure you have the following libraries installed:

- `pyttsx3` (Text-to-Speech Engine)
- `speech_recognition` (Voice Recognition)
- `wikipedia` (Wikipedia API)
- `webbrowser` (Web Browser Control)
- `os` (Operating System Interface)
- `smtplib` (Send Emails)
- `getpass` (Securely Enter Passwords)

You can install the necessary libraries using `pip`:

```bash
pip install pyttsx3 speechrecognition wikipedia
