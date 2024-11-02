from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
row = 10
col = 100


class SummarizeForm(FlaskForm):
    text = TextAreaField('Text', render_kw={"rows": row, "cols": col})
    submit = SubmitField('Summarize')


result = TextAreaField('Result', render_kw={
    'readonly': True, "rows": row, "cols": col})
result = TextAreaField('Result', render_kw={'readonly': True})


class InputForm(FlaskForm):
    """
    """
    input = StringField("input", validators=[DataRequired()])
    submit = SubmitField('translate')
    result = TextAreaField('output')


>>>>>> > 93565bf53209bd2fe0daaae064019d017b4b9969
