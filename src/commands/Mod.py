import click
import matplotlib.pyplot as plt
from utils import set_spine_visibility

@click.group(invoke_without_command=True)
@click.option("--ax"                , "ax"           , type = (int, int)           , default = (0, 0)    , help = "grid indices for the plot.")
@click.option("--left-spine"        , "left_spine"   , type = bool                 , default = True      , help = "Controls the visibility of the left spine.")
@click.option("--right-spine"       , "right_spine"  , type = bool                 , default = True      , help = "Controls the visibility of the right spine.")
@click.option("--top-spine"         , "top_spine"    , type = bool                 , default = True      , help = "Controls the visibility of the top spine.")
@click.option("--bottom-spine"      , "bottom_spine" , type = bool                 , default = True      , help = "Controls the visibility of the bottom spine.")
@click.option("--y-label"           , "ylabel"       , type = str                  , default = None      , help = "Y axis label name.")
@click.option("--x-label"           , "xlabel"       , type = str                  , default = None      , help = "X axis label name.")
@click.option("--y-scale"           , "yscale"       , type = str                  , default = None      , help = "Y axis scale. e.g. linear, log, symlog, logit")
@click.option("--x-scale"           , "xscale"       , type = str                  , default = None      , help = "X axis scale. e.g. linear, log, symlog, logit")
@click.option("--y-lim"             , "ylim"         , type = (float,float)        , default = None      , help = "Y axis lim.")
@click.option("--x-lim"             , "xlim"         , type = (float,float)        , default = None      , help = "X axis lim.")
@click.option("--y-ticks"           , "yticks"       , type = str                  , default = "default" , help = "Y axis bins.")
@click.option("--x-ticks"           , "xticks"       , type = str                  , default = "default" , help = "X axis bins.")
@click.option("--title"             , "title"        , type = str                  , default = ""        , help = "Plot title.")
@click.option("--left-spine-color"  , "lsc"          , type = (float,float,float)  , default = None      , help = "Left spine color.")
@click.option("--right-spine-color" , "rsc"          , type = (float,float,float)  , default = None      , help = "Right spine color.")
@click.option("--top-spine-color"   , "tsc"          , type = (float,float,float)  , default = None      , help = "Top spine color.")
@click.option("--bottom-spine-color", "bsc"         , type = (float,float,float)  , default = None      , help = "Bottom spine color.")
@click.pass_obj
def mod(plotobj, title, ylabel, xlabel, yscale, xscale, xlim, ylim, left_spine, right_spine, top_spine, bottom_spine, xticks, yticks, ax, lsc, rsc, tsc, bsc):
    set_spine_visibility(
        ax = plotobj.axs[ax[0]][ax[1]],
        left_spine   = left_spine,
        right_spine  = right_spine,
        bottom_spine = bottom_spine,
        top_spine    = top_spine,
    )
    if yscale is not None: plotobj.axs[ax[0]][ax[1]].set_yscale(yscale)
    if xscale is not None: plotobj.axs[ax[0]][ax[1]].set_xscale(xscale)
    if ylim   is not None: plotobj.axs[ax[0]][ax[1]].set_ylim  (ylim)
    if xlim   is not None: plotobj.axs[ax[0]][ax[1]].set_xlim  (xlim)
    if ylabel is not None: plotobj.axs[ax[0]][ax[1]].set_ylabel(ylabel)
    if xlabel is not None: plotobj.axs[ax[0]][ax[1]].set_xlabel(xlabel)
    if rsc    is not None: plotobj.axs[ax[0]][ax[1]].spines['right' ].set_color(rsc)
    if tsc    is not None: plotobj.axs[ax[0]][ax[1]].spines['top'   ].set_color(tsc)
    if lsc    is not None: 
        plotobj.axs[ax[0]][ax[1]].spines['left'  ].set_color(lsc)
        plotobj.axs[ax[0]][ax[1]].yaxis.label.set_color(lsc)
        plotobj.axs[ax[0]][ax[1]].tick_params(axis='y', colors=lsc)
    if bsc    is not None: 
        plotobj.axs[ax[0]][ax[1]].spines['bottom'].set_color(bsc)
        plotobj.axs[ax[0]][ax[1]].xaxis.label.set_color(bsc)
        plotobj.axs[ax[0]][ax[1]].tick_params(axis='x', colors=bsc)

    match xticks:
        case "none": plotobj.axs[ax[0]][ax[1]].set_xticks([])
        case "default": pass
        case _: plotobj.axs[ax[0]][ax[1]].set_xticks(list(map(float, xticks.split(","))))
    match yticks:
        case "none": plotobj.axs[ax[0]][ax[1]].set_yticks([])
        case "default": pass
        case _: plotobj.axs[ax[0]][ax[1]].set_yticks(list(map(float, yticks.split(","))))

    plotobj.axs[ax[0]][ax[1]].set_title(title)

