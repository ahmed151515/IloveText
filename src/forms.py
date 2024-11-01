from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class SummarizeForm(FlaskForm):
    text = TextAreaField('Text')
    submit = SubmitField('Summarize')
    result = TextAreaField('Result', render_kw={'readonly': True})
