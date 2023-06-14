#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   project_one.py
@Time    :   2023/06/14 15:08:22
@Author  :   Andres Bonilla 
@Version :   1.0
@Contact :   cabonillao.oc@gmail.com
@License :   (C)Copyright 2023-2024, Andres Bonilla
@Desc    :   toy script for git training 
'''

from typing import Union
import pandas as pd
import numpy as np

def add_values(
        value_1: Union[int,float],
        value_2: Union[int,float]
        ) -> Union[int,float] :
    """returns the sume of two values

    Args:
        value_1 (Union[int,float]): the first value
        value_2 (Union[int,float]): the second value
        
    Returns:
        Union[int,float]: the sum of value_1 and value_2
    """
    return value_1 + value_2
    