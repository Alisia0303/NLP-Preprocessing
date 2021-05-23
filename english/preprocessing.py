from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from utils.clean import CleanData

class PreProcessing(CleanData):
    def __init__(self, text):
        self.text = text

    def step_clean(self):
        textRemoveHTMLTag = self.remove_html_tags(self.text)
        textRemoveSpecialCharacter = self.remove_special_characters_eng(textRemoveHTMLTag)
        self.text = textRemoveSpecialCharacter

    def show_text(self):
        return self.text