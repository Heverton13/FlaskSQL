from app import db

class Pessoa(db.Model):
    __tablename__="pessoa"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    cpf = db.Column(db.String(11), nullable=True)
    idade = db.Column(db.String(11), nullable=True)

    # Aqui eu poderia fazer o def __init__ mudaria somente a ordem que ficaria igual a do def __init__

    def __repr__ (self):
        return "<Pessoa: %r CPF: %r" % (self.name, self.cpf)