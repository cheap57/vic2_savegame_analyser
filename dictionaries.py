pop_types=["aristocrats","capitalists","bureaucrats","clerks","officers","clergymen","artisans","slaves","soldiers","farmers","labourers","craftsmen"]
pop_stats=["id","size","cult","rel","money","con","mil","literacy","bank","life_needs","everyday_needs","luxury_needs","movement_issue","production_type","current_producing","production_income","needs_cost"]

goods_types=["ammunition", "small_arms", "artillery", "canned_food", "barrels", "aeroplanes", "cotton", "dye", "wool", "silk", "coal", "sulphur", "iron", "timber", "tropical_wood", "rubber", "oil", "precious_metal", "steel", "cement", "machine_parts", "glass", "fuel", "fertilizer", "explosives", "clipper_convoy", "steamer_convoy", "electric_gear", "fabric", "lumber", "paper", "cattle", "fish", "fruit", "grain", "tobacco", "tea", "coffee", "opium", "automobiles", "telephones", "wine", "liquor", "regular_clothes", "luxury_clothes", "furniture", "luxury_furniture", "radio"]
goods_stats=["worldmarket_pool", "price_pool", "last_price_history", "supply_pool", "last_supply_pool", "price_history", "price_history_last_update", "price_change", "actual_sold", "actual_sold_world", "real_demand", "demand"]

exclusion_list=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","{","}","type","id"]
#TODO
    #intégrer autres objets par listes et ajouter au dictionnaire de listes

obj_dict = {
  "pop_types": pop_types,
  "pop_stats": pop_stats,
  "goods_types": goods_types,
  "goods_stats": goods_stats
}
