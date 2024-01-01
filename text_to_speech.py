import pyttsx4
from pypdf import PdfReader


def audio_book(text_to_speak, voice_played, saved_file):
    # Initialize the text-to-speech engine
    engine = pyttsx4.init()

    # Set the speech rate (optional)
    engine.setProperty("rate", 150)

    # Set the speech in telugu language
    engine.setProperty("voice", 'te')

    # Set the voice (optional, you can omit this line to use the default voice)
    # engine.getProperty("voices")[0].id => Default and Male Voice
    # engine.getProperty("voices")[1].id => Female Voice

    if voice_played != "Female":
        voice_property = engine.getProperty("voices")[0].id
    else:
        voice_property = engine.getProperty("voices")[1].id

    engine.setProperty("voice", voice_property)

    # Convert the text to speech
    # engine.say(text_to_speak)

    # Save the Text file into Mp3 Format.
    engine.save_to_file(text_to_speak, path + saved_file)

    # Wait for the speech to finish
    engine.runAndWait()


path = "C:\\Users\\Palli Chandra Sekhar\\Desktop\\TTS\\"
# reader = PdfReader(path+"Chapter 1 Supergene.pdf")
reader = PdfReader(path+"Chapter_ONE_TELUGU_VERSION_SUPERGENE.pdf")
number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
print("number of pgs : ", number_of_pages)
text = ''
for i in range(number_of_pages):
    page = reader.pages[i]
    text += page.extract_text()

# print("Text in pdf : ", text)
# text = "Hey, Chuunchi Muuthee, Akkada Unnaav?"
# f = open('demo.txt', 'w')
# f.write(text)
# f.close()

voice_type = "Female"
# File name should be with .extension
file_name = "SuperGene_Chapter_1.mp3"
audio_book(text, voice_type, file_name)
