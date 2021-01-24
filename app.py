from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/celsius', methods=['GET', 'POST'])

def fahrenheit_converter():
    c_temp = ''
    fahrenheit = ''
    if request.method == 'POST' and 'c_temp' in request.form:
        c_temp = int(request.form.get('c_temp'))
        fahrenheit = round(c_temp * (9/5) + 32)

    # elif request.method == 'POST' and ValueError:
    #     return '<h1>Please Enter Integer Value</h1>'
    # elif request.method == 'POST' and 'f_temp' in request.form:
    #     celsius_converter()

    return render_template('index.html', fahrenheit=fahrenheit)

@app.route('/fahrenheit', methods=['GET', 'POST'])

def celsius_converter():
    f_temp = ''
    celsius = ''
    if request.method == 'POST' and 'f_temp' in request.form:
        f_temp = int(request.form.get('f_temp'))
        celsius = round((f_temp - 32) * 5 / 9)

    return render_template('result.html', celsius=celsius)


if __name__ == "__main__":
    app.run(debug=True)

