import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

FOODS = [
    {"name": "김치찌개", "image": "https://static.wtable.co.kr/image-resize/production/service/recipe/291/4x3/a2421dff-e56c-40bd-8b40-06a91fc000a9.jpg", "comment": "돼지고기 추가는 필수인거 알제?" },
     {"name": "된장찌개", "image":"https://cookpick.kr/wp-content/uploads/2025/10/chadol-doenjang-jjigae-recipe1.webp", "comment": "차돌 넣으면 개 야르~"},
     {"name": "라면 & 김밥", "image":"https://mblogthumb-phinf.pstatic.net/MjAyMzA0MDlfMjI5/MDAxNjgxMDM5MTIyOTMz._VoBUZXonMFCgH4c1RppNZqN4wmKx7KUiwrgup_iSk8g.4ndChMDoN9iB3hA5IXgWsVsnUuAikPl8bwaZG8SkG4kg.JPEG.joyand2/IMG_9470.jpg?type=w800", "comment": "여기에 김치까지 곁들이면..... 말이 필요하나?"},
     {"name" : "햄버거", "image":"https://i.namu.wiki/i/1EDvyVH0IZjtAA_d3N0fOgcQ0W-41UIPYYplbmBWG5bMEvC96171vKeMCLYa328tN5O9hqIb8JFqsRVetDHntw.webp", "comment": "월요일 좋아~ 최고로 좋아~"}
      ]

@app.route("/")
def start():
    return render_template("start.html")

# 기존: food = random.choice(FOODS) 후 전달
# 수정: 비어있는 상태로 페이지 열기
@app.route("/draw_page")
def draw_page():
    return render_template("index.html", food=None)

@app.route("/draw")
def draw():
    current = request.args.get("current")
    
    choices = [food for food in FOODS if food["name"] != current]
    if not choices:  # 혹시 예외 케이스 처리
        choices = FOODS

    food = random.choice(choices)

    return jsonify(food)  # HTML 대신 JSON 반환

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)