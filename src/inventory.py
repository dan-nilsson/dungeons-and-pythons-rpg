from item import Item

class Inventory:
    def __init__(self,items=None,size=10):
        self.items = items if items else []
        self.size = size

    def __str__(self) -> str:
        return '\n'.join([f'{i}. {item}' for i,item in enumerate(self.items,start=1)])

    def add_item(self,item) -> bool:
        if self.size > len(self.items) and item: 
            self.items.append(item)
            return True
        else: 
            print(f'Inventory full or invalid item.')
            return False

    def remove_item(self,item):
        self.items.remove(item)
