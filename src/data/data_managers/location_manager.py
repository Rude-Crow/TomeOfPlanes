from data.tables_and_relations import Location, NPC, Quest
from data.data_managers.base_manager import BaseManager

class LocationManager(BaseManager):
    def __init__(self, session):
        super().__init__(session)
        self.model = Location
    
    def get_sub_locations(self, location_id):
        location = self.get_by_id(location_id)
        return location.sub_locations if location else []
    
    def get_plane(self, location_id):
        location = self.get_by_id(location_id)
        return location.plane if location else None
    
    def add_npc(self, location_id, npc_id):
        location = self.get_by_id(location_id)
        npc = self.session.query(NPC).get(npc_id)
        if location and npc:
            location.npcs.append(npc)
            self.session.commit()
    
    def add_quest(self, location_id, quest_id):
        location = self.get_by_id(location_id)
        quest = self.session.query(Quest).get(quest_id)
        if location and quest:
            location.quests.append(quest)
            self.session.commit()