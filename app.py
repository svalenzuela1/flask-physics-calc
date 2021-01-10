from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def fahrenheit_converter():
    celsius = ''
    if request.method == 'POST':
        celsius = (int(request.form.get('celsius')) - 32) * 5/9

    return render_template('index.html', celsius=celsius)


if __name__ == '__main__':
    app.run()
