from src import app

from .forms import InputForm, TranslationForm, languages
from flask import render_template
from .functions import get_response_from_model, translate

app.secret_key = "secret"


@app.route('/')
def home():
    routse = [i.endpoint for i in app.url_map.iter_rules()]
    del routse[0:2]
    return render_template('home.html', routes=routse)


@app.route('/summarize', methods=["GET", 'POST'])
def summarize():
    form = InputForm()
    if form.validate_on_submit():
        text = form.text.data
        model_id = "facebook/bart-large-cnn"
        response = get_response_from_model(
            model_id,
            {
                "inputs": text,
                "parameters": {
                    "max_length": 300, "min_length": 50, "do_sample": False,
                },
            })
        result = response[0].get("summary_text")

        form.result.data = result

    return render_template('summarize.html', form=form)


@app.route('/translate', methods=["GET", 'POST'])
def translation():
    """
    """
    form = TranslationForm()
    if form.validate_on_submit():
        text = form.text.data
        language = form.language.data
        result = translate(text, languages.get(language))
        form.result.data = result

    return render_template('translation.html', form=form)
