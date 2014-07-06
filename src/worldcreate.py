#!/usr/bin/python

import textwrap, sys
from random import randint

portchar = {2: "A", 3: "A", 4: "A", 5: "B", 6: "B", 7: "C", 8: "C", 9: "D", 10: "E", 11: "E", 12: "X"}

portdesc = {"A": "Excellent quality installation.  Refined fuel available.  Annual maintenance overhaul available.  Shipyard capable of both starship and non-starship construction present.",
            "B": "Good quality installation.  Refined fuel available.  Annual maintenance overhaul available.  Shipyard capable of non-starship construction present.",
            "C": "Routine quality installation. Only unrefined fuel available. Reasonable repair facilities are present.",
            "D": "Poor quality installation.  Only unrefined fuel available.  No repair or shipyard facilities present.",
            "E": "Frontier installation. Essentially a bare spot of bedrock with no fuel, facilities, or bases present.",
            "X": "No provision is made for any starship landings."
            }

atmodesc = {0: "No atmosphere.  Protective vacc suits required at all times.",
            1: "Trace atmosphere.  Protective vacc suits required at all times.",
            2: "Very thin, tainted atmosphere.  Respirators/compressors with filter masks required for adequate oxygen supply.",
            3: "Very thin atmosphere.  Respirators/compressors required for adequate oxygen supply.",
            4: "Thin, tainted atmosphere.  Filter mask required.",
            5: "Thin atmosphere.  Breathable without assistance.",
            6: "Standard atmosphere.  Breathable without assistance.",
            7: "Standard, tainted atmosphere.  Filter mask required.",
            8: "Dense atmosphere.  Breathable without assistance.",
            9: "Dense, tainted atmosphere.  Filter mask required.",
            10: "Exotic atmosphere.  Oxygen tanks required.",
            11: "Corrosive atmosphere.  Protective vacc suits required at all times.",
            12: "Insidious atmosphere.  Will defeat any personal protective measures in 2-12 hours."
            }

govdesc = {0: "No government structure.  In many cases, family bonds will predominate.",
           1: "Company/Corporation: Ruling functions are assumed by a company managerial elite, and most citizenry are company employees or dependents.",
           2: "Participating Democracy: Ruling function decisions are reached by the advice and consent of the citizenry directly.",
           3: "Self-Perpetuating Oligarchy: Ruling functions are performed by a restricted minority, with little or no input from the mass of the citizenry.",
           4: "Representative Democracy: Ruling functions are performed by elected representatives.",
           5: "Feudal Technocracy: Ruling functions are performed by specific individuals for persons who agree to be ruled by them.  Relationships are based on the performance of technical activities which are mutually beneficial.",
           6: "Captive Government: Ruling functions are performed by an imposed leadership answerable to an outside group.  A colony or conquered area.",
           7: "Balkanization: No central ruling authority exists; rival governments compete for control.  Law level refers to government nearest the starport.",
           8: "Civil Service Bureaucracy: Ruling functions are performed by government agencies employing individuals selected for their expertise.",
           9: "Impersonal Bureaucracy: Ruling functions are performed by agencies which have become insulated from the governed citizens.",
           10: "Charismatic Dictator: Ruling functions are performed by agencies directed by a single leader who enjoys the overwhelming confidence of the citizens.",
           11: "Non-Charismatic Leader: A previous charismatic dictator has been replaced by a leader through normal channels.",
           12: "Charismatic Oligarchy: Ruling functions are performed by a select group of members of an organization or class which enjoys the overwhelming confidence of the citizenry.",
           13: "Religious Dictatorship: Ruling functions are performed by a religious organization without regard to the specific individual needs of the citizenry."
           }

lawdesc = ["0: No laws affecting weapons possession or weapons ownership.",
           "1: Certain weapons are prohibited, including specifically 1) body pistols which are undetectable by standard detectors, 2) explosive weapons such as bombs or grenades, and 3) poison gas.",
           "2: Portable energy weapons, such as laser rifles or carbines are prohibited.  Ship's gunnery is not affected.",
           "3: Weapons of a strict military nature (such as machine guns or automatic rifles, though not submachine guns) are prohibited.",
           "4: Light assault weapons (such as submachine guns) are prohibited",
           "5: Personal concealable firearms (such as pistols and revolvers) are prohibited",
           "6: Most firearms (all except shotguns) are prohibited.  The carrying of any type of weapon openly is discouraged.",
           "7: Shotguns are prohibited.",
           "8: Long bladed weapons (all blade weapons except daggers) are strictly controlled.  Open possession in public is prohibited.  Ownership is, however, not restricted.",
           "9: Possession of any weapon outside of one's home is prohibited."
           ]

