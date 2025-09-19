from bs4 import BeautifulSoup

input_file = "input.html"
output_file = "output.html"

# HTML ფაილის წაკითხვა
with open(input_file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# ყველა <article> ტეგის შიგთავსის დატოვება, <article> მოხსნით
for article in soup.find_all("article"):
    article.replace_with(*article.contents)

# შეცვლილი HTML-ის შენახვა
with open(output_file, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"<article> tag removed. Clean HTML saved to '{output_file}'")
