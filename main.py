import random
from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "<a href='/random_facts'>View a random fact!</a>"
@app.route("/random_facts")
def hello_world():
    facts_list = [
        'KFC is founded by Colonel Harland Sanders: Sanders started selling fried chicken at a roadside service station in Corbin, Kentucky, during the Great Depression.',
        "McDonald's is the world's largest restaurant chain by revenue, operating over 45,000 locations across more than 100 countries.",
        "Indonesia is the world's largest archipelagic state, located in Southeast Asia and Oceania between the Indian and Pacific oceans.",
        "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50 percent orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
        "The word martabak comes from the Arabic word mutabbaq, which translates to folded",
        "Welt Yang: He is over 80 years old in lore and carries over as a veteran character from Honkai Impact 3rd. Despite wearing glasses, his vision is completely healthy—he doesn't actually need them"
    ]
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/flip_coin")
def beda():
    coins = [
        'Heads',
        'Tails'
    ]
    return f'<p>{random.choice(coins)}</p>'
app.run(debug=True)
