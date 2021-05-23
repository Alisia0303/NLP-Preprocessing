
from preprocessing import PreProcessing

if __name__ == "__main__":
    sample_text = """
        ADD MORE: 1234456 <head> Thuy Hang </head>
        These steps should give you a good idea about how to build your clean-up and pre-processing strategies. 
        After these pre-processing steps, the corpus of text is ready for NLP algorithms such as Word2Vec, GloVe etc. These pre-processing steps will definitely improve the model’s accuracy.

        Hope you liked this article, and if so, then please say so in comments. If you would like to share any suggestion on any approach, then feel free to say so in comments and I will revert right away.
    """

    process = PreProcessing(sample_text)
    process.step_clean()
    cleantext = process.show_text()
    print("==========TEXT AFTER CLEAN STEP============")
    print(cleantext)
