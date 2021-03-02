from flask import Flask, redirect, url_for, request, render_template



app = Flask(__name__)

@app.route('/', defaults={'result': "Unavailable!"})
@app.route('/<result>')
def mainpage(result):
    return render_template("homepage.html", result = result)

@app.route('/submit',methods = ['GET'])
def submit():
   if request.method == 'GET':
        fn = request.args['first_name']
        ln= request.args['last_name']

        ans=fn +" "+ ln
        return redirect(url_for('mainpage',result = " {}!".format(ans)))
   else:
        return redirect(url_for('mainpage',result = "Something went wrong!"))


if __name__ == '__main__':
    app.run(debug=True)
