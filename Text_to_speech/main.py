#credentials[C:\Users\melin\AppData\Roaming\gcloud\application_default_credentials.json]

# """Synthesizes speech from the input string of text or ssml.Make sure to be working in a virtual environment.
# Note: ssml must be well-formed according to:
# https://www.w3.org/TR/speech-synthesis/

# importing required classes
from pypdf import PdfReader
from google.cloud import texttospeech

booktext=" "

# creating a pdf reader object
reader = PdfReader('Blackjack_Flowchart.pdf')

# printing number of pages in pdf file
length = len(reader.pages)

for page_nr in range(length):
    # creating a page object
    page = reader.pages[page_nr]
    bookpage = page.extract_text()
    booktext += bookpage

print(booktext)

#GOOGLE TEXT TO SPEECH SETUP
# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=f"{booktext}")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')