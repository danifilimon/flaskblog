from flask import Flask, render_template, url_for
app = Flask(__name__)


my_posts = [
    {
        'author': 'Daniel Filimon',
        'title': 'Blog Post 1',
        'content': 'This is my first post!',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Jane Filimon',
        'title': 'Blog Post 2',
        'content': 'This is my first post!',
        'date_posted': 'April 28, 2019'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=my_posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
