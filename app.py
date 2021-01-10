from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def fahrenheit_converter():
    c_temp = ''
    if request.method == 'POST' and 'c_temp' in request.form:
        c_temp = (int(request.form.get('c_temp')) - 32) * 5/9

    return render_template('index.html', c_temp=c_temp)


if __name__ == '__main__':
    app.run()
