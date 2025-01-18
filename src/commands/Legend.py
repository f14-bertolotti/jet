import matplotlib.pyplot as plt
import click

@click.group(invoke_without_command=True)
@click.option("--ax"     , "ax"     , type=(int, int)                       , default = (0, 0), help = "grid indices for the plot.")
@click.option("--line"   , "lines"  , type=(str,float,float,float,float,str), default=[]      , help="add line to legend in the form of (label,color,width,style)", multiple=True)
@click.option("--frameon", "frameon", type=bool                             , default=False   , help="True if the legend frame should be showed")
@click.option("--cols"   , "cols"   , type=int                              , default=None    , help="Number of columns in the legend")
@click.option("--loc"    , "loc"    , type=str                              , default="best"  , help="Location of the legend")
@click.option("--shift"  , "shift"  , type=(float,float)                    , default=None    , help="Shift the legend by (x,y)")
@click.pass_obj
def legend(plotobj, lines, frameon, cols, loc, ax, shift):
    custom_handles = [plt.Line2D([0], [0], color=(colorx, colory, colorz), lw=lw, label=label, linestyle=style) for label, colorx, colory, colorz, lw, style in lines]
    plotobj.axs[ax[0]][ax[1]].legend(handles=custom_handles, loc=loc, frameon=frameon, ncol=cols if cols else 1, bbox_to_anchor=shift)
