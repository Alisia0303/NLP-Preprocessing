#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from preprocessing import PreProcessing

if __name__ == "__main__":
    sample_text = """
                    <html> <body>
                    BIẾT ƠN 123456
                    Cảm giác luôn là sự biết ơn, vì khi đi vào Sài Gòn đông đúc này, mới nhận ra rằng quanh mình luôn có những người yêu thương, quan tâm, giúp đỡ và luôn dõi theo. 
                    Không được ở chung với gia đình mới thấy rằng gia đình là nơi yêu thương vô điều kiện. Mỗi lần FaceTime là Ba lúc nào cũng nói “ Răng bữa ni mập rứa con, mập rứa ko ai ưa mô, coi giảm cân đi nghe” 
                    Trước đây rất ít khi thấy Ba nói ra những câu như vậy, chắc do con gái đi xa nên Ba lo hihi. 
                    Còn bà chị già khó tính của tui là lúc mô cũng nhắc rửa tay, uống nước cam, dặn lo phòng dịch... và thế là bà chị ko tin tưởng tui gửi vào Sài gòn cho con bé HECTOR SÂM để tăng sức đề kháng mùa dịch này
                    </body></html>
                """
    
    process = PreProcessing(sample_text)
    process.step_clean()
    cleantext = process.show_text()
    print("==========TEXT AFTER CLEAN STEP============")
    print(cleantext)
