from basic_cleaner import clean
from organic_keywords import organic_keywords_extractor
from summa import summarizer



with open("urls.txt", "r") as f1 , open("keywords.txt", "w") as keywords, open("summary.txt", 'w') as content:
    urls= f1.readlines()
    for url in urls:
        url= url.replace('\n', '')
        print(url)
        organic_keywords= organic_keywords_extractor.extract_organic_keywords(url)
        # print(organic_keywords)

        text= clean(url)
        summary= summarizer.summarize(text, words=100)
        summary= summary.replace('\n', ' ')
        
        keywords.write(str(organic_keywords)+'\n')
        content.write(summary+'\n')