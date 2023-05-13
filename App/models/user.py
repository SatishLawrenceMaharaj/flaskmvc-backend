from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    student_name = db.Column(db.String(120), nullable=False)
    student_dob = db.Column(db.String(120), nullable=False)
    student_class = db.Column(db.String(120), nullable=False)
    access = db.Column(db.String(120), nullable=False)
    
    def __init__(self, name, password, email, phone, student_name, student_dob, student_class, access):
        self.name = name
        self.set_password(password)
        self.email = email
        self.phone = phone
        self.student_name = student_name
        self.student_dob = student_dob
        self.student_class = student_class 
        self.access = access    
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'student_name': self.student_name,
            'student_dob': self.student_dob,
            'student_class': self.student_class,
            'access': self.access
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def get_access(self):
        return self.access