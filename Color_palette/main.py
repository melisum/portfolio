from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from Pylette import extract_colors
from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename

# # Save palette's color values to CSV
# palette.to_csv(filename='color_palette.csv', frequency=True)
# # Pick random colors
# random_color = palette.random_color(N=1, mode='uniform')
# random_colors = palette.random_color(N=100, mode='frequency')
# # Access colors by index
#     most_common_color = palette[0]
#     print(palette[0].rgb)
def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
#
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Maeoigfneirog'
Bootstrap5(app)

class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField()

@app.route("/", methods=['GET', 'POST'])
def home():
    palette = extract_colors(image='static/queen.png', palette_size=10)
    hex_codes = []
    rgbs=[]
    for counter in range(1, 10):
        color = palette[counter]
        hex_code = rgb2hex(color.rgb[0], color.rgb[1], color.rgb[2])
        hex_codes += [hex_code]
        rgbs += [color.rgb]
    print(hex_codes)
    form = UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('static/' + filename)
        palette = extract_colors(image=f'static/{filename}', palette_size=10)
        hex_codes = []
        rgbs = []
        for counter in range(1, 10):
            color = palette[counter]
            hex_code = rgb2hex(color.rgb[0], color.rgb[1], color.rgb[2])
            hex_codes += [hex_code]
            rgbs += [color.rgb]
        print(hex_codes, filename)
        return render_template("palette.html", codes=hex_codes, form=form, rgbs=rgbs, picture=filename)

    return render_template("palette.html", codes=hex_codes, form=form, rgbs=rgbs, picture="queen.png")



if __name__ == '__main__':
    app.run(debug=True, port=5002)
