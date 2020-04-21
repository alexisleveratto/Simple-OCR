from app import app
from app.forms import SubmitTaxNoticeForm
from flask import render_template, request, redirect, url_for
from .ocr_module import allowed_file, searh_paragraph, ocr_core
import os


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SubmitTaxNoticeForm()
    if form.validate_on_submit():
        file = form.file_path.data

        if not os.path.isdir(app.config["UPLOAD_FOLDER"]):
            os.mkdir(app.config["UPLOAD_FOLDER"])
        # if no file is selected
        if file.filename == "":
            return render_template("upload.html", msg="No file selected")

        if file and allowed_file(file.filename):
            # call the OCR function on it
            extracted_text = ocr_core(file)
            found_paragrahps = searh_paragraph(extracted_text, form.search_words.data)
            # extract the text and display it
            return render_template(
                "index.html", form=form, found_paragrahps=found_paragrahps
            )  # extracted_text=extracted_text, img_src=os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
    return render_template("index.html", form=form)
