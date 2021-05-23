from inspect import getsourcefile
import os.path
import sys
import re
from bs4 import BeautifulSoup


class CleanData:
    def __init__(self):
        pass

    # function to remove HTML tags
    def remove_html_tags(self, text):
        return BeautifulSoup(text, 'html.parser').get_text()

    
    # function to remove special characters
    def remove_special_characters_eng(self, text):
        pattern = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 
        return re.sub(pattern, '', text)

    def remove_special_characters_vn(self, text):
        pattern = r'[^a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđA-ZÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÍÌỈĨỊÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴĐ0-9.,!?/:;\"\'\s]' 
        return re.sub(pattern, '', text)

    # function to remove numbers
    def remove_numbers_vn(self, text):
        pattern = r'[^a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđA-ZÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÍÌỈĨỊÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴĐ.,!?/:;\"\'\s]' 
        return re.sub(pattern, '', text)

    def remove_numbers_eng(self, text):
        pattern = r'[^a-zA-z.,!?/:;\"\'\s]'
        return re.sub(pattern, '', text)

    # function to remove extra whitespace tabs
    def remove_extra_whitespace_tabs(self, text):
        pattern = r'^\s*|\s\s*'
        return re.sub(pattern, ' ', text).strip()

    # function to convert string to lowercase
    def to_lowercase(self, text):
        return text.lower()

    