import dictionaries
def get_value(string,lookupstring):
    return str(string).strip().replace(lookupstring,"").replace("\"","")

#######fonctions pour stats de pop, à unifier?#############
def get_culture(string):
    middle=string.find("=")
    return string[:middle]
def get_religion(string):
    middle=string.find("=")+1
    return string[middle:]
##########fonction pour identifier une pop. eventuellement à remplacer################
def get_poptype(string):
    match dictionaries.pop_types.count(string.replace("=","")):
        case 1:
            poptype=string.replace("=","")
        case _:
            poptype="nope"
    return poptype
#######################################
#fonction pour scanner l'intérieur d'un objet dans un niveau et en retourner toutes les valeurs de stats
    #exemple: le parser tombe sur une pop, la fonction vérifie les stats de pop et les cherche dans la string courante. si c'est une stat, la fonction renvoie une chaine [stat, valeur]
    #le parser créée une variable cur_getobjparam(x,y,z)[0] de valeur getobjparam(x,y,z)[1]
def get_obj_param(obj_type,obj_stats,teststring):
    #for stats in dictionaries.obj_dict[obj_type+"_"+obj_stats]:
    match dictionaries.obj_dict[obj_type+"_"+obj_stats].count(teststring.replace("=","")):
        case 1:
            #stat=[stats,teststring.replace(stats+"=","")]
            #stat=stats+": "+teststring.replace(stats+"=","")]
            #print (stat)
            return teststring.replace("=","")
        case _:
            return ""

#get_obj_param("pop","types",1,10)
