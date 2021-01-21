from flask import Flask, request, render_template, session

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def fahrenheit_converter():
    # resp = Flask.Response("Foo bar baz")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    c_temp = ''
    celsius = ''
    if request.method == 'POST':
        c_temp = int(request.form.get('c_temp'))
        celsius = round((c_temp - 32) * 5/9)

    return render_template('index.html', celsius=celsius)

@app.route('/fahrenheit', methods=['GET', 'POST'])

def celsius_converter():
    f_temp = ''
    fahrenheit = ''
    if request.method == 'POST':
        f_temp = int(request.form.get('f_temp'))
        fahrenheit = round((f_temp - 32) * 5 / 9)

    #return render_template('index.html', fahrenheit=fahrenheit)
    return render_template('result.html', fahrenheit=fahrenheit)



app.run()
