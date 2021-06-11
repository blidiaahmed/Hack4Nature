import matplotlib.pyplot as plt
import itertools
from shapely.geometry import mapping, shape,Point,Polygon
import numpy as np
from json import load
from itertools import product


class city_inspectation:
    file_object="../Hack4Nature/data/limit_marseille.json"
    # minx=0
    # maxx=1
    # miny=0
    # maxy=1
    
    def __init__(self,e):
        #
        
        self.file_load()
        self.polygon=self.forming_polygon()
        
        self.framing_region()
        
    def file_load(self):
        with open(self.file_object) as f:

            self.Departement_file=load(f)
        return self.Departement_file
    def if_meet_city(self,grid=np.array([[0,0],[1,0],[0,1],[1,1]])):
        self.polygon=forming_polygon()
        for i in range(grid.shape[0]):
            point = Point(grid[i,0],grid[i,1])
            j=0
            found=False
            while j<len(self.polygon) and not found:
                if self.polygon[j].contains(point):
                    return True
                j+=1
            return False
    def forming_polygon(self):
        #"../Hack4Nature/data/limit_marseille.json"):
        self.sectors_array=self.Departement_file["features"][0]["geometry"]["coordinates"]
        #print(self.Departement_file)
        self.polygon=[]
        #print(sectors_array[0].shape)
        for j in range(7):
            #all_sectors.append(np.array(sector_array[j,0]))
            sector=self.sectors_array[j]
            
            sector=np.array(sector[0])
            
            #print([(sector[i,0],sector[i,1]) 
            #                       for i in range(sector.shape[0])])
            self.polygon.append(Polygon([(sector[i,0],sector[i,1])for i in range(sector.shape[0])]))
            
        #print(self.minx)
        return self.polygon
    
    def framing_region(self):
        self.all_sectors=np.concatenate([self.sectors_array[i][0] for i in range(7)])
        self.minx=min(self.all_sectors[:,1])
        self.maxx=max(self.all_sectors[:,1])
        self.miny=min(self.all_sectors[:,0])
        self.maxy=max(self.all_sectors[:,0])
        return [self.minx,self.maxx,self.miny,self.maxy]

    def forming_grid(self,size#,minx=minx,maxx=maxx,miny=miny,maxy=maxy
    ):
        #print(self.maxx)
        sector=self.sectors_array[0][0]
        maxx=max([sector[i][0] for i in range(len(sector))])
        minx=min([sector[i][0] for i in range(len(sector))])
        maxy=max([sector[i][1] for i in range(len(sector))])
        miny=min([sector[i][1] for i in range(len(sector))])
        l1=np.linspace(minx,maxx,size[0])
        l2=np.linspace(miny,maxy,size[1])
        self.grid=list(product(l1,l2))
        self.grid=np.array(self.grid)
        return self.grid
    def visualise_data(self,size=(4,4)):
        self.forming_grid(size)
        
        island_points_colors=[]
        sea_points_colors=[]
        island_points=[]
        lsstt=[]
        lsst=[]
        for i in range(self.grid.shape[0]):
                point = Point(self.grid[i,0],self.grid[i,1]) 
                j=0
                found=False
                while j<len(self.polygon) and not found:
                    
                    if self.polygon[j].contains(point):
                        island_points_colors.append(3+j)
                        island_points.append(self.grid[i,:])
                        found=True
                    j+=1
                if not found:
                    lsstt.append(self.grid[i,:])
                    sea_points_colors.append(0)    
        island_points=np.array(island_points)
        lsst=np.array(lsst)
        lsstt=np.array(lsstt)
        print((len(island_points_colors)))
        island_points_colors[len(island_points_colors)-1]=0
        plt.scatter(island_points[:,1],island_points[:,0])#,s=10,c=island_points_colors) 
        plt.scatter(lsstt[:,1],lsstt[:,0],s=11,c=sea_points_colors)