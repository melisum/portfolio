#credentials[C:\Users\melin\AppData\Roaming\gcloud\application_default_credentials.json]

# """Synthesizes speech from the input string of text or ssml.Make sure to be working in a virtual environment.
# Note: ssml must be well-formed according to:
# https://www.w3.org/TR/speech-synthesis/

# importing required classes
from pypdf import PdfReader
from gtts import gTTS

booksnippet=" "

# creating a pdf reader object
reader = PdfReader('Weddings_Pregnancies_and.pdf')

# printing number of pages in pdf file
length = len(reader.pages)


#the book is quite long, so let´s only work with a snippet
for page_nr in range(25,28):
    # creating a page object
    page = reader.pages[page_nr]
    #change to text
    bookpage = page.extract_text()
    booksnippet += bookpage

print(booksnippet)

tts = gTTS(text=booksnippet, lang="en", slow=False)
tts.save('audiobook.mp3')


