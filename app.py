from flask import Flask,render_template

app=Flask(__name__)
Jobs=[
  {
    'id':1,
    'title': 'Software Engineer',
    'location':'Banglore,India',
    'salary':'Rs. 10,00,000'
  },
   {
    'id':2,
    'title': 'Data Engineer',
    'location':'Gurgaon,India',
    'salary':'Rs. 9,00,000'
  } ,
{
    'id':3,
    'title': 'Backend Engineer',
    'location':'Texas,US',
    'salary':'$ 120,000'
  }, 
{
    'id':4,
    'title': 'Frontend Engineer',
    'location':'Remote job',
    'salary':'Rs. 6,00,000'
  }
]
@app.route("/")
def hello():
  return render_template('home.html',jobs=Jobs)


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
 