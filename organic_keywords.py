
import http.client
import json


# conn = http.client.HTTPSConnection("www.spyfu.com")

# # headers = { 'Authorization': "Basic REPLACE_BASIC_AUTH" }
# headers = { 'Authorization': "b57ebffc-6753-4d8c-b832-6bfcc8067d7b:NNXIHRGE" }

# conn.request("GET", "/apis/serp_api/v2/seo/getMostValuableKeywords?query=https://www.headphonesty.com/2018/11/best-cat-ear-headphones/&sortBy=rank&sortOrder=Ascending&pageSize=10000", headers=headers)

# res = conn.getresponse()
# data = res.read()




class OrganicKeywords:
    def __init__(self) -> None:
        self.conn= http.client.HTTPSConnection("www.spyfu.com")
        self.headers = { 'Authorization': "b57ebffc-6753-4d8c-b832-6bfcc8067d7b:NNXIHRGE" }

    def extract_organic_keywords(self, url):
        self.conn.request(
            "GET",
            f"/apis/serp_api/v2/seo/getMostValuableKeywords?query={url}&sortBy=rank&sortOrder=Ascending&pageSize=10000", 
            headers=self.headers
            )
        res= self.conn.getresponse()
        data= res.read()
        data= data.decode("utf-8")


        keywords= []

        data= json.loads(data)
        for d in data['results']:
            # if d['rank']<=10:
            if d['rank']<=15:
                keywords.append(d['keyword'])
        return keywords



organic_keywords_extractor= OrganicKeywords()
  

