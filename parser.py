import dictionaries as dico
import fonctions as do
import defines

import time
import csv


#import numpy as np

start_time = time.time()

#########################################
with open(defines.output, 'w', newline='') as output:
    pops = csv.writer(output)
    pops.writerow(["Date","province","provid","Country","Pop_size","pop_type","pop_cul","pop_rel","consciousness","militancy","literacy","life_needs","everyday_needs","luxury_needs","production_type","production_qty","production_value"
])
    with open(defines.input,'r') as f:
        lines = f.readlines()
        savegame=[0]

        for line in lines:
            savegame.append(line)

        curdate=savegame[1].replace("\"","").replace("date=","").strip()
        cur_pop=""
        cur_stat=""
        truc=""
        for x in range(len(savegame)):
            #truc+=cur_pop+"-"+cur_stat
            if do.get_obj_param("pop","types",str(savegame[x]).strip())!="":
                cur_pop="\r\n"+curdate+"-"+do.get_obj_param("pop","types",str(savegame[x]).strip())
                
            if do.get_obj_param("pop","stats",str(savegame[x]).strip())!="":
                cur_stat=do.get_obj_param("pop","stats",str(savegame[x]).strip())
            
            print (cur_pop+"-"+cur_stat)
            
#############           
##            isname = str(savegame[x]).find("name=")
##            isunit = str(savegame[x]).find(" ")
##            #if isname!=-1 and isunit!=4:
##
##            province=do.get_value(savegame[x],"name=")
##            province_id=do.get_value(savegame[x-2],"=")
##            owner=do.get_value(savegame[x+1],"owner=")
##            controller=do.get_value(savegame[x+2],"controller=")
##
##            if len(province_id)<=4:
##
##                cur_prov=province.replace("\"","")
##                cur_provid=province_id
##                cur_owner=owner
##                cur_controller=controller
##        #on a affaire à une pop: scrap les datas
##        if do.get_poptype(str(savegame[x]).strip())!="nope":
##            cur_pop=do.get_poptype(str(savegame[x]).strip())
##            cur_size=do.get_value(savegame[x+3],"size=")
##            cur_cul=do.get_culture(savegame[x+4].strip())
##            cur_rel=do.get_religion(savegame[x+4].strip())
##
##            is_mil =  str(savegame[x]).find("mil=")
#############
            #pops.writerow([curdate,cur_prov,cur_provid,cur_owner,cur_size,cur_pop,cur_cul,cur_rel])
            #print ([curdate,cur_prov,cur_provid,cur_owner,cur_size,cur_pop,cur_cul,cur_rel])
            
        #print (str(x))
        
            #do.get_obj_param("pop","stats",str(savegame[x]).strip())+str(x))
        #on a affaire à un rgo
        #on a affaire à un goods
print("--- %s seconds ---" % (time.time() - start_time))
