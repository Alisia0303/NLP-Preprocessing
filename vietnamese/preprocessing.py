from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from utils.clean import CleanData
from utils.paragraph_segmentation import ParagraphSegmentation
from utils.sentence_segmentation import SentenceSegmentation

class PreProcessing(CleanData, ParagraphSegmentation, SentenceSegmentation):
    def __init__(self, text):
        self.text = text
        ParagraphSegmentation.__init__(self, self.text, 'vietnamese')

    def step_clean(self):
        textRemoveHTMLTag = self.remove_html_tags(self.text)
        textRemoveSpecialCharacter = self.remove_special_characters_vn(textRemoveHTMLTag)
        self.text = textRemoveSpecialCharacter

    def step_paragraph_segmentation(self):
        self.get_paragraphs()
        paragraphs = self.show_paragraphs()
        return paragraphs

    def step_sentence_segmentation(self, paragraphs):
        new_sentences = []
        for paragraph in paragraphs:
            paragraph = self.replace_email(paragraph)
            paragraph = self.replace_url(paragraph)
            paragraph = self.is_end_sentence(paragraph)
            paragraph_remove_number = self.remove_numbers_vn(paragraph)
            paragraph_remove_extra_whitespace = self.remove_extra_whitespace_tabs(paragraph_remove_number)
            paragraph_to_lowercase = self.to_lowercase(paragraph_remove_extra_whitespace)
            sentences = paragraph_to_lowercase.split('.')
            for sentence in sentences:
                if (sentence == ' ') or (sentence == '') or (sentence == '\t'):
                    pass
                else:
                    new_sentences.append(sentence)
        return new_sentences

    def show_text(self):
        return self.text