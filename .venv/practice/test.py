@app.route('/')
def index():
    myvalue = 'NeuralNine'
    myresult = 10 + 20
    mylist = [10, 20, 30, 40, 50]
    return render_template('index.html', myvalue=myvalue, myresult=myresult, mylist = mylist)

@app.route('/other')
def other():
    some_text = 'Hello World'
    return render_template('other.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('reverse_string')
def reverse_string(s):
    # this is how you reverse a string in python
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('aleternate_case')
def alternate_case(s):
    return''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])