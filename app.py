from flask import Flask,render_template
from naver_webtoon_best import get_challenge_best50
from get_weather_info import get_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/webtoons')
def webtoons():
    star_score_url = "https://comic.naver.com/genre/bestChallenge?m=main&order=StarScore"
    view_count_url = "https://comic.naver.com/genre/bestChallenge?m=main&order=ViewCount"
    views = get_challenge_best50(view_count_url)
    stars = get_challenge_best50(star_score_url)
    return render_template('webtoons.html',views=views,stars=stars)

@app.route('/weather')
def weather():
    info = get_info()
    return render_template('weather.html',info=info)
if __name__=="__main__":
    app.run(debug=True)