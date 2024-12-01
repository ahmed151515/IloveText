from langdetect import detect
from src import app

from .forms import InputForm, TranslationForm, languages
from flask import render_template
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
    if form.validate_on_submit():
        text = form.text.data

        form.result.data = summarize(text)

    return render_template('summarize.html', form=form)


@app.route('/translate', methods=["GET", 'POST'])
def translation():
    """
    Route handler for the '/translate' endpoint.

    This function loads a tokenizer from the Hugging Face `transformers` library,
    specifically the M2M100Tokenizer, which is used for multilingual text translation.

    Steps:
    1. Creates an instance of `InputForm` to handle user input.
    2. Loads the M2M100 tokenizer with the pre-trained model "facebook/m2m100_418M".
    3. Calls the `get_response_from_model` function (assuming it's defined elsewhere) 
       with the loaded model and a dictionary of parameters to perform translation.
    4. The input text and language parameter (`forced_bos_token_id`) are passed to
       the model, targeting English ("en") as the output language.

    Notes:    - The print statement outputs the model's response to the console for debugging.
    """
    form = TranslationForm()
    if form.validate_on_submit():
        text = form.text.data
        language = form.language.data

        result = translate(text, languages.get(language))

        form.result.data = result

    return render_template('translation.html', form=form)

