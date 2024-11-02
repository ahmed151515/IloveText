from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField, SubmitField, StringField


row = 10
col = 100


class SummarizeForm(FlaskForm):
    text = TextAreaField('Text', render_kw={"rows": row, "cols": col}, validators=[
                         DataRequired()])
    submit = SubmitField('Summarize')
    result = TextAreaField('Result', render_kw={
                           'readonly': True, "rows": row, "cols": col})


class InputForm(FlaskForm):
    """
    """
    input = StringField("input", validators=[DataRequired()])
    submit = SubmitField('translate')
    result = TextAreaField('output')
