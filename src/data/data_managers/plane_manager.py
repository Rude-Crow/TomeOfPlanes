# plane_manager.py
from data.tables_and_relations import Plane
from data.data_managers.base_manager import BaseManager

class PlaneManager(BaseManager):
    def __init__(self, session):
        super().__init__(session)
        self.model = Plane
    
    def get_locations(self, plane_id):
        plane = self.get_by_id(plane_id)
        return plane.locations if plane else []