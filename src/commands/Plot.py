import matplotlib.pyplot as plt
import click

@click.group(invoke_without_command=True)
@click.pass_obj
@click.option("--show"         , "show"         , type = bool         , default = True   , help = "True if the plot has to be shown.")
@click.option("--output-path"  , "output_path"  , type = click.Path() , default = None   , help = "Output plot path.")
@click.option("--figsize"      , "figsize"      , type = (float,float), default = (None,None), help = "Figure size.")
@click.option("--tight"        , "tight"        , type = bool         , default = False  , help = "Tight layout.")
@click.option("--transparent"  , "transparent"  , type = bool         , default = False  , help = "Transparent background.")
def plot(plotobj, show, output_path, figsize, tight, transparent):
    if tight: plt.tight_layout()
    if show: plt.show()
    if figsize[0] is not None: plotobj.fig.set_figheight(figsize[0])
    if figsize[1] is not None: plotobj.fig.set_figwidth(figsize[1])
    if output_path: plotobj.fig.savefig(output_path, transparent = transparent)

