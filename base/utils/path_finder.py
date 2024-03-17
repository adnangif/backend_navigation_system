from collections import deque

class Point:
    x = -1
    y = -1
    def __init__(self,_x:int,_y:int) -> None:
        self.x = _x
        self.y = _y

    def __hash__(self) -> int:
        return hash(repr((self.x,self.y)))
    
    def __eq__(self, ano) -> bool:
        if(self.x == ano.x and self.y == ano.y): 
            return True
        return False

    def __str__(self) -> str:
        return f"x:{self.x} y:{self.y}"

class Map:
    obstacles = [[]]
    parent:dict[Point, Point]={}
    directions:dict[Point,str] = {}
    x_axis_len = 0
    y_axis_len = 0
    starting_location = Point(-1,-1)

    def __init__(self, c_location:Point, obstacles:list[list[int]]) -> None:
        assert len(obstacles) >= 1
        assert c_location.x < len(obstacles)
        assert c_location.y < len(obstacles[0])

        self.obstacles = obstacles
        self.starting_location = c_location
        self.x_axis_len = len(obstacles)
        self.y_axis_len = len(obstacles[0])
    
        
    
    def is_valid_point(self,p:Point) -> bool:
        if(p.x < 0 or p.y < 0 or p.x >= self.x_axis_len or p.y >= self.y_axis_len):
            return False
        return True
    
    def path(self) -> str:
        str_path = ""
        c = Point(0,0)
        assert c in self.parent.keys()
        assert c in self.directions.keys()

        while(c != self.starting_location):
            str_path += self.directions[c]
            c = self.parent[c]
        
        return (str_path[::-1])

    def transformed_path(self) -> str:
        actual_path = self.path()
        new_path = ''

        altered = deque()
        altered.append('L')
        altered.append('U')
        altered.append('R')
        altered.append('D')

        memo = {
            'L':0,
            'U':1,
            'R':2,
            'D':3,
            }


        for current_command in actual_path:
            direction = altered[memo[current_command]]

            new_path += direction
            
            if(direction == 'L'):
                temp = altered.popleft()
                altered.append(temp)

            elif(direction == 'R'):
                temp = altered.pop()
                altered.appendleft(temp)

        return new_path
            
            


    def bfs(self) -> None:
        vis:list[Point] = []
        queue = deque()
        queue.append(self.starting_location)
        vis.append(self.starting_location)

        while(len(queue) != 0):
            c:Point = queue.popleft()

            up = Point(c.x - 1 , c.y)
            down = Point(c.x + 1 , c.y)
            left = Point(c.x, c.y - 1)
            right = Point(c.x, c.y + 1)

            if self.is_valid_point(up) and up not in vis and not self.obstacles[up.x][up.y] :
                queue.append(up)
                vis.append(up)
                self.parent[up] = c
                self.directions[up] = 'U'

            if self.is_valid_point(down) and down not in vis and not self.obstacles[down.x][down.y]:
                queue.append(down)
                vis.append(down)
                self.parent[down] = c
                self.directions[down] = 'D'


            if self.is_valid_point(left) and left not in vis and not self.obstacles[left.x][left.y]:
                queue.append(left)
                vis.append(left)
                self.parent[left] = c
                self.directions[left] = 'L'


            if (self.is_valid_point(right) and 
                right not in vis and 
                not self.obstacles[right.x][right.y]
                ):
                queue.append(right)
                vis.append(right)
                self.parent[right] = c
                self.directions[right] = 'R'



if __name__ =="__main__":
    m = Map(Point(5,3),
    [
        [0,1,1,1],
        [0,0,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,1,1,1],
        [0,0,0,0],
    ])
    m.bfs()
    print(m.path())
    print(m.transformed_path())