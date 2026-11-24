from flask import Flask, render_template, request

app = Flask(__name__)

DAFTAR_TEMA = ["ungu", "sunset", "mint", "langit"]


@app.route("/", methods=["GET", "POST"])
def index():
    nama = None
    jurusan = ""
    hobi_teks = ""
    hobi = []
    tema = "ungu"
    if request.method == "POST":
        nama = request.form.get("nama", "").strip() or None
        jurusan = request.form.get("jurusan", "").strip()
        hobi_teks = request.form.get("hobi", "").strip()
        hobi = [h.strip() for h in hobi_teks.split(",") if h.strip()][:5]
        tema = request.form.get("tema", "ungu")
        if tema not in DAFTAR_TEMA:
            tema = "ungu"
    return render_template(
        "index.html",
        nama=nama,
        jurusan=jurusan,
        hobi=hobi,
        hobi_teks=hobi_teks,
        tema=tema,
    )


@app.route("/about")
def about():
    return "Kartu Nama Flask: latihan method POST"


@app.route("/user/<name>")
def profile(name):
    return render_template(
        "index.html", nama=name, jurusan="", hobi=[], hobi_teks="", tema="ungu"
    )


@app.route("/umur/<int:n>")
def umur(n):
    return f"Umurmu {n} tahun"