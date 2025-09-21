# Smart Notepad

## Project Description

Smart Notepad is a Python-based note-taking application designed for
interactive
use[\[1\]](https://mrs0lver.github.io/PortFolio/#:~:text=This%20Python,interactively).
It allows users to create, edit, and organize notes using both typing
and speech, leveraging voice recognition to transcribe spoken input and
text-to-speech to read notes aloud. The interface is built with Tkinter,
the standard GUI toolkit for
Python[\[2\]](https://docs.python.org/3/library/tkinter.html#:~:text=The%20tkinter%20%20package%20,well%20as%20on%20Windows%20systems),
providing a familiar desktop window with menus and buttons. The purpose
of Smart Notepad is to streamline note-taking by combining traditional
text editing with advanced features like speech transcription,
on-the-fly language translation, and built-in data encryption for
privacy. This makes it especially useful for students and developers who
want a technical, feature-rich environment for managing their notes.

## Key Features

-   **Voice Recognition:** Dictate notes by speaking into the
    microphone. The app uses a speech-recognition library to convert
    speech to text, enabling hands-free
    note-taking[\[3\]](https://realpython.com/python-speech-recognition/#:~:text=The%20flexibility%20and%20ease,if%20SpeechRecognition%20will%20work%20in).
-   **Text-to-Speech:** Have the app read your notes aloud using a TTS
    engine (e.g. `pyttsx3` or similar), improving accessibility.
-   **Language Translation:** Translate notes between languages on
    demand using Google's Translate API. The `googletrans` library
    provides free translation services in
    Python[\[4\]](https://py-googletrans.readthedocs.io/en/latest/#:~:text=Googletrans%20is%20a%20free%20and,methods%20as%20detect%20and%20translate),
    so users can instantly convert a note's language with a single
    command.
-   **Data Encryption:** Secure sensitive notes with encryption before
    saving. Smart Notepad uses the Python `cryptography` library to
    encrypt and decrypt text (e.g. using symmetric Fernet
    encryption)[\[5\]](https://cryptography.io/en/latest/#:~:text=,high%20level%20symmetric%20encryption%20recipe),
    ensuring that stored notes remain confidential.
-   **Graphical User Interface:** A clean, intuitive GUI built with
    Tkinter[\[2\]](https://docs.python.org/3/library/tkinter.html#:~:text=The%20tkinter%20%20package%20,well%20as%20on%20Windows%20systems)
    offers menu options (File, Edit, Tools, Help) and buttons for all
    features. The design follows standard desktop-notepad layouts but
    adds controls for the advanced functions above.
-   **Database Backend:** Notes can be saved and retrieved from an
    Oracle database for persistence. The `cx_Oracle` (or
    `python-oracledb`) module is used to connect to Oracle DB
    instances[\[6\]](https://cx-oracle.readthedocs.io/en/8.1/user_guide/introduction.html#:~:text=cx_Oracle%20is%20a%20Python%20extension,and%20a%20couple%20of%20exclusions),
    allowing notes to be stored in a structured database table rather
    than flat files.
-   **Image Capture (OpenCV):** Support for image-based notes or OCR. By
    integrating OpenCV (a leading computer vision
    library[\[7\]](https://opencv.org/#:~:text=OpenCV%20is%20the%20world%27s%20biggest,computer%20vision%20library)),
    Smart Notepad can capture images (e.g. screenshots or photos of
    handwritten notes) and process them (for example, extract text via
    OCR) to include in notes.

## Technologies Used

-   **Python:** The core programming language (Python 3.x).
-   **Tkinter:** Standard Python GUI toolkit for desktop
    applications[\[2\]](https://docs.python.org/3/library/tkinter.html#:~:text=The%20tkinter%20%20package%20,well%20as%20on%20Windows%20systems).
-   **SpeechRecognition:** Python library for capturing audio and
    converting speech to
    text[\[3\]](https://realpython.com/python-speech-recognition/#:~:text=The%20flexibility%20and%20ease,if%20SpeechRecognition%20will%20work%20in).
-   **pyttsx3/gTTS (optional):** Libraries for text-to-speech (TTS) to
    read notes aloud.
-   **googletrans:** Free Python library for Google Translate API
    (language
    translation)[\[4\]](https://py-googletrans.readthedocs.io/en/latest/#:~:text=Googletrans%20is%20a%20free%20and,methods%20as%20detect%20and%20translate).
-   **cryptography:** Python library offering encryption primitives
    (used here for note
    encryption)[\[5\]](https://cryptography.io/en/latest/#:~:text=,high%20level%20symmetric%20encryption%20recipe).
-   **OpenCV:** Open Source Computer Vision Library for image
    processing[\[7\]](https://opencv.org/#:~:text=OpenCV%20is%20the%20world%27s%20biggest,computer%20vision%20library).
-   **Oracle Database (cx_Oracle or oracledb):** Database backend for
    storing notes, accessed via Python's cx_Oracle
    module[\[6\]](https://cx-oracle.readthedocs.io/en/8.1/user_guide/introduction.html#:~:text=cx_Oracle%20is%20a%20Python%20extension,and%20a%20couple%20of%20exclusions).
-   **Other Utilities:** Standard libraries (e.g. `threading` for
    concurrency, `pyaudio` for microphone audio input, etc.) and any
    required third-party packages listed in `requirements.txt`.

## Setup and Installation

1.  **Clone the repository:**

-   git clone https://github.com/Abhi-604/Smart_Notepad.git
        cd Smart_Notepad

2.  **Install dependencies:** (It's recommended to use a virtual
    environment.)

-   python -m venv venv
        source venv/bin/activate       # (or `venv\Scripts\activate` on Windows)
        pip install -r requirements.txt

    This will install required libraries such as Tkinter (usually
    included with Python), `speechrecognition`, `pyttsx3`,
    `googletrans`, `cryptography`, `opencv-python`, and `cx_Oracle`,
    among others.

3.  **Configure Database:** Ensure an Oracle database is accessible.
    Create a table (e.g. `notes`) for storing the note data. Update the
    database connection parameters in the code or a config file
    (username, password, DSN).
4.  **Run the application:**

-   python Smart_Notepad.py

    (Or double-click the executable if packaged.) The Smart Notepad
    window should appear.

## Usage

After launching Smart Notepad, you can use its features as follows:

-   **Typing and Editing:** Start a new note by typing into the text
    area. Use the menu (File → New/Open/Save) or toolbar buttons to
    create, open, and save notes.
-   **Voice Input:** Click the "Record" or microphone button and speak
    clearly. The `speech_recognition` library will capture the audio and
    insert the transcribed text into the
    note[\[3\]](https://realpython.com/python-speech-recognition/#:~:text=The%20flexibility%20and%20ease,if%20SpeechRecognition%20will%20work%20in).
-   **Translation:** To translate the current note, click the
    "Translate" button and select a target language (e.g. French,
    Spanish). Internally, the app uses `googletrans`. For example:

```{=html}
<!-- -->
```
-   from googletrans import Translator

        translator = Translator()
        result = translator.translate("Hello, world!", dest="es")
        print(result.text)  # 'Hola, mundo'

    This converts "Hello, world!" to
    Spanish[\[8\]](https://py-googletrans.readthedocs.io/en/latest/#:~:text=,pronunciation%3DGood%20evening).

```{=html}
<!-- -->
```
-   **Encryption:** Before saving, you can encrypt the note. For
    instance, using the `cryptography` library:

```{=html}
<!-- -->
```
-   from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        cipher = Fernet(key)
        token = cipher.encrypt(b"Sensitive note")
        print(cipher.decrypt(token))  # b'Sensitive note'

    This protects the note text in
    storage[\[5\]](https://cryptography.io/en/latest/#:~:text=,high%20level%20symmetric%20encryption%20recipe).
    Only the correct key will decrypt it later.

```{=html}
<!-- -->
```
-   **Viewing Notes:** Encrypted notes can be decrypted by entering the
    key when opening. Translated notes can be switched back to the
    original language.
-   **Additional Tools:** Use built-in options to capture images (via
    webcam or screenshot) and insert them into notes, leveraging OpenCV;
    or right-click for context actions.

## Target Audience

Smart Notepad is intended for computer science students, developers, or
technically proficient users who want a powerful note-taking tool. Its
feature set (programmatic voice/speech handling, database usage, and
encryption) assumes a technical background. This project serves as both
a productivity app and a learning example for combining GUI programming
with advanced libraries in Python.
