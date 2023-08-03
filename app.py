from flask import Flask, render_template
from iphone_scraper import Sit
from samsung import Site
from informatica import Info
from tv import Tvs
from eletroportateis import Eletro
from smartwatch import Smart
from audio import Audio
from game import Game



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/iphones')
def iphones():
    site_iphone = Sit('iphone')
    dict_iphone = site_iphone.celular()
    return render_template('iphones.html', data=dict_iphone)

@app.route('/samsung')
def samsung():
    site_iphone = Site('samsung')
    dict_iphone = site_iphone.celular()
    return render_template('samsung.html', data=dict_iphone)

@app.route('/informatica')
def informatica():
    site_iphone = Info('informatica')
    dict_iphone = site_iphone.informatica()
    return render_template('informatica.html', data=dict_iphone)

@app.route('/tv')
def tv():
    site_iphone = Tvs('tv')
    dict_iphone = site_iphone.tv()
    return render_template('tv.html', data=dict_iphone)

@app.route('/eletroportateis')
def eletroportateis():
    site_iphone = Eletro('eletricos')
    dict_iphone = site_iphone.eletroportateis()
    return render_template('eletroportateis.html', data=dict_iphone)

@app.route('/smartwatch')
def smartwatch():
    site_iphone = Smart('smartwatch')
    dict_iphone = site_iphone.smartwatch()
    return render_template('smartwatch.html', data=dict_iphone)

@app.route('/audio')
def audio():
    site_iphone = Audio('audio')
    dict_iphone = site_iphone.audio()
    return render_template('audio.html', data=dict_iphone)

@app.route('/games')
def games():
    site_iphone = Game('game')
    dict_iphone = site_iphone.game()
    return render_template('games.html', data=dict_iphone)


if __name__ == '__main__':
    app.run(debug=True)
