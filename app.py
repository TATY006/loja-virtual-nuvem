from flask import Flask, render_template_string

app = Flask(__name__)

# Carrega o conteúdo do HTML diretamente
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

@app.route("/")
def homepage():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
