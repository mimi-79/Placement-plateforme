from flask import Flask, redirect
from flask import render_template

from forms import ProjetForm

app = Flask(__name__)

from config import Config
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    projets = {'titre': 'Placement de plateforme'}
    return render_template('index.html', title='Accueil', mod=projets)

from flask import flash

@app.route('/form_projet_input', methods=['GET', 'POST'])
def form_projet_input():
    projet_form = ProjetForm()
    if projet_form.validate_on_submit():

        flash('ID projet:{}, titre:{}'.format(projet_form.id_projet.data,
                                              projet_form.titre.data))
        return redirect('/index')
    return render_template('form_projet_input.html',
                           title='Edition projet', form=projet_form)
@app.route('/contact')
def contact():
    # On passe le titre pour que l'onglet du navigateur s'actualise
    return render_template('contact.html', title='Nous contacter')


if __name__ == "__main__":
    app.run(debug=True)