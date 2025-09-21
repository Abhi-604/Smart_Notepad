# Smart Notepad

## Project Description  
Smart Notepad is a Python-based note-taking application designed for interactive use. It allows users to create, edit, and organize notes using both typing and speech, leveraging **speech-to-text conversion** to transcribe spoken input into text. The interface is built with Tkinter, the standard GUI toolkit for Python, providing a familiar desktop window with menus and buttons. The purpose of Smart Notepad is to streamline note-taking by combining traditional text editing with advanced features like speech transcription, on-the-fly language translation, and built-in data encryption for privacy. This makes it especially useful for students and developers who want a technical, feature-rich environment for managing their notes.

## Key Features  
- **Speech-to-Text Conversion:** Dictate notes by speaking into the microphone. The app uses a speech-recognition library to convert speech to text, enabling hands-free note-taking.  
- **Language Translation:** Translate notes between languages on demand using Google’s Translate API. The `googletrans` library provides free translation services in Python, so users can instantly convert a note’s language with a single command.  
- **Data Encryption:** Secure sensitive notes with encryption before saving. Smart Notepad uses the Caesar Cipher technique to encrypt and decrypt text, ensuring that stored notes remain confidential.  
- **Graphical User Interface:** A clean, intuitive GUI built with Tkinter offers menu options (File, Edit, Tools, Help) and buttons for all features. The design follows standard desktop-notepad layouts but adds controls for the advanced functions above.  
- **Database Backend:** Notes can be saved and retrieved from an Oracle database for persistence. The `cx_Oracle` (or `python-oracledb`) module is used to connect to Oracle DB instances, allowing notes metadata or credentials (eg, owner name, password) to be stored in a structured database table and the file is saved on the system, and when it is tried to open asks for the credentials to authenticate the owner.  
 

## Technologies Used  
- **Python:** The core programming language (Python 3.x).  
- **Tkinter:** Standard Python GUI toolkit for desktop applications.  
- **SpeechRecognition:** Python library for capturing audio and converting speech to text.  
- **pyaudio:** Required for microphone input.  
- **googletrans:** Free Python library for Google Translate API (language translation).  
- **cryptography:** Python library offering encryption primitives (used here for note encryption).   
- **Oracle Database (cx_Oracle or oracledb):** Database backend for storing note credentials used to access the file, accessed via Python’s cx_Oracle module.  
- **Other Utilities:** Standard libraries and any required third-party packages listed in `requirements.txt`.  

## Setup and Installation  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/Abhi-604/Smart_Notepad.git
   cd Smart_Notepad
   ```  
2. **Install dependencies:** (It’s recommended to use a virtual environment.)  
   ```bash
   python -m venv venv
   source venv/bin/activate       # (or `venv\Scripts\activate` on Windows)
   pip install -r requirements.txt
   ```  
   This will install required libraries such as Tkinter (usually included with Python), `speechrecognition`, `pyaudio`, `googletrans`, and `cx_Oracle`, among others.  
3. **Configure Database:** Ensure an Oracle database is accessible. Create a table (e.g., `notes`) for storing the note metadata. Update the database connection parameters in the code or a config file (username, password, DSN).  
4. **Run the application:**  
   ```bash
   python NotePadView.py
   ```  
   (Or double-click the executable if packaged.) The Smart Notepad window should appear.  

## Usage  
After launching Smart Notepad, you can use its features as follows:  

- **Typing and Editing:** Start a new note by typing into the text area. Use the menu (File → New/Open/Save) or toolbar buttons to create, open, and save notes.  
- **Speech-to-Text Input:** Click the “Record” or microphone button and speak clearly. The `speech_recognition` library will capture the audio and insert the transcribed text into the note.  
- **Translation:** To translate the current note, click the “Translate” button and select a target language (e.g., French, Spanish). Internally, the app uses `googletrans`. For example:  
  ```python
  from googletrans import Translator

  translator = Translator()
  result = translator.translate("Hello, world!", dest="es")
  print(result.text)  # 'Hola, mundo'
  ```  
- **Encryption:** Before saving, you can encrypt the note. 
  This protects the note text in storage. Only the correct key will decrypt it later.  
- **Viewing Notes:** Encrypted notes can be decrypted by entering the key when opening. Translated notes can be switched back to the original language.  
 

## Target Audience  
Smart Notepad is intended for computer science students, developers, or technically proficient users who want a powerful note-taking tool. Its feature set (speech-to-text handling, database usage, and encryption) assumes a technical background. This project serves as both a productivity app and a learning example for combining GUI programming with advanced Python libraries.


##Project screenshots

First UI window:
<img width="1103" height="653" alt="image" src="https://github.com/user-attachments/assets/7bb1231a-e8b1-455d-a1eb-225e730c793b" />

File Module:
<img width="974" height="810" alt="image" src="https://github.com/user-attachments/assets/a4514fa6-2076-48ab-9eb5-0df494b2dd12" />

Edit Module:
<img width="1020" height="607" alt="image" src="https://github.com/user-attachments/assets/a6534499-7da4-49d1-affd-a34c9469f2ce" />

View Module:
<img width="1020" height="607" alt="image" src="https://github.com/user-attachments/assets/34ca59f6-1621-411c-8df2-9950ced6f0ef" />

Color Theme:
<img width="999" height="682" alt="image" src="https://github.com/user-attachments/assets/14f91ecd-4ace-499a-b4c8-a323179b55f2" />


Secure Files:
<img width="1020" height="604" alt="image" src="https://github.com/user-attachments/assets/a747cf20-156d-455f-a898-2c70f71b788b" />

Font Color:
<img width="1020" height="604" alt="image" src="https://github.com/user-attachments/assets/ce8b6bad-bfc9-46ff-9081-73d0170de3e0" />


Language Translator 1:
<img width="1020" height="670" alt="image" src="https://github.com/user-attachments/assets/9062e0c2-032a-4abb-ac5a-0d4351489bcb" />

Language Translator 2:
<img width="1020" height="578" alt="image" src="https://github.com/user-attachments/assets/162f6cf3-0c60-4a6e-a9c6-f10ab23721eb" />

Open file:
<img width="1020" height="662" alt="image" src="https://github.com/user-attachments/assets/36a1c716-d92b-43ef-8c58-703a6772fd4a" />


Find and Replace:
<img width="1147" height="805" alt="image" src="https://github.com/user-attachments/assets/05a1afb3-a3eb-4203-9e9d-4f7190b8eabf" />

Change Theme:
<img width="1020" height="616" alt="image" src="https://github.com/user-attachments/assets/10c4ba38-cb74-42e7-968e-4b8e51c993f7" />


