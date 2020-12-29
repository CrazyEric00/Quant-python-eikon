import eikon as ek  # the Eikon Python wrapper package
import numpy as np  # NumPy
import pandas as pd  # pandas
import cufflinks as cf  # Cufflinks
import configparser as cp

from eikon import Profile as profile
profile.get_scripting_proxy_port = 49152

ek.set_app_id('0a845119ab7548339124ed3f965d50480c0f4205')