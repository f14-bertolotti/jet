import click
from utils import set_spine_visibility

@click.group(invoke_without_command=True)
@click.option("--ax"           , "ax"           , type = (int, int) , default = (0, 0) , help = "grid indices for the plot.")
@click.option("--left-spine"   , "left_spine"   , type = bool       , default = True   , help = "Controls the visibility of the left spine.")
@click.option("--right-spine"  , "right_spine"  , type = bool       , default = True   , help = "Controls the visibility of the right spine.")
@click.option("--top-spine"    , "top_spine"    , type = bool       , default = True   , help = "Controls the visibility of the top spine.")
@click.option("--bottom-spine" , "bottom_spine" , type = bool       , default = True   , help = "Controls the visibility of the bottom spine.")
@click.option("--y-label"      , "ylabel"       , type = str        , default = None   , help = "Y axis label name.")
@click.option("--x-label"      , "xlabel"       , type = str        , default = None   , help = "X axis label name.")
@click.option("--title"        , "title"        , type = str        , default = ""     , help = "Plot title.")
@click.pass_obj
def mod(plotobj, title, ylabel, xlabel, left_spine, right_spine, top_spine, bottom_spine, ax):
    set_spine_visibility(
        ax = plotobj.axs[ax[0]][ax[1]],
        left_spine   = left_spine,
        right_spine  = right_spine,
        bottom_spine = bottom_spine,
        top_spine    = top_spine,
    )
    if ylabel is not None: plotobj.axs[ax[0]][ax[1]].set_ylabel(ylabel)
    if xlabel is not None: plotobj.axs[ax[0]][ax[1]].set_xlabel(xlabel)
    plotobj.axs[ax[0]][ax[1]].set_title(title)

