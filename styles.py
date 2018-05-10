# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:04:02 2018

@author: Frederik
"""

def marker_line(
        color="black",
        width=2,
        dash="solid"
        ):
    return dict(color=color, width=width, dash=dash)

def marker_point(
        size=10,
        color="white",
        line=None
        ):
    if line is None:
        line = marker_line(color="grey")
    return dict(size=size, color=color, line=line)

def font(
        color="black",
        size=14
        ):
    return dict(color=color, size=size)

def hoverlabel(
        font=None
        ):
    hlab = dict()
    if font is not None:
        hlab["font"] = font
    else:
        hlab["font"] = font()
    
    return hlab

def axis(title="",
         autorange=True,
         autotick=True,
         zeroline=False,
         showline=True,
         zerolinewidth=20,
         zerolinecolor="blue",
         linewidth=2,
         linecolor="#42B8CE",
         showticklabels=True,
         tickangle=0,
         tickwidth=1,
         tickfont=font(),
         showgrid=True,
         _range=None):
    ax = dict(
            title=title,
            autorange=autorange,
            autotick=autotick,
            zeroline=zeroline,
            showline=showline,
            zerolinewidth=zerolinewidth,
            zerolinecolor=zerolinecolor,
            linewidth=linewidth,
            linecolor=linecolor,
            showticklabels=showticklabels,
            tickangle=tickangle,
            tickwidth=tickwidth,
            tickfont=tickfont,
            showgrid=showgrid
            )
    
    if _range is not None:
        ax["range"] = _range
        
    return ax

def layout(title="",
           xaxis=axis(tickangle=-45, showgrid=False),
           yaxis=axis(),
           margin=None):   
    layout = dict(
            title=title,
            xaxis=xaxis,
            yaxis=yaxis
            )
            
    if isinstance(margin, dict):
        layout["margin"] = margin
            
    return layout