from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#password:admin
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///polio.db'
db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    skripsi=db.Column(db.String(250))
    nama=db.Column(db.String(40))
    nim=db.Column(db.String(15))
    prodi=db.Column(db.String(25))
    lama=db.Column(db.String(4))
    ipk=db.Column(db.String(5))
    status=db.Column(db.String(25))
    photo=db.Column(db.String(25))

def __init__(self,skripsi,nama,nim,prodi,lama,ipk, status, photo):
    self.skripsi=skripsi
    self.nama=nama 
    self.nim=nim
    self.prodi=prodi
    self.lama=lama
    self.ipk=ipk
    self.status=status
    self.photo=photo
@app.route('/')
def index():
    return render_template('muka.html')

@app.route('/<int:page_num>')
def student(page_num):
    student = Student.query.paginate(per_page=1, page=page_num, error_out=True)
    return render_template('index.html', student=student)




if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')