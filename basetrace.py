# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:16:04 2018

@author: Frederik
"""

import plotly.graph_objs as go
import styles

def bartrace(df,
             name=None,
             layout=None, 
             hovertext="perc",
             markercolor="blue",
             opacity=1):
    if layout is None:
        layout = styles.layout()
    
    trace = go.Bar(
            x=df.iloc[:, 0],
            y=df.iloc[:, 1],
            marker=dict(color=markercolor),
            opacity=opacity
            )
    
    if hovertext is not None:
        if hovertext == "perc":
            hovtxt = ((df.iloc[:, 1] / df.iloc[:, 1].sum()).round(2) *
                      100).astype(int).astype(str) + "%"
        else:
            hovtxt = hovertext
    
        trace["text"] = hovtxt
        
    if name is not None:
        trace["name"] = name
        
    return trace

def scattertrace(df,
                 name=None,
                 mode="lines+markers",
                 layout=None,
                 markers=None, # pass markers as named dict, e.g. dict(line=..., marker=...)
                 text=None,
                 hoverinfo = "text", #"none" for no hover
                 hoverlabel=None,
                 opacity=1):
    
    trace = go.Scatter(
            x=df.iloc[:, 0],
            y=df.iloc[:, 1],
            mode=mode,
            hoverinfo = hoverinfo,
            opacity=opacity
            )
    
    if name is not None:
        trace["name"] = name
    
    if markers is not None and isinstance(markers, dict):
        trace.update(markers)
    else:
        mode_fun_lookup = dict(lines = styles.marker_line(), markers = styles.marker_point()) #CALL STYLES LIB HERE
        modes = mode.split("+")
        for m in modes:
            trace[m[:-1]] = mode_fun_lookup[m]
            
    if text is not None:
        trace["text"] = text
        
    if hoverlabel is not None:
        trace["hoverlabel"] = hoverlabel
    else:
        trace["hoverlabel"] = styles.hoverlabel() #CALL STYLES LIB HERE

    return trace