class Buffs:
    #Buffs are a tuple of % chance and number of turns.
    self.call_to_action = (0, 0)
    self.daze = (0, 0)
    self.deathmark = (0, 0)
    self.foresight = (0, 0)
    self.fracture = (0, 0)
    self.isolate = (0, 0)
    self.speed_down = (0, 0)
    self.speed_up = (0, 0)
    self.stealth = (0, 0)
    self.stun = (0, 0)
    self.tenacity = (0, 0)
    self.tm_reduce = (0, 0)

class Attack:
    self.targets_ally = False
    self.affect_allies = False

    def __init__(self, basic, cooldown=0):
        self.basic = basic
        self.target_buffs = Buffs()
        self.ally_buffs = Buffs()
        self.target_ally_buffs = Buffs()
        self.cooldown = 0


class Character:
    self.attacks = []
    self.abilities = []

    def __init__(self, speed):
        self.speed = speed

    def gives_foresight():
        pass

    def gives_stealth():
        pass

    def removes_tm():
        pass

r2d2 = Character(220)
