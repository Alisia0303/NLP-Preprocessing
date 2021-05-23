from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from utils.clean import CleanData
from utils.paragraph_segmentation import ParagraphSegmentation

class PreProcessing(CleanData, ParagraphSegmentation):
    def __init__(self, text):
        self.text = text
        ParagraphSegmentation.__init__(self, self.text, 'english')

    def step_clean(self):
        textRemoveHTMLTag = self.remove_html_tags(self.text)
        textRemoveSpecialCharacter = self.remove_special_characters_eng(textRemoveHTMLTag)
        self.text = textRemoveSpecialCharacter

    def step_paragraph_segmentation(self):
        self.get_paragraphs()
        paragraphs = self.show_paragraphs()
        new_paragraphs = []
        for paragraph in paragraphs:
            paragraph_remove_count_number = self.remove_count_number(paragraph)
            paragraph_remove_number = self.remove_numbers_eng(paragraph_remove_count_number)
            paragraph_remove_extra_whitespace_tabs = self.remove_extra_whitespace_tabs(paragraph_remove_number)
            paragraph_to_lowercase = self.to_lowercase(paragraph_remove_extra_whitespace_tabs)
            new_paragraphs.append(paragraph_to_lowercase)
        return new_paragraphs

    def show_text(self):
        return self.text