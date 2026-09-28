class Inventory:
    def __init__(self,items=None,size=10):
        self.items if items else []
        self.size = size

    def list_items(self) -> [str]:
        return [f'{i}. {item}' for i,item in enumerate(self.items,start=1)]

    def add_item(self,item) -> bool:
        if size > len(items): 
            self.append(item)
            return True
        else: 
            print(f'Inventory full.')
            return False

    def remove_item(self,item):
        self.items.remove(item)
