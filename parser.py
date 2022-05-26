import time
import csv
#import numpy as np

start_time = time.time()

pop_types=["aristocrats","capitalists","bureaucrats","clerks","officers","clergymen","artisans","slaves","soldiers","farmers","labourers","craftsmen"]
pop_stats=["id","size","cult","rel","money","con","mil","literacy","bank","life_needs","everyday_needs","luxury_needs","movement_issue","production_type","current_producing","production_income","needs_cost"]
obj_dict = {
  "pop_types": pop_types,
  "pop_stats": pop_stats
}
def get_value(string,lookupstring):
    return string.strip().replace(lookupstring,"").replace("\"","")

#######fonctions pour stats de pop, à unifier?#############
def get_culture(string):
    middle=string.find("=")
    return string[:middle]
def get_religion(string):
    middle=string.find("=")+1
    return string[middle:]
##########fonction pour identifier une pop. eventuellement à remplacer################
def get_poptype(string):
    match pop_types.count(string.replace("=","")):
        case 1:
            poptype=string.replace("=","")
        case _:
            poptype="nope"
    return poptype
#######################################
#fonction pour scanner l'intérieur d'un objet dans un niveau et en retourner toutes les valeurs de stats
#exemple: le parser tombe sur une pop, la fonction liste les stats de pop et les cherche dans les { } correspondants
def get_obj_param(obj_type,obj_stats,floor,ceiling):
    for stats in obj_dict[obj_type+"_"+obj_stats]:
        print (stats)
get_obj_param("pop","types",1,10)
#########################################
with open('output/ouput.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(["province","provid","Country","Pop_size","pop_type","pop_cul","pop_rel","consciousness","militancy","literacy","life_needs","everyday_needs","luxury_needs","production_type","production_qty","production_value"
])
    with open('input/autosave.v2','r') as f:
        lines = f.readlines()
        savegame=[0]
        
        for line in lines:
            savegame.append(line)
        
        date=savegame[1].replace("\"","").replace("date=","")
        
        for x in range(len(savegame)):
            isname = str(savegame[x]).find("name=")
            isunit = str(savegame[x]).find(" ")
            if isname!=-1 and isunit!=4:
                
                province=get_value(savegame[x],"name=")
                province_id=get_value(savegame[x-2],"=")
                owner=get_value(savegame[x+1],"owner=")
                controller=get_value(savegame[x+2],"controller=")
                
                if len(province_id)<=4:
                    
                    cur_prov=province.replace("\"","")
                    cur_provid=province_id
                    cur_owner=owner
                    cur_controller=controller
            #on a affaire à une pop: scrap les datas        
            if get_poptype(str(savegame[x]).strip())!="nope":
                cur_pop=get_poptype(str(savegame[x]).strip())
                cur_size=savegame[x+3].strip().replace("size=","")
                cur_cul=get_culture(savegame[x+4].strip())
                cur_rel=get_religion(savegame[x+4].strip())

                is_mil =  str(savegame[x]).find("mil=")
                
                #writer.writerow([cur_prov,cur_provid,cur_owner,cur_size,cur_pop,cur_cul,cur_rel])
            #on a affaire à un rgo
            #on a affaire à un goods
print("--- %s seconds ---" % (time.time() - start_time))
