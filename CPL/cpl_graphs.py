#!/usr/bin/python
import numpy as np
import datetime
import matplotlib.pyplot as plt

import sys
import os.path
from textwrap import wrap

########################################################################################
# plotInfoDic = {'colorLst'          : ['b*', 'r'],               \
#                'legendLst'         : ['Result1', 'Result2'],    \
#                'xTicksValues'      : xLabelValues,              \
#                'xTicksValuesStep'  : 1,                         \
#                'xTicksOrientation' : 90,                        \
#                'title'             : 'This is the title',       \
#                'xLabel'            : 'Time',                    \
#                'yLabel'            : 'Product values'
########################################################################################


########################################################################################
# @brief Create comparison plots between 2 results for a list of bands/products
# @param yValuesPairLst         (array of float)        list of pairs of y-values
# @param plotInfoDic            (dictionary)            dictionary containing plot settings
# @param savePath               (string)                path to store figure
def showComparisonPlot(yValuesPairLst, plotInfoDic, savePath=''):
    plt.clf()
    # Create a new fig object: it will be used later on for tight_layout
    fig, ax = plt.subplots()

    # Set colours
    if 'colorLst' in plotInfoDic.keys():
        colors = plotInfoDic['colorLst']
        for yValues, colour in zip(yValuesPairLst, colors) :
            plt.plot(yValues, colour)
    else:
        for yValues, colour in zip(yValuesPairLst, cm.rainbow(np.linspace(0, 1, len(yValuesPairLst)))) :
            plt.plot(yValues, color=colour)

    # Set the locations and labels of the xticks
    # Set step to 1 if not defined
    step = plotInfoDic['xTicksValuesStep'] if 'xTicksValuesStep' in plotInfoDic.keys() else 1
    # Set x label orientation to 0 if not defined
    rotation = plotInfoDic['xTicksOrientation'] if 'xTicksOrientation' in plotInfoDic.keys() else 0

    # Set x-ticks
    if 'xTicksValues' in plotInfoDic.keys():
        xTicksPos = np.array(xrange(len(plotInfoDic['xTicksValues'])))
        xTicksPos = xTicksPos[::step].tolist()
        xTicksValues = plotInfoDic['xTicksValues'][::step]
        plt.xticks(xTicksPos, xTicksValues , rotation=rotation)

    # Set x and y labels
    if 'xLabel' in plotInfoDic.keys():
        plt.xlabel(plotInfoDic['xLabel'])
    if 'yLabel' in plotInfoDic.keys():
        plt.ylabel(plotInfoDic['yLabel'])

    # Set legend and title
    if 'legendLst' in plotInfoDic.keys():
        plt.legend(plotInfoDic['legendLst'], loc='best')
    if 'title' in plotInfoDic.keys():
        # Handle long titles: create multiple lines using wrap
        # Title line fixed for the moment at 60 characters
        plt.title("\n".join(wrap(plotInfoDic['title'], 60)))

    # Use tight lay out to ensure all x,y labels are on figure and are not cropped
    fig.tight_layout()

    # Save Plot
    print savePath
    if savePath != '':
        dirPath = os.path.dirname(savePath)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        plt.savefig(savePath)
