import re

class ParagraphSegmentation:
    def __init__(self, text, language):
        self.text = text
        self.language = language
        self.lst_latin_nums = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        self.lst_index_paragraph = []
        self.is_start = False
        self.is_end = False
        self.idx_start = 0
        self.idx_end = 0

    def is_start_paragraph(self, char, prechar, nextchar):
        if self.language == 'vietnamese':
            if (char.isupper()) and (prechar==' '):
                return True
            elif (char.isnumeric() or (char in self.lst_latin_nums)) and (nextchar in ['.', ')', ',']) and (prechar==' '):
                return True
            elif (char == '-') and (prechar==' '):
                return True
            else:
                return False
        elif self.language == 'english':
            if (char.isupper()) :
                return True
            elif (char.isnumeric() or (char in self.lst_latin_nums)) and (nextchar in ['.', ')', ',']) :
                return True
            elif (char == '-') :
                return True
            else:
                return False

    def is_end_paragraph(self, char, nextchar, nextnextchar):
        if self.language == 'vietnamese':
            if (char in ['.', ':', '?', '!']) and (nextchar == '\n') and (nextnextchar == ' '):
                return True
            elif (char == '\n') and (nextchar == '\n'):
                return True
            else:
                return False
        elif self.language == 'english':
            if (char in ['.', ':', '?', '!']) and (nextchar == '\n') :
                return True
            elif (char == '\n') and (nextchar == '\n'):
                return True
            else:
                return False

    def get_paragraphs(self):
        for idx in range(len(self.text)):
            if self.is_start == False: #find begin of paragraph
                if idx == 0:
                    self.is_start = self.is_start_paragraph(self.text[idx], None, self.text[idx+1])
                elif idx == len(self.text) - 1:
                    self.is_start = self.is_start_paragraph(self.text[idx], self.text[idx-1], None)
                else:
                    self.is_start = self.is_start_paragraph(self.text[idx], self.text[idx-1], self.text[idx+1])
                if self.is_start == True:
                    self.idx_start = idx
            elif self.is_start == True: # find end of paragraph
                if idx == len(self.text) - 1:
                    self.is_end = self.is_end_paragraph(self.text[idx], None, None)
                elif idx == len(self.text) - 2:
                    self.is_end = self.is_end_paragraph(self.text[idx], self.text[idx+1], None)
                else:
                    self.is_end = self.is_end_paragraph(self.text[idx], self.text[idx+1], self.text[idx+2])
                if (self.is_end == True) or (idx==(len(self.text) - 1)):
                    self.idx_end = idx
                    self.lst_index_paragraph.append([self.idx_start, self.idx_end])
                    self.is_start = False #reset variables to find new paragraph
                    self.is_end = False   #reset variables to find new paragraph
            
    def show_paragraphs(self):
        paragraph_contents = []
        for idx in self.lst_index_paragraph:
            paragraph_contents.append(self.text[idx[0]:idx[1]])
        print(self.lst_index_paragraph)
        return paragraph_contents

    def remove_count_number(self, text):
        pattern = r'[0-9(.|)|,]'
        return re.sub(pattern, '', text)

    

    

