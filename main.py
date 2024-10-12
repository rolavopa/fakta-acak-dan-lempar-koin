from flask import Flask
import random

app = Flask(__name__)
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]
koin_list = ["uang", "burung"]

@app.route("/")
def index():
    return f'<h1>Hai! di halaman ini, kamu dapat mempelajari beberapa fakta menarik tentang ketergantungan teknologi dan kamu dapat mamainkan lempar koin!(refresh untuk memperbarui fakta)</h1><a href="/fakta_acak">Lihat fakta acak</a>'

@app.route("/fakta_acak")
def facts():
    return f'<h2>{random.choice(facts_list)}</h2><a href="/lempar_koin">Lihat lempar koin!</a>'


@app.route("/lempar_koin")
def koin():
    return f'<p>{random.choice(koin_list)}</p>'

app.run(debug=True)
