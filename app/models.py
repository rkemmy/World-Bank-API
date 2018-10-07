from . import db

class Catalog(db.Model):
    __tablename__ = 'catalog'
    id = db.Column(db.Integer, primary_key=True)
    metatype = db.Column(db.String, nullable=False)

    def __init__(self, id, metatype):
        self.id = id
        self. metatype = metatype

    def __repr__(self):
        return f'<Catalog {self.id}'
    

class Metatype(db.Model):
    __tablename__ = 'metatype'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String,  nullable=False)
    # catalog_id = db.Column(db.Integer, db.ForeignKey=("catalog_id"))

    def __init__(self,id,value):
        self.id = id
        self.value = value

    def __repr__(self):
        return f'Metatype {self.value}'
    
    