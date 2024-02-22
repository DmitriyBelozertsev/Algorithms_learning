#-----------------------------------------------------------------------#
#          made for this course https://stepik.org/course/5608          #
#-----------------------------------------------------------------------#
from collections import deque
class node_int(int):
    def __init__(self,x):
        int.__init__(self)
        self.color = True   #true denotes unread node, false denotes read
    def change_color_from_true_to_false(self, color = False):
        self.color = color
    def change_color_from_false_to_true(self):
        self.color = True
        
        
class graph():
    def __init__(self, G, V):
        self.G: int =  G
        self.V: int = V
        self.G_set = [node_int(i) for i in range(1,G+1)]
        self.vertices: dict[int, list[int]] = {}
    def add_vertice(self,x,y):
        x = node_int(x)
        y = node_int(y)
        self.G_set[x-1] = x
        self.G_set[y-1] = y
        zx = self.vertices.get(x)
        zy = self.vertices.get(y)
        #print('zx', zx)
        #print('zy', zy)
        if zx == None:
            self.vertices.update({x:[y]})
        else:
            self.vertices.update({x:zx+[y]})
        if zy == None:
            self.vertices.update({y:[x]})
        else:
            self.vertices.update({y:zy+[x]})
            
    def wfw(self):
        G_stack = deque(self.G_set) #стэк из вершин
        components = 0
        walk_queue = deque()
                
        for i1 in self.G_set:
            if i1.color == False:
                continue
            else:
                walk_queue.append(i1)
                while walk_queue.__len__() != 0:
                    z1 = walk_queue.popleft()
                    z1.color = False
                    z1_values = self.vertices.get(z1,None)
                    if z1_values == None:
                        continue
                    z1_values = [z2 for z2 in z1_values if z2.color== True]
                    if z1_values==[]:
                        z1_values = None
                    if z1_values == None:
                        continue
                    else:
                        for e1 in z1_values:
                            walk_queue.append(e1)
                else:
                    components+=1
        return components
        
        
        
G, V =  [int(i) for i in input().split()]
baron = graph(G,V)
for i in range(V):
    x , y =  [int(i) for i in input().split()]  
    baron.add_vertice(x, y)

print(baron.wfw())
