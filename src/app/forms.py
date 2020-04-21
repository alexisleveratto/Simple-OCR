from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, SubmitField, StringField


class SubmitTaxNoticeForm(FlaskForm):
    file_path = FileField(
        "Tax Notice",
        validators=[FileRequired(), FileAllowed(["pdf", "png", "jpg"], "Tax Notice",),],
    )
    search_words = StringField("Search Words separated by a comma (,)")
    submit = SubmitField("Submit")
