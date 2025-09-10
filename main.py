from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/fertilizer/")
def fertilizer():
    return render_template("fertilizer.html")

@app.route("/cropre/", methods=["POST"])
def cropre():
    N = float(request.form["n"])
    P = float(request.form["p"])
    K = float(request.form["k"])
    T = float(request.form["t"])
    H = float(request.form["h"])
    PH = float(request.form["ph"])
    R = float(request.form["r"])

    model = pickle.load(open("crop.pkl", "rb"))
    data = [[N, P, K, T, H, PH, R]]
    pred = model.predict(data)
    pred1 = str(pred[0])
    msg = f"You should grow {pred1.upper()} in your farm."
    return render_template("Crop prediction.html", ms=msg)

@app.route("/ferpre/", methods=["POST"])
def ferpre():
    N = float(request.form["n"])
    P = float(request.form["p"])
    K = float(request.form["k"])
    T = float(request.form["t"])
    H = float(request.form["h"])
    M = float(request.form["m"])

    model = pickle.load(open("fert.pkl", "rb"))
    data = [[T, H, M, 4, N, P, K]]
    pred = model.predict(data)
    pred1 = pred[0]

    templates = {
        "Urea": "urea.html",
        "17-17-17": "17-17-17.html",
        "20-20": "20-20.html",
        "DAP": "DAP.html",
        "14-35-14": "14-35-14.html",
        "10-26-26": "10-26-26.html",
        "28-28": "28-28.html",
    }
    return render_template(templates.get(pred1, "fertilizer.html"), m=pred1)

@app.route("/crop/")
def crop():
    return render_template("Crop prediction.html")

@app.route("/agrihub/")
def agrihub():
    return render_template("agrihub.html")

@app.route("/insights/")
def agriinsights():
    return render_template("insights.html")

@app.route("/blogs/")
def blogs():
    sample_blogs = [
        "Welcome to AgriHub!",
        "Fertilizer tips for better yield",
        "How to choose the right crop"
    ]
    return render_template("Blogs.html", info=sample_blogs)

@app.route("/insightsadmin/")
def insightsadmin():
    return render_template("insightsadmin.html")

@app.route("/dynamiccard/")
def dynamiccard():
    return render_template("adminpage.html")

@app.route("/formsignin/", methods=["POST", "GET"])
def signin():
    database = {"bhandarkarathang@gmail.com": "athang123@"}
    email = request.form.get("Email")
    pwd = request.form.get("Password")
    if email in database and database[email] == pwd:
        return render_template("dynamiccard.html")
    return render_template("insightsadmin.html")

@app.route("/adminpage/")
def adminpage():
    return render_template("adminpage.html")

@app.route("/agrinews/")
def agrinews():
    try:
        r = requests.get(
            "https://serpapi.com/search.json?q=IndiaAgriculture&location=india&tbm=nws&api_key=b12217562727563e8f023a862765dac7a70f93ee5d16b65cfe45654851c93dcb"
        )
        data = r.json()
        data1 = data.get("news_results", [])
        return render_template("news.html", news=data1)
    except Exception as e:
        print("Error fetching news:", e)
        return render_template("news.html", news=[])

if __name__ == "__main__":
    app.run(debug=True)
