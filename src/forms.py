from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired


class SummarizeForm(FlaskForm):
    text = TextAreaField('Text')
    submit = SubmitField('Summarize')
    result = TextAreaField('Result', render_kw={'readonly': True})

class InputForm(FlaskForm):
    """
    """
    input = StringField("input", validators=[DataRequired()])
    submit = SubmitField('translate')
    result = TextAreaField('output')
