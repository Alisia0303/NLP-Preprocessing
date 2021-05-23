import re

class SentenceSegmentation:
    def __init__(self):
        pass

    def replace_email(self, paragraph):
        regex = r'[\w\.-]+@[\w\.-]+'
        emails = re.findall(regex,paragraph)
        for email in emails:
            paragraph = paragraph.replace(email[0], '')
        return paragraph

    def replace_url(self, paragraph):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        urls = re.findall(regex,paragraph)  
        for url in urls:
            paragraph = paragraph.replace(url[0], '')
        return paragraph

    def is_decimal(self, prechar, nextchar):
        if prechar.isnumeric() and nextchar.isnumeric():
            return True
        else:
            return False

    def is_count_number(self, prechar, nextchar):
        if prechar.isnumeric() and (nextchar == ' ' or nextchar == '\t'):
            return True

    def is_end_sentence(self, paragraph):
        lst_remove = []
        lst_dots = [i for i, ltr in enumerate(paragraph) if ltr == '.']
        for idx in lst_dots:
            if self.is_decimal(paragraph[idx-1], paragraph[idx+1]):
                lst_remove.append(idx)
            elif self.is_count_number(paragraph[idx-1], paragraph[idx+1]):
                lst_remove.append(idx)
        for char in lst_remove:
            paragraph = paragraph.replace(paragraph[char], '')
        return paragraph 

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

    