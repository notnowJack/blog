from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    blogs = [
        {"id":1, "title": "Wanderstop - A game that made me both stop and wander"},
        {"id":2, "title": "Clair Obscur: Expedition 33 - This game sure aged me 33 years"},
        {"id":3, "title": "Jusant - These french games sure be hitting me in the feels"},
    ]
    return render_template("home.html", blogs=blogs)

@app.route("/blog/<int:blog_id>")
def blog_posts(blog_id):
    blogs = {
        1: {"title": "Wanderstop - A game that made me both stop and wander", "text": "yappa yappa i'll put more text in eventually"},
        2: {"title": "Clair Obscur: Expedition 33 - This game sure aged me 33 years", "text": "making this text different from the last one boy oh boy i miss Gustave"},
        3: {"title": "Jusant - These french games sure be hitting me in the feels", "text": "damn not a single piece of dialogue and yet i could still right boatloads about this game"},
    }
    
    blog = blogs.get(blog_id)
    if blog is None:
        return render_template("index.html", blogs=blogs)
    return render_template("blog_page.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)