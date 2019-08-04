class Parent(object):
    def __init__(self):
        print("PARENT INIT")
        self.species = "human"
        self.arms = 2
        self.legs = 2
        self.head = 1
        self.torso = 1
        self.hair_color = "blonde"
    def set_hair_color(self,hair_color):
        print("Parent Function")
        self.hair_color = hair_color
    def set_arms_count(self,arms_count):
        self.arms = int(arms_count)
    def set_legs_count(self,arms_count):
        self.arms = int(arms_count)
    def set_head_count(self,arms_count):
        self.arms = int(arms_count)

class MaleChild(Parent):
    '''call child init, by default will init parent without this method'''
    def __init__(self):
        print("CHILD INIT")
        '''call parent init if you want those init vars!'''
        Parent.__init__(self)
        '''DISCLAIMER: These are generalizations for concept and should not represent any sort of gender stereotyping'''
        self.get_into_trouble = True
        self.likes_gi_joes = True
        self.likes_barbies = False
        self.hair_color = "brown"
        self.eye_color = "blue"
        self.height_inch = 46
        '''notice this method is being overriding the parent'''
    def set_hair_color(self,hair_color):
        print("Child Function")
        self.hair_color = hair_color
    def set_eye_color(self, eye_color):
        self.eye_color = eye_color

class FemaleChild(Parent):
    '''call child init, by default will init parent without this method'''
    def __init__(self):
        print("CHILD INIT")
        '''call parent init to inherit'''
        Parent.__init__(self)
        '''DISCLAIMER: These are generalizations for concept and should not represent any sort of gender stereotyping'''
        self.get_into_trouble = False
        self.likes_gi_joes = False
        self.likes_barbies = True

        self.hair_color = "brown"
        self.eye_color = "blue"
        self.height_inch = 46
        '''notice this method is being overriding the parent'''
    def set_hair_color(self,hair_color):
        print("Child Function")
        self.hair_color = hair_color
    def set_eye_color(self, eye_color):
        self.eye_color = eye_color

male_child_ob_instance = MaleChild()
male_child_ob_instance.set_arms_count(4)
male_child_ob_instance.set_hair_color("red")
serialized_male_child = male_child_ob_instance.__dict__
print(serialized_male_child)

female_child_ob_instance = FemaleChild()
female_child_ob_instance.set_legs_count(3)
female_child_ob_instance.set_hair_color("black")
serialized_female_child = female_child_ob_instance.__dict__
print(serialized_female_child)