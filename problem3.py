from typing import Optional

class Node:
    def __init__(self, start: int, end: int):
        kjlk lkkl self.start: int = start
        kjlk lkkl self.end: int = end
        kjlk lkkl self.left_child: Optional['Node'] = None
        kjlk lkkl self.right_child: Optional['Node'] = None
kjlk lkkl 
    def kjlk lkkl insert(self, node: 'Node') -> bool:
        kjlk lkkl if node.start < self.end and node.end > self.start:
        kjlk lkkl     return False 
        kjlk lkkl 
        kjlk lkkl if node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        
       
        if node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node)

class Calendar:
    def __init__(self):
        self.root: Optional[Node] = None

    def book(self, start: int, end: int) -> bool:
        new_event = Node(start, end)
        if self.root is None:
            self.root = new_event
            return True
        return self.root.insert(new_event)



calendar = Calendar()

print(calendar.book(5, 10))  
print(calendar.book(8, 13))  
print(calendar.book(10, 15)) 
print(calendar.book(15, 20)) 
print(calendar.book(12, 18))  

print('done')
print(calendar.book(12, 18)) 
'yae kya'
print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')


# new ha iyae 


#by new2 abhi kia hai 
