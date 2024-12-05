from langdetect import detect
from src import app

from .forms import InputForm, TranslationForm, languages
from flask import render_template, url_for
from .functions import translate, summarize

app.secret_key = "secret"





@app.route('/')
def home():
    routse = [i.endpoint for i in app.url_map.iter_rules()]
    del routse[0:2]
    return render_template('home.html', routes=routse, enumerate=enumerate, ls=range(10), condtion=lambda i: i % 3 == 0)


@app.route('/summarize', methods=["GET", 'POST'])
def summarizetion():
    form = InputForm()
    show_error = False
    if form.validate_on_submit():
        text = form.text.data

        success, result = summarize(text)
        if not success:
            show_error = True
        else:
            form.result.data = result

    return render_template('summarize.html', form=form, show_error=show_error)


@app.route('/translate', methods=["GET", 'POST'])
def translation():
    """
    Route handler for the '/translate' endpoint.
    Handles translation requests and shows error tooltip if translation fails.
    """
    form = TranslationForm()
    show_error = False
    if form.validate_on_submit():
        text = form.text.data
        language = form.language.data

        success, result = translate(text, languages.get(language))
        if not success:
            show_error = True
        else:
            form.result.data = result

    return render_template('translation.html', form=form, show_error=show_error)
