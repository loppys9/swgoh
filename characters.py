import json
import numpy
import cv2

class Buffs:
    #Buffs are a tuple of % chance and number of turns.

    def __init__(self, buffs):
        #print(buffs)
        self.advantage = (0, 0)
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
        self.tm_gain = (0, 0)

        for b in buffs:
            for key, value in b.items():
                self.__dict__[key] = (value[0], value[1])

class Abilities:

    def __init__(self):
        self.allies = False
        self.selfs = False
        self.leader = False

        self.accuracy = 0
        self.crit_chance = 0
        self.crit_dmg = 0
        self.protection = 0
        self.health = 0
        self.potency = 0

class Attack:

    def __init__(self, spec):
        self.name = spec['name']
        self.basic = spec['basic']
        self.targets_ally = spec['targets_ally']
        self.affect_allies = spec['affects_ally']
        self.aoe = spec['aoe']
        self.cooldown = spec['cooldown']
        self.target_buffs = Buffs(spec['target_buffs'])
        self.ally_buffs = Buffs(spec['ally_buffs'])
        self.self_buffs = Buffs(spec['self_buffs'])
        self.target_ally_buffs = Buffs(spec['target_ally_buffs'])


class Character:

    # Should probably have a serializer here but meh.
    def __init__(self, specs):
        self.name = specs['name']
        self.speed = specs['speed']
        self.factions = specs['factions']

        self.attacks = []
        for attack in specs['attacks']:
            self.attacks.append(Attack(attack))

        self.get_img(specs['img'])


    def get_img(self, img_file):
        self.img = cv2.imread('chars/' + img_file, 0)

    def gives_foresight():
        pass

    def gives_stealth():
        pass

    def removes_tm():
        pass

def read_from_config(config_file):
    with open(config_file) as json_file:
        data = json.load(json_file)

    characters = []
    for ch in data:
        #print(ch)
        characters.append(Character(ch))

    return characters
