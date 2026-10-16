
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import time

r = sr.Recognizer()

phone_numbers = {
    "jane": "+98 65236585",
    "jenny": "+98 65236585",
    "samy": "+98 65236585"
}

bank_account_numbers = {
    "jane": "25645268651",
    "jenny": "2564856245"
}


def speak(command):
    engine = pyttsx3.init()
    engine.setProperty("voice", engine.getProperty("voices")[0].id)
    engine.say(str(command))
    engine.runAndWait()
    engine.stop()


def commands():
    try:
        with sr.Microphone() as source:
            print("Adjusting for background noise...")
            r.adjust_for_ambient_noise(source, duration=0.8)

            print("Listening... Ask now.")

            try:
                audioin = r.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )
            except sr.WaitTimeoutError:
                print("No speech detected. Try again.")
                return

    except OSError as error:
        print(f"Microphone error: {error}")
        print("Check your microphone and input device.")
        time.sleep(2)
        return

    try:
        my_text = r.recognize_google(audioin).lower().strip()
        print("You said:", my_text)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return

    except sr.RequestError as error:
        print(f"Speech recognition service error: {error}")
        print("Check your internet connection.")
        time.sleep(2)
        return

    # Ask about a person
    if "who is" in my_text:
        person = my_text.replace("who is", "", 1).strip()

        try:
            info = wikipedia.summary(person, sentences=1)
            speak(info)

        except wikipedia.exceptions.DisambiguationError:
            speak("There are several results. Please be more specific.")

        except wikipedia.exceptions.PageError:
            speak("I could not find that person on Wikipedia.")

        except Exception as error:
            print(f"Wikipedia error: {error}")

    # Ask for a phone number
    elif "phone number" in my_text:
        found = False

        for name, number in phone_numbers.items():
            if name in my_text:
                speak(f"{name} phone number is {number}")
                found = True
                break

        if not found:
            speak("I could not find that contact.")

    # Ask for a bank account number
    elif "account number" in my_text:
        found = False

        for name, number in bank_account_numbers.items():
            if name in my_text:
                speak(f"{name} bank account number is {number}")
                found = True
                break

        if not found:
            speak("I could not find that account.")

    # Play a song on YouTube
    elif my_text.startswith("play "):
        song = my_text.replace("play", "", 1).strip()

        if song:
            speak(f"Playing {song}")
            try:
                pywhatkit.playonyt(song)
            except Exception as error:
                print(f"YouTube playback error: {error}")
                speak("Sorry, I could not play that song.")

    # Ask for the time
    elif "time" in my_text:
        timenow = datetime.datetime.now().strftime("%H:%M")
        speak(timenow)

    # Ask for the date
    elif "date" in my_text:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(today)

    else:
        speak("Please ask a supported question.")


if __name__ == "__main__":
    print("Voice assistant started. Press Ctrl+C to stop.")

    try:
        while True:
            commands()

    except KeyboardInterrupt:
        print("\nVoice assistant stopped.")
