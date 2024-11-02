from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
row = 10
col = 100


class SummarizeForm(FlaskForm):
    text = TextAreaField('Text', render_kw={"rows": row, "cols": col})
    submit = SubmitField('Summarize')
    result = TextAreaField('Result', render_kw={
                           'readonly': True, "rows": row, "cols": col})
