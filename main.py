import pyttsx3
import PyPDF3


pdfreader = PyPDF3.PdfFileReader(open("aaa - Copy.pdf", "rb"))
speaker = pyttsx3.init()
rate = speaker.getProperty("rate")
speaker.setProperty("rate", rate - 70)
voices = speaker.getProperty("voices")
speaker.setProperty("voice", voices[0].id)

text = ""
for page_num in range(pdfreader.numPages):
    page = pdfreader.getPage(page_num)
    text += page.extractText()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)

speaker.save_to_file(clean_text, "story.mp3")
speaker.runAndWait()

speaker.stop()


