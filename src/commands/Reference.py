import click
import matplotlib.pyplot as plt
from utils import set_spine_visibility

@click.group(invoke_without_command=True)
@click.option("--ax"         , "ax"          , type = (int, int)          , default = (0, 0) , help = "grid indices for the plot.")
@click.option("--value"      , "value"       , type = float               , default = 0      , help = "jsonl input data files.")
@click.option("--label"      , "label"       , type = str                 , default = "0"    , help = "draws an horizontal dashed line.")
@click.option("--ax"         , "ax"          , type = (int,int)           , default = (0,0)  , help = "grid indices for the plot.")
@click.option("--color"      , "color"       , type = (float,float,float) , default = None   , help = "plot color.")
@click.option("--linewidth"  , "linewidth"   , type = float               , default = 1.0    , help = "line width.")
@click.pass_obj
def reference(plotobj, ax, value, color, linewidth, label):
    """ draws an horizontal dashed line  """

    ax = plotobj.axs[ax[0]][ax[1]]
    ax.axhline(y=value, color=color, linewidth=linewidth, linestyle="--", label=label)

