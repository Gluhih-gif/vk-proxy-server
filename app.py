
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

ACCESS_TOKEN = "vk1.a.RwQAMDzAKOLOVWXNGaFusWEyDxGI_aUUVzavBjP3L0AlYLvM8jyV0cVAzQyB0zOym8iiCywQXAhMUGQlUM5QnRLjZT5EYreEv-Z4IFYn12b9mAI1aJDsWWuUv_rHuf3yyPzam2i7i193de8OVnCfUeTuPuN7NHWlbBANwK2qV9ohqUY3fBJI__VZo8e7batb2CWcg9ECNqrH_W_YX2vPsw"
GROUP_ID = "136706358"

@app.route("/get_posts")
def get_posts():
    vk_url = "https://api.vk.com/method/wall.get"
    params = {
        "owner_id": f"-{GROUP_ID}",
        "filter": "suggests",
        "count": 100,
        "access_token": ACCESS_TOKEN,
        "v": "5.131"
    }
    try:
        res = requests.get(vk_url, params=params)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
