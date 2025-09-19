from flask import Flask, send_file
from bs4 import BeautifulSoup

app = Flask(__name__)

INPUT_FILE = "input.html"
OUTPUT_FILE = "output.html"

@app.route("/")
def clean_article():
    # HTML-ის წაკითხვა
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # ყველა <article> ტეგის შიგთავსის დატოვება, <article> მოხსნით
    for article in soup.find_all("article"):
        article.replace_with(*article.contents)

    # შენახვა
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(str(soup))

    # HTML-ის დაბრუნება ბრაუზერში
    return send_file(OUTPUT_FILE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
