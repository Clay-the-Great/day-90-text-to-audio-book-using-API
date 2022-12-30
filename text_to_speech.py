import PyPDF2
from gtts import gTTS
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Read from PDF
pdf_page_number = 0
pdf_file_name = "ICC2"
with open(f"text/{pdf_file_name}.pdf", "rb") as text_file:
    pdf_reader = PyPDF2.PdfReader(text_file)
    page_object = pdf_reader.pages[pdf_page_number]
    text_pdf = page_object.extract_text()


# Read from EPUB
def chapter_to_string(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), "html.parser")
    text = [paragraph.get_text() for paragraph in soup.find_all("p")]
    # return text[0]
    return " ".join(text)


epub_file_name = "Frank_Dikotter_The_Cultural_Revolution_A_People’s_History,_1962.epub"
book = epub.read_epub(f"text/{epub_file_name}")
chapters = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
chapter_names = [chapter.get_name() for chapter in chapters]
epub_chapters_text = [chapter_to_string(chapter) for chapter in chapters]
# epub_chapter1 = chapter_to_string(chapters[4])

# Make audio file
audio = gTTS(epub_chapters_text[5], lang='en', tld="ca")  # Voice in Canadian English
audio.save(f'audio/{epub_file_name}.mp3')
