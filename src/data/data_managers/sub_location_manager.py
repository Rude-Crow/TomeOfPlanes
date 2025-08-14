from data.tables_and_relations import SubLocation, NPC, Quest
from data.data_managers.base_manager import BaseManager

class SubLocationManager(BaseManager):
    def __init__(self, session):
        super().__init__(session)
        self.model = SubLocation
    
    def get_location(self, sub_location_id):
        sub_location = self.get_by_id(sub_location_id)
        return sub_location.location if sub_location else None
    
    def add_npc(self, sub_location_id, npc_id):
        sub_location = self.get_by_id(sub_location_id)
        npc = self.session.query(NPC).get(npc_id)
        if sub_location and npc:
            sub_location.npcs.append(npc)
            self.session.commit()
    
    def add_quest(self, sub_location_id, quest_id):
        sub_location = self.get_by_id(sub_location_id)
        quest = self.session.query(Quest).get(quest_id)
        if sub_location and quest:
            sub_location.quests.append(quest)
            self.session.commit()