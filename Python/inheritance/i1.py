class Area:
    def __init__(self,l,w):
        self.__l=l
        self.__w =w
    
    def get_area(self):
        return self.__l * self.__w
    

class Volume(Area):
    def __init__(self,l,w,h):
        super().__init__(l,w)
        self.__h =h

    def get_volume(self):
        return self.get_area() * self.__h
    
class Density(Volume):
    def __init__(self, l, w, h,m):
        super().__init__(l, w, h)
        self.__m=m

    def get_density(self):
        return self.__m/self.get_volume()
    

d = Density(2,3,4,100)
density =d.get_density()
volume = d.get_volume()
area = d.get_area()
print(f"Density : {density:.2f}")
print(f"Volume : {volume}")
print(f"Area : {area}")