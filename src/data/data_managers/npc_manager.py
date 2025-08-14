from data.tables_and_relations import Location, SubLocation, NPC, Quest
from data.data_managers.base_manager import BaseManager

class NPCManager(BaseManager):
    def __init__(self, session):
        super().__init__(session)
        self.model = NPC
    
    def add_location(self, npc_id, location_id):
        npc = self.get_by_id(npc_id)
        location = self.session.query(Location).get(location_id)
        if npc and location:
            npc.locations.append(location)
            self.session.commit()
    
    def add_sub_location(self, npc_id, sub_location_id):
        npc = self.get_by_id(npc_id)
        sub_location = self.session.query(SubLocation).get(sub_location_id)
        if npc and sub_location:
            npc.sub_locations.append(sub_location)
            self.session.commit()
    
    def add_quest(self, npc_id, quest_id):
        npc = self.get_by_id(npc_id)
        quest = self.session.query(Quest).get(quest_id)
        if npc and quest:
            npc.quests.append(quest)
            self.session.commit()
    
    def get_related_locations(self, npc_id):
        npc = self.get_by_id(npc_id)
        return npc.locations if npc else []
    
    def get_related_sub_locations(self, npc_id):
        npc = self.get_by_id(npc_id)
        return npc.sub_locations if npc else []
    
    def get_related_quests(self, npc_id):
        npc = self.get_by_id(npc_id)
        return npc.quests if npc else []