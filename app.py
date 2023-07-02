from flask import Flask, render_template, request, jsonify
from database import load_jobs_from_db, load_job_from_db, add_applcn_to_db

app = Flask(__name__)


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "NOT FOUND", 404
  return render_template('jobpage.html', JOB=job)


@app.route("/job/<id>/apply", methods=['post'])
def applying_for_job(id):
  Data = request.form
  add_applcn_to_db(id,Data)
  return render_template('submitted.html',data=Data)

  #return jsonify(data)
  


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
