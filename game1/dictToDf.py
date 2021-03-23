# -*- coding: utf-8 -*-

import pandas as pd
from monkeylearn import MonkeyLearn
import json
import numpy as np


ml = MonkeyLearn('b7c9b60a4a1a33752602958fcec16aeedd72bf49')
model_id = 'cl_A2hjXMXV'


data = ["large social gathering indoors", "sewing by myself", "walking in the park", "sleeping in my bed"]
result = ml.classifiers.classify(model_id, data)

r = result.body
print('----------')
print(r)

#TODO: these might need to be updated...
allDf = pd.DataFrame({'text':pd.Series([], dtype='str'),
                   'inside':pd.Series([], dtype='float'),
                   'outside':pd.Series([], dtype='float'),
                   '> 6 feet distance':pd.Series([], dtype='float'),
                   '< 6 feet distance':pd.Series([], dtype='float'),
                   'touching':pd.Series([], dtype='float'),
                   'low travel exposure':pd.Series([], dtype='float'),
                   'medium travel exposure':pd.Series([], dtype='float'),
                   'high travel exposure':pd.Series([], dtype='float'),
                   '< 4 people':pd.Series([], dtype='float'),
                   '4-25 people':pd.Series([], dtype='float'),
                   '> 25 people':pd.Series([], dtype='float'),
                   })
  


for ret in r:
    d = ret['classifications']

    df = pd.DataFrame.from_dict(d)
    confidence = df['confidence'].values.reshape(1, len(df))
    columns = df['tag_name']
    df = pd.DataFrame(confidence, columns=columns)
    df['text'] = ret['text']
    
    allDf = allDf.append(df)
    