technames = ["Personal Weapons:\t",
             "Personal Armor:\t\t",
             "Special Weapons:\t",
             "Computers:\t\t",
             "Communications:\t\t",
             "Water Transportation:\t",
             "Land Transportation:\t",
             "Air Transportation:\t",
             "Space Transportation:\t",
             "Energy Generation:\t"
             ]

techdesc = {0: ['Club, Cudgel, Spear', 'No Armor', 'No Special', 'No Computers', 'Runners', 'Canoes', 'Carts', 'No Air Transportation', 'No Space Transportation', 'Muscle'],
            1: ['Dagger, Pike, Sword', 'Jack', 'Catapult', 'Abacus', 'Heliograph', 'Galley', 'Wagons', 'No Air Transportation', 'No Space Transportation', 'Muscle'],
            2: ['Halberd, Broadsword', 'Jack', 'Cannon', 'Abacus', 'Heliograph', 'Galley', 'Wagons', 'No Air Transportation', 'No Space Transportation', 'Wind'],
            3: ['Foil, Cutlass, Blade, Bayonet', 'Jack', 'Cannon', 'Abacus', 'Postal System', 'Sailing Ships', 'Wagons', 'Hot Air Balloons', 'No Space Transportation', 'Water Wheel'],
            4: ['Revolver, Shotgun', 'Cloth', 'Artillery', 'Adding Machine', 'Telephones', 'Steamships', 'Trains', 'Dirigibles', 'No Space Transportation', 'Coal'],
            5: ['Carbine, Rifle, SMG, Pistol', 'Cloth', 'Sandcasters, Mortars', 'Model/1', 'Radio', 'Steamships', 'Ground Cars', 'Fixed Wing Aircraft', 'No Space Transportation', 'Oil'],
            6: ['Auto Rifle', 'Cloth', 'Missiles, Rocket Launchers', 'Model/1 bis', 'Television', 'Submersibles', 'ATV, AFV', 'Rotary Wing Aircraft', 'No Space Transportation', 'Fission'],
            7: ['Body Pistol', 'Mesh', 'Pulse Laser', 'Model/2', 'Internet', 'Hovercraft', 'Hovercraft', 'Rotary Wing Aircraft', 'Non-Starships', 'Solar'],
            8: ['Laser Carbine', 'Mesh', 'Auto-Cannon', 'Model/2 bis', 'Internet', 'Hovercraft', 'Hovercraft', 'Air/Raft', 'Non-Starships', 'Fusion'],
            9: ['Laser Rifle', 'Ablat', 'Beam Laser', 'Model/3', 'Internet', 'Hovercraft', 'Hovercraft', 'Air/Raft', 'Starships', 'Fusion'],
            10: ['Laser Rifle', 'Reflec', 'Beam Laser', 'Model/4', 'Internet', 'Hovercraft', 'Hovercraft', 'Air/Raft', 'Drives H or less', 'Fusion'],
            11: ['Laser Rifle', 'Reflec', 'Beam Laser', 'Model/5', 'Internet', 'Hovercraft', 'Hovercraft', 'Air/Raft', 'Drives K or less', 'Fusion'],
            12: ['Laser Rifle', 'Reflec', 'Beam Laser', 'Model/6', 'Internet', 'Hovercraft', 'Hovercraft', 'Grav Belts', 'Drives N or less', 'Fusion'],
            13: ['Laser Rifle', 'Battle Dress', 'Beam Laser', 'Model/7', 'Internet', 'Hovercraft', 'Hovercraft', 'Grav Belts', 'Drives Q or less', 'Fusion'],
            14: ['Laser Rifle', 'Battle Dress', 'Beam Laser', 'Model/7', 'Internet', 'Hovercraft', 'Hovercraft', 'Grav Belts', 'Drives U or less', 'Fusion'],
            15: ['Laser Rifle', 'Battle Dress', 'Beam Laser', 'Model/7', 'Internet', 'Hovercraft', 'Hovercraft', 'Grav Belts', 'All Drives', 'Fusion'],
            16: ['Laser Rifle', 'Battle Dress', 'Beam Laser', 'Model/7', 'Internet', 'Matter Transport', 'Matter Transport', 'Matter Transport', 'All Drives', 'Fusion'],
            17: ['Laser Rifle', 'Battle Dress', 'Beam Laser', 'Artificial Intelligence', 'Internet', 'Matter Transport', 'Matter Transport', 'Matter Transport', 'All Drives', 'Antimatter'],
            18: ['Laser Rifle', 'Battle Dress', 'Beam Laser', 'Artificial Intelligence', 'Internet', 'Matter Transport', 'Matter Transport', 'Matter Transport', 'All Drives', 'Antimatter'],
            }

