#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from preprocessing import PreProcessing

if __name__ == "__main__":
    sample_text = """
                    <html> <body>
 BIẾT ƠN 123456.
 Cảm giác luôn là sự biết ơn, vì khi đi vào Sài Gòn đông đúc này, 
mới nhận ra rằng quanh mình luôn có những người yêu thương, quan tâm, giúp đỡ và luôn dõi theo.
 Không được ở chung với gia đình mới thấy rằng gia đình là nơi yêu thương vô điều 
kiện. Mỗi lần FaceTime là Ba lúc nào cũng nói “ Răng bữa ni mập rứa con, mập rứa ko ai ưa mô, https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles coi giảm cân đi nghe”.
    
    Trước đây rất ít khi thấy Ba nói ra những câu như vậy, chắc do con gái đi xa nên Ba lo hihi. 

 Còn bà chị già khó tính của tui là lúc mô cũng nhắc rửa tay:
  1. aaaa
  2. bbbbbbb
  3. ccccccccc
 
                    </body></html>
                """
    
    process = PreProcessing(sample_text)
    process.step_clean()
    cleantext = process.show_text()
    print("==========TEXT AFTER CLEAN STEP============")
    print(cleantext)
    paragraphs = process.step_paragraph_segmentation()
    print("==========TEXT AFTER PARAGRAPH SEGMENTATION==========")
    print(paragraphs)
    sentences = process.step_sentence_segmentation(paragraphs)
    print("==========TEXT AFTER SENTENCE SEGMENTATION===========")
    print(sentences)
