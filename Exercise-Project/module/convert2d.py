import numpy as np
import pandas as pd
import json

def convert_3d_to_2d(file_2d, file_3d):
    with open(file_2d) as datafile:
        data = json.load(datafile)
    df = pd.DataFrame(data)