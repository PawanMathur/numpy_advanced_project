#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    return ipl_matches_array[:,16] == '6'

#print ipl_matches_array[get_all_sixes_filter()][:10]
#print get_all_sixes_filter()[:10]
