from data.tables_and_relations import Location, SubLocation, NPC, Quest
from data.data_managers.base_manager import BaseManager

class QuestManager(BaseManager):
    def __init__(self, session):
        super().__init__(session)
        self.model = Quest
    
    def add_location(self, quest_id, location_id):
        quest = self.get_by_id(quest_id)
        location = self.session.query(Location).get(location_id)
        if quest and location:
            quest.locations.append(location)
            self.session.commit()
    
    def add_sub_location(self, quest_id, sub_location_id):
        quest = self.get_by_id(quest_id)
        sub_location = self.session.query(SubLocation).get(sub_location_id)
        if quest and sub_location:
            quest.sub_locations.append(sub_location)
            self.session.commit()
    
    def add_npc(self, quest_id, npc_id):
        quest = self.get_by_id(quest_id)
        npc = self.session.query(NPC).get(npc_id)
        if quest and npc:
            quest.npcs.append(npc)
            self.session.commit()
    
    def get_related_locations(self, quest_id):
        quest = self.get_by_id(quest_id)
        return quest.locations if quest else []
    
    def get_related_sub_locations(self, quest_id):
        quest = self.get_by_id(quest_id)
        return quest.sub_locations if quest else []
    
    def get_related_npcs(self, quest_id):
        quest = self.get_by_id(quest_id)
        return quest.npcs if quest else []