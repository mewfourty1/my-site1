import requests
from bs4 import BeautifulSoup
from typing import List
def get_challenge_best50(_url:str)->List:
    top50=[]
    for page in range(1,4):

        url = _url+ "&page="+str(page)

        res=requests.get(url)
        soup = BeautifulSoup(res.text,'lxml')

        webtoons = soup.select(".challengeList td>.challengeInfo")
        titles = [w.select_one(".challengeTitle")for w in webtoons]
        titles = [t.text.replace('\n','')for t in titles]
        titles = [t.strip() for t in titles]

        scores = [w.select_one('.rating_type>strong')for w in webtoons]
        scores = [float(s.text) for s in scores]

        # 해당 url에서 썸네일의 img 태그를 가져온다.
        images = soup.select(".challengeList td>.fl img")
        # 썸네일의 img 태그에서 src 속성만 가져온다.
        images = [img['src'] for img in images]

        info = list(zip(images,titles,scores))
        top50+=info
    return top50[:50]


if __name__ == "__main__":

    view_count_url="https://comic.naver.com/genre/bestChallenge?m=main&order=ViewCount"
    star_score_url="https://comic.naver.com/genre/bestChallenge?m=main&order=StarScore"
    view_count50=get_challenge_best50(view_count_url)
    star_score50=get_challenge_best50(star_score_url)

    view_count50_order_score = sorted(view_count50,key=lambda x:x[1],reverse=True)
    print("challenge best 50")
    print(view_count50)
    print("challenge score 50")
    print(view_count50_order_score)
    print("score 50")
    view_score_50 = set(star_score50) & set(star_score50)
    print(list(view_score_50))
