# -*- coding: utf-8 -*-
##########################################################################
# File name : config.py
# Usages : Description of the module
# Start date : Thu Jan 04 13:09:58 2018
# Last review : Thu Jan 04 13:09:58 2018
# Version : 0.1
# Author(s) : Julien Vachaudez - julien.vachaudez@cerisic.be
# License : The pycta project is distributed under the GNU General Public
#           License version 3 (https://www.gnu.org/licenses/gpl-3.0.html)
# Dependencies : Python 2.7
##########################################################################

import os

# Constants for configuration

CWD = os.getcwd()
CSV_PATH = os.path.join(CWD, "csv")
NBR_OF_SECONDS_BETWEEN_TWO_SAMPLES = 3.0

# Minimum duration for one visit (in seconds)
# Below this value the visit is deleted
MIN_VISIT_DURATION = 180

# Number of seconds to delete at the begining of the visit (in seconds)
# if these are not the same the CH4/CO2 value will take the longest in consideration
DELETE_SECONDS_CO2 = 30
DELETE_SECONDS_CH4 = 30

# Maximums for each curve, in absolute, per scale (B01, B02)
MAX_CO2_B01 = 1.7
MAX_CO2_B02 = 1.7

MAX_CH4_B01 = 0.2
MAX_CH4_B02 = 0.2

# Minimums for each curve, in relatve (in percentile), per scale (B01, B02)
MIN_PERCENTILE_CO2_B01 = 5 # in %
MIN_PERCENTILE_CO2_B02 = 5

MIN_PERCENTILE_CH4_B01 = 5 # in %
MIN_PERCENTILE_CH4_B02 = 5

