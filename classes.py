class Player(): # Player Sheet Class
    def __init__(self, name, background, p_class, species, p_subclass, level, xp, ac, prof, inititave, speed, size, pass_perception, heroic_inspiration):
        self.name = name
        self.background = background
        self.p_class = p_class
        self.species = species
        self.p_subclass = p_subclass
        self.level = level
        self.xp = xp
        self.ac = ac
        self.prof = prof
        self.inititave = inititave
        self.speed = speed
        self.size = size
        self.pass_perception = pass_perception
        self.heroic_inspiration = heroic_inspiration
        
    class hp: # Hit Points
        def __init__(self, current_hp, temp_hp, max_hp):
            self.current_hp = current_hp
            self.temp_hp = temp_hp
            self.max_hp = max_hp
    
    class intelligence: # Intelligence
        def __init__(self, modifier, score, saving_throw, arcana, history, investigation, nature, religion):
            self.modifier = modifier
            self.saving_throw = saving_throw
            self.arcana = arcana
            self.history = history
            self.investigation = investigation
            self.nature = nature
            self.score = score
            self.religion = religion
    
    class strength: # Strength
        def __init__(self, modifier, score, saving_throw, athletics):
            self.modifier = modifier
            self.saving_throw = saving_throw
            self.score = score
            self.athletics = athletics
        
    class dex: # Dexterety
        def __init__(self, modifier, score, saving_throw, acrobatics, sleight_of_hand, stealth):
            self.modifier = modifier
            self.saving_throw = saving_throw
            self.score = score
            self.acrobatics = acrobatics
            self.sleight_of_hand = sleight_of_hand
            self.stealth = stealth

    class wisdom: # Wisdom
        def __init__(self, modifier, score, saving_throw, animal_handling, insight, medicine, perception, survival):
            self.modifier = modifier
            self.saving_throw = saving_throw
            self.score = score
            self.animal_handling = animal_handling
            self.insight = insight
            self.medicine = medicine
            self.perception = perception
            self.survival = survival
                        
    class const: # Constitution
        def __init__(self, modifier, score, saving_throw):
            self.modifier = modifier
            self.saving_throw = saving_throw
            self.score = score
            
    class charisma: # Charisma
        def __init__(self, modifier, score, saving_throw, deception, intimidation, performance, persuasion):
            self.modifier = modifier
            self.saving_throw = saving_throw
            self.score = score
            self.deception = deception
            self.intimidation = intimidation
            self.performance = performance
            self.persuasion = persuasion