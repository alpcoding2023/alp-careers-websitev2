from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Siquijor',
  'salary': '50,000'
}, {
  'id': 2,
  'title': 'Frontend Engineer',
  'location': 'Manila',
  'salary': '$70,000'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'California',
  'salary': '$150,000'
}, {
  'id': 4,
  'title': 'Data Scientist',
  'location': 'San Francisco'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
