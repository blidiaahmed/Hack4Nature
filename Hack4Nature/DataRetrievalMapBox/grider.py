import random
import matplotlib.pyplot as plt
import itertools
from shapely.geometry import mapping, shape,Point,Polygon
import numpy as np
from json import load
from itertools import product
import os

class city_inspectation:
    file_object="Hack4Nature/data/limit_marseille.json"
    # minx=0
    # maxx=1
    # miny=0
    # maxy=1
    
    def __init__(self):
        self.file_load()
        self.polygon=self.forming_polygon()
        self.framing_region()
    def file_load(self):
        with open(self.file_object) as f:

            self.Departement_file=load(f)
        return self.Departement_file

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
        self.minx=min(self.all_sectors[:,0])
        self.maxx=max(self.all_sectors[:,0])
        self.miny=min(self.all_sectors[:,1])
        self.maxy=max(self.all_sectors[:,1])
        return [self.minx,self.maxx,self.miny,self.maxy]

    def forming_grid(self,size):
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
        #print((len(island_points_colors)))
        island_points_colors[len(island_points_colors)-1]=0
        plt.scatter(island_points[:,1],island_points[:,0])#,s=10,c=island_points_colors) 
        plt.scatter(lsstt[:,1],lsstt[:,0],s=11,c=sea_points_colors)

    def if_meet_city(self,grid=np.array([[0,0],[1,0],[0,1],[1,1]])):
        #self.polygon=forming_polygon()
        for i in range(grid.shape[0]):
            point = Point(grid[i,0],grid[i,1])
            j=0
            found=False
            while j<len(self.polygon) and not found:
                if self.polygon[j].contains(point):
                    return True
                j+=1
            return False
    def if_in_city(self,point):
        #self.polygon=forming_polygon()
        
        point = Point(point[0],point[1])
        j=0
        found=False
        while j<len(self.polygon) and not found:
            if self.polygon[j].contains(point):
                return True
            j+=1
        return False

    
    def pick_point(self,number,size=(100,100)):
        #print(self.minx,self.maxx)
        l1=np.linspace(self.minx,self.maxx,size[0])
        l2=np.linspace(self.miny,self.maxy,size[1])   
        
        points=[]
        for i in range(1,number+1):
            inside=False
            while not inside:    
                r1=random.randint(0,len(l1)-1)
                r2=random.randint(0,len(l2)-1)
                #print(r1,r2)
                point=[l1[r1],l2[r2]]
                #print(self.if_in_city(point),point)
                if self.if_in_city(point):
                    inside =True
                    points.append(point)
        return points
"""
sector=self.sectors_array[0][0]
maxx=max([sector[i][0] for i in range(len(sector))])
minx=min([sector[i][0] for i in range(len(sector))])
maxy=max([sector[i][1] for i in range(len(sector))])
miny=min([sector[i][1] for i in range(len(sector))])
"""

                




class requester_mapbox:
    

    def request(self,mapbox_api_key,coordinates_box,path_to_file="""raw_data/mapbox_tests/satellite/example-mapbox-static-bbox-2.png"""):

        str1="""curl -g "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/["""
        str2=str(coordinates_box [0])+','+str(coordinates_box[1])+','+str(coordinates_box[2])+','+str(coordinates_box[3])
        str3= """]/400x400?padding=50,10,20&access_token="""
        str4="""" --output """
        strtot=str1+str2+str3+mapbox_api_key+str4+path_to_file
        #print(strtot)
        os.system(strtot)
        return 0
    def request_zoom(self,mapbox_api_key,coordinates,path_to_file="""raw_data/mapbox_tests/satellite-zoom/example-mapbox-static-zoom.png"""):

        str1="""curl -g "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"""
        str2=str(coordinates[0])+','+str(coordinates[1])
        str3= """/400x400?padding=50,10,20&access_token="""
        str4="""" --output """
        strtot=str1+str2+str3+mapbox_api_key+str4+path_to_file
        #print(strtot)
        os.system(strtot)
        return 0
    def request_packet(self,MAPBOX_TOKEN,obj,number=10,dimensions=(0.001,0.001)):
        
        
        point=obj.pick_point(number,(100,100))
        #print(point)
        for i in range(number):
            ls=[point[i][0],point[i][1],point[i][0]+0.000151,point[i][1]+0.000151]
            path_to_file="raw_data/mapbox_tests/satellite-only-city/Marseille-city-"+str(i)+"-"+str(round(ls[0],3))+","+str(round(ls[1],3))+".png"
            self.request(MAPBOX_TOKEN,ls,path_to_file) 
            #print("\n ----------------- ",i,"--------------",path_to_file)


"""
if __name__ == "__main__":
    os.system("sh key.sh")
    #point=obj.pick_point(10)
    MAPBOX_TOKEN=os.environ.get("MAPBOX_TOKEN")
    MAPBOX_TOKEN=""
    obj=city_inspectation()
    obj.minx=5.376537
    obj.miny=43.291301
    obj.maxx=5.404442
    obj.maxy=43.309708
    #ls=[point[0][0],point[0][1],point[0][0]+0.001,point[0][1]+0.001]
    req=requester_mapbox()#.request(MAPBOX_TOKEN,ls)
    req.request_packet(MAPBOX_TOKEN,obj,10)
"""


if __name__ == "__main__":
    os.system("sh key.sh")
    #point=obj.pick_point(10)
    MAPBOX_TOKEN=os.getenv("MAPBOX_TOKEN")#os.environ.get("MAPBOX_TOKEN")
    #MAPBOX_TOKEN=""
    ls=[5.376537,43.291301]
    req=requester_mapbox()#.request(MAPBOX_TOKEN,ls)
    req.request_zoom(MAPBOX_TOKEN,ls)