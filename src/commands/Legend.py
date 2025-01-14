import matplotlib.pyplot as plt
import click

@click.group(invoke_without_command=True)
@click.option("--line", "lines", type=(str,float,float,float,float,str), default=[], multiple=True, help="add line to legend in the form of (label,color,width,style)")
@click.option("--frameon", "frameon", type=bool, default=False, help="True if the legend frame should be showed")
@click.pass_obj
def legend(plotobj, lines, frameon):
    custom_handles = [plt.Line2D([0], [0], color=(colorx, colory, colorz), lw=lw, label=label, linestyle=style) for label, colorx, colory, colorz, lw, style in lines]
    plt.legend(handles=custom_handles, loc='best', frameon=frameon)
