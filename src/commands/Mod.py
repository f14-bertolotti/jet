import click
from utils import set_spine_visibility

@click.group(invoke_without_command=True)
@click.option("--ax"           , "ax"           , type = (int, int)    , default = (0, 0) , help = "grid indices for the plot.")
@click.option("--left-spine"   , "left_spine"   , type = bool          , default = True   , help = "Controls the visibility of the left spine.")
@click.option("--right-spine"  , "right_spine"  , type = bool          , default = True   , help = "Controls the visibility of the right spine.")
@click.option("--top-spine"    , "top_spine"    , type = bool          , default = True   , help = "Controls the visibility of the top spine.")
@click.option("--bottom-spine" , "bottom_spine" , type = bool          , default = True   , help = "Controls the visibility of the bottom spine.")
@click.option("--y-label"      , "ylabel"       , type = str           , default = None   , help = "Y axis label name.")
@click.option("--x-label"      , "xlabel"       , type = str           , default = None   , help = "X axis label name.")
@click.option("--y-scale"      , "yscale"       , type = str           , default = None   , help = "Y axis scale. e.g. linear, log, symlog, logit")
@click.option("--x-scale"      , "xscale"       , type = str           , default = None   , help = "X axis scale. e.g. linear, log, symlog, logit")
@click.option("--y-lim"        , "ylim"         , type = (float,float) , default = None   , help = "Y axis lim.")
@click.option("--x-lim"        , "xlim"         , type = (float,float) , default = None   , help = "X axis lim.")
@click.option("--title"        , "title"        , type = str           , default = ""     , help = "Plot title.")
@click.pass_obj
def mod(plotobj, title, ylabel, xlabel, yscale, xscale, xlim, ylim, left_spine, right_spine, top_spine, bottom_spine, ax):
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
    plotobj.axs[ax[0]][ax[1]].set_title(title)

