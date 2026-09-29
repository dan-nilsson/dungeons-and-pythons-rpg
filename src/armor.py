from item import Item

armor_slots = ['helm','body','gloves','boots']

class Armor(Item):
    def __init__(self,name,slot,rarity='Common',attrib=None):
        super().__init__(name,rarity,attrib)
        self.slot = slot if slot in armor_slots else 'unknown'

    def get_item_type(self):
        return 'armor'

    def get_slot(self):
        return self.slot

linen_armors = {    'helm' : Armor('Linen Hat','helm',attrib={'int':10,'armor':10}),
                    'body' : Armor('Linen Robe','body',attrib={'int':15,'armor' : 10}),
                    'gloves' : Armor('Linen Mits','gloves',attrib={'armor' : 10}),
                    'boots' : Armor('Linen Slippers','boots',attrib={'armor' : 10})
}
leather_armors = {  'helm' : Armor('Leather Cap','helm',attrib={'stam':10,'armor':15}),
                    'body' : Armor('Leather Tunic','body',attrib={'stam':15,'armor' : 15}),
                    'gloves' : Armor('Leather Handwraps','gloves',attrib={'str':10,'armor' : 15}),
                    'boots' : Armor('Leather Boots','boots',attrib={'armor' : 15})
}
plate_armors = {    'helm' : Armor('Plate Visor','helm',attrib={'stam':10,'armor':20}),
                    'body' : Armor('Plate Breastplate','body',attrib={'stam':15,'armor' : 20}),
                    'gloves' : Armor('Plate Handguards','gloves',attrib={'stam':10,'armor' : 20}),
                    'boots' : Armor('Plate Stirrups','boots',attrib={'armor' : 20})
}