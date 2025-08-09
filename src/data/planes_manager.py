from data.tables_and_relations import SessionLocal, Plane

class PlanesManager:
    def __init__(self):
        pass

    def get_all_planes(self):
        session = SessionLocal()
        try:
            return session.query(Plane).order_by(Plane.name).all()
        finally:
            session.close()

    def add_plane(self, name, description):
        session = SessionLocal()
        try:
            plane = Plane(name=name.strip(), description=description.strip())
            session.add(plane)
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

