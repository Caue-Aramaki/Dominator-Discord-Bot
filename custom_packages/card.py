class Skill:
  name = ''
  desc = ""
  cost = 0

  def __init__(self, skill_name="Unknown Skill", skill_desc = "No description for this skill.", skill_cost = 5):
    self.name = skill_name
    self.desc = skill_desc
    self.cost = skill_cost
# End

class Card:
  name = ''
  desc = ''
  health = 0
  defense = 0
  attack = 0
  skill = Skill()

  def __init__(self, card_name="Unknown Warrior", card_desc="No description for this warrior.",
               card_health=1000, card_defense=1000, card_attack=1000, 
               card_skill=Skill()
               ):
    
    self.name = card_name
    self.desc = card_desc
    self.health = card_health
    self.defense = card_defense
    self.attack = card_attack
    self.skill = card_skill
# End

class Master:
  name = ""
  id = ""
  cards = []

  def __init__(self, master_name="Unknown Master", master_id = "Unknown ID",
               card1=Card(card_name="Brave Pepega"), 
               card2=Card(card_name="Mindmaster Trump"),
               card3=Card(card_name="Enchanted Delphine"),
               ):
    self.name = master_name
    self.id = master_id
    self.cards = [card1, card2, card3]

# End  

master = Master()

master.cards[0].name