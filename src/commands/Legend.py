from utils import Color
import matplotlib.pyplot as plt
import click

@click.group(invoke_without_command=True)
@click.option("--line", "lines", type=(str,Color(),float), default=[], multiple=True, help="add line to legend in the form of (label,color,width)")
@click.option("--frameon", "frameon", type=bool, default=False, help="True if the legend frame should be showed")
@click.pass_obj
def legend(plotobj, lines,frameon):
    custom_handles = [plt.Line2D([0], [0], color=color, lw=lw, label=label) for label, color, lw in lines]
    plt.legend(handles=custom_handles, loc='best', frameon=frameon)
