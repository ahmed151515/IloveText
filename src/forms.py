from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import TextAreaField, SubmitField, SelectField


row = 10
col = 100
languages = {
    "Afrikaans": "af", "Amharic": "am", "Arabic": "ar", "Asturian": "ast", "Azerbaijani": "az",
    "Bashkir": "ba", "Belarusian": "be", "Bulgarian": "bg", "Bengali": "bn", "Breton": "br",
    "Bosnian": "bs", "Catalan; Valencian": "ca", "Cebuano": "ceb", "Czech": "cs", "Welsh": "cy",
    "Danish": "da", "German": "de", "Greek": "el", "English": "en", "Spanish": "es", "Estonian": "et",
    "Persian": "fa", "Fulah": "ff", "Finnish": "fi", "French": "fr", "Western Frisian": "fy",
    "Irish": "ga", "Gaelic; Scottish Gaelic": "gd", "Galician": "gl", "Gujarati": "gu",
    "Hausa": "ha", "Hebrew": "he", "Hindi": "hi", "Croatian": "hr", "Haitian; Haitian Creole": "ht",
    "Hungarian": "hu", "Armenian": "hy", "Indonesian": "id", "Igbo": "ig", "Iloko": "ilo",
    "Icelandic": "is", "Italian": "it", "Japanese": "ja", "Javanese": "jv", "Georgian": "ka",
    "Kazakh": "kk", "Central Khmer": "km", "Kannada": "kn", "Korean": "ko",
    "Luxembourgish; Letzeburgesch": "lb", "Ganda": "lg", "Lingala": "ln", "Lao": "lo",
    "Lithuanian": "lt", "Latvian": "lv", "Malagasy": "mg", "Macedonian": "mk", "Malayalam": "ml",
    "Mongolian": "mn", "Marathi": "mr", "Malay": "ms", "Burmese": "my", "Nepali": "ne",
    "Dutch; Flemish": "nl", "Norwegian": "no", "Northern Sotho": "ns", "Occitan (post 1500)": "oc",
    "Oriya": "or", "Panjabi; Punjabi": "pa", "Polish": "pl", "Pushto; Pashto": "ps",
    "Portuguese": "pt", "Romanian; Moldavian; Moldovan": "ro", "Russian": "ru", "Sindhi": "sd",
    "Sinhala; Sinhalese": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Albanian": "sq",
    "Serbian": "sr", "Swati": "ss", "Sundanese": "su", "Swedish": "sv", "Swahili": "sw",
    "Tamil": "ta", "Thai": "th", "Tagalog": "tl", "Tswana": "tn", "Turkish": "tr",
    "Ukrainian": "uk", "Urdu": "ur", "Uzbek": "uz", "Vietnamese": "vi", "Wolof": "wo",
    "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Chinese": "zh", "Zulu": "zu"
}
languages = dict(sorted(languages.items()))

class InputForm(FlaskForm):
    text = TextAreaField('Text', render_kw={"rows": row, "cols": col}, validators=[
                         DataRequired(),
                         #  Length(max=300)
                         ])
    submit = SubmitField('Summarize')
    result = TextAreaField('Result', render_kw={
                           'readonly': True, "rows": row, "cols": col})


class TranslationForm(InputForm):

    language = SelectField('Language', choices=languages.keys())
    submit = SubmitField('Translate')
