from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/project 1')
def project1():
    return render_template('project1.html',
                           PAGE_TITLE='Project One',
                           PAGE_DESCRIPTION='Every Court Has a Story',
                           PAGE_URL='https://yourwebsite.com/project1')

@app.route('/project 2')
def project2():
    return render_template('project2.html',
                           PAGE_TITLE='Project Two',
                           PAGE_DESCRIPTION='Description for Project Two',
                           PAGE_URL='https://yourwebsite.com/project2')

@app.route('/project 3')
def project3():
    return render_template('project3.html',
                           PAGE_TITLE='Project Three',
                           PAGE_DESCRIPTION='Description for Project Three',
                           PAGE_URL='https://yourwebsite.com/project3')

@app.route('/project 4')
def project4():
    return render_template('project4.html',
                           PAGE_TITLE='Project Four',
                           PAGE_DESCRIPTION='Description for Project Four',
                           PAGE_URL='https://yourwebsite.com/project4')



if __name__ == '__main__':
    app.run()
