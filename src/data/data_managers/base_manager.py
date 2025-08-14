#base_manager.py
class BaseManager:
    def __init__(self, session):
        self.session = session
    
    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        return obj
    
    def update(self, obj_id, **kwargs):
        obj = self.get_by_id(obj_id)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.session.commit()
        return obj
    
    def delete(self, obj_id):
        obj = self.get_by_id(obj_id)
        self.session.delete(obj)
        self.session.commit()
    
    def get_by_id(self, obj_id):
        return self.session.query(self.model).get(obj_id)
    
    def get_all(self):
        return self.session.query(self.model).all()
    
    def get_by_name(self, name):
        return self.session.query(self.model).filter_by(name=name).first()
    
    def get_by_filter(self, **filters):
        return self.session.query(self.model).filter_by(**filters).all()