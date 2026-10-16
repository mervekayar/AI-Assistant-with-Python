# AI Voice Assistant 🎙️

A Python-based voice assistant that listens to voice commands and performs various tasks using speech recognition and text-to-speech technologies.

## Features

- 🎤 **Voice Recognition:** Recognizes spoken commands using Google Speech Recognition.
- 🔊 **Text-to-Speech:** Responds verbally using `pyttsx3`.
- 🌐 **Wikipedia Search:** Retrieves brief information about people and topics.
- 📞 **Contact Lookup:** Provides stored phone numbers for predefined contacts.
- 🏦 **Bank Account Lookup:** Retrieves predefined account numbers.
- 🎵 **YouTube Music Playback:** Searches for and plays songs on YouTube using `pywhatkit`.
- 🕒 **Time and Date:** Announces the current time and date.

## Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- PyWhatKit
- Wikipedia API
- datetime

## Installation

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Install the required dependencies:

   ```bash
   pip install SpeechRecognition PyAudio pyttsx3 pywhatkit wikipedia
   ```

3. Make sure your microphone is connected and accessible.

4. Run the Python script:

   ```bash
   python ai_assisstant.py
   ```

## Usage

Run the script and speak a command, such as:

- "Who is Albert Einstein?"
- "What is Jane's phone number?"
- "Play Bohemian Rhapsody."
- "What time is it?"
- "What is the date?"

The assistant processes the command and responds with speech or performs the requested action.

## Notes

- An active internet connection is required for Google Speech Recognition, Wikipedia searches, and YouTube playback.
- Microphone access and PyAudio must be configured correctly.
- Contact and bank account information is stored locally in dictionaries for demonstration purposes. Use fictional data and never publish sensitive personal or financial information in a public repository.

## Future Improvements

- Add more voice commands.
- Improve error handling and speech recognition.
- Add a wake-word feature.
- Integrate additional APIs and smart assistant capabilities.

## License

This project is intended for educational purposes.