class World(object):
    def __init__(self, name):
        self.name = name
        self.starport = ""
        self.size = 0
        self.atmosphere = 0
        self.hydro = 0
        self.hydrodm = 0
        self.population = 0
        self.government = 0
        self.law = 0
        self.techindexdm = 0
        self.techindex = 0
        
    def create_world(self):
        self.starport = portchar[randint(2, 12)]
        if self.starport == "A":
            self.navalbasethreshold = 8
            self.scoutbasethreshold = 10
        if self.starport == "B":
            self.navalbasethreshold = 8
            self.scoutbasethreshold = 9
        if self.starport == "C":
            self.scoutbasethreshold = 8
            self.navalbasethreshold = 13
        if self.starport == "D":
            self.scoutbasethreshold = 7
            self.navalbasethreshold = 13
        if self.starport == "E":
            self.navalbasethreshold = 13
            self.scoutbasethreshold = 13
        self.size = randint(2, 12) - 2
        if self.size == 0:
            self.atmosphere = 0
        else:
            self.atmosphere = randint(2, 12) - 7 + self.size
        if self.atmosphere < 0: self.atmosphere = 0
        if self.atmosphere > 12: self.atmosphere = 12
        if ((self.atmosphere < 2) or (self.atmosphere > 9)):
            self.hydrodm = -4
        if self.size < 2:
            self.hydro = 0
        else:
            self.hydro = randint(2, 12) - 7 + self.size + self.hydrodm
        if self.hydro < 0: self.hydro = 0
        if self.hydro > 10: self.hydro = 10
        self.population = randint(2, 12) - 2
        self.government = randint(2, 12) - 7 + self.population
        if self.government < 0: self.government = 0
        if self.government > 13: self.government = 13
        self.law = randint(2, 12) - 7 + self.government
        if self.law < 0: self.law = 0
        if self.law > 9: self.law = 9
        self.techindexdm = self.create_tech_index(self.starport, self.size, self.atmosphere, self.hydro, self.population, self.government)
        self.techindex = randint(1, 6) + self.techindexdm
        if self.techindex < 0: self.techindex = 0
        if self.techindex > 18: self.techindex = 18
    
    def create_tech_index(self, techport, techsize, techatmo, techhydro, techpop, techgov):
        modifier = 0
        techportdm = {"A": 6, "B": 4, "C": 2, "X": -4}
        if techport in techportdm.keys():
            modifier += techportdm[techport]
        if techsize in [0, 1]: modifier += 2
        if techsize in [2, 3, 4]: modifier += 1
        if techatmo in [0, 1, 2, 3, 10, 11, 12]: modifier += 1
        if techhydro == 9: modifier += 1
        if techhydro == 10: modifier += 2
        if techpop in [1, 2, 3, 4, 5]: modifier += 1
        if techpop == 9: modifier += 2
        if techpop == 10: modifier += 4
        if techgov in [0, 5]: modifier += 1
        if techgov == 13: modifier -= 2
        return modifier
        
    def print_world(self):
        print self.name
        print
        if self.starport == "X": print "No Starport"
        else: 
            print self.starport, "Class Starport"
            baseroll = randint(2, 12)
            if baseroll >= self.navalbasethreshold: print "+ Naval Base"
            if baseroll >= self.scoutbasethreshold: print "+ Scout Base"
        print textwrap.fill(portdesc[self.starport], width = 54)
        print
        if self.size == 0: print "Asteroid complex"
        else: print "{:,} miles diameter".format(self.size * 1000)
        print atmodesc[self.atmosphere]
        if self.hydro == 0: print "No free-standing water"
        else: print "{}% of surface is water".format(self.hydro * 10)
        print "{:,} est. population".format(10 ** self.population)
        print "\nGovernment:"
        print textwrap.fill(govdesc[self.government], width = 54)
        print "\nLaw Level:"
        print textwrap.fill(lawdesc[self.law], width = 54)
        print "\nTech Index =", self.techindex
        print
        for i in range(len(technames)): print technames[i], techdesc[self.techindex][i]
        
        
try:
    newworld = World(sys.argv[1])
    newworld.create_world()
    newworld.print_world()
except IndexError:
    worldname = raw_input("World Name: ")
    newworld = World(worldname)
    newworld.create_world()
    newworld.print_world()
    