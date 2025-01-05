import matplotlib.pyplot as plt
import click

@click.group(invoke_without_command=True)
@click.pass_obj
@click.option("--show"         , "show"         , type = bool         , default = True   , help = "True if the plot has to be shown.")
@click.option("--output-path"  , "output_path"  , type = click.Path() , default = None   , help = "Output plot path.")
@click.option("--figsize"      , "figsize"      , type = (float,float), default = (10,10), help = "Figure size.")
@click.option("--tight"        , "tight"        , type = bool         , default = False  , help = "Tight layout.")
def plot(plotobj, show, output_path, figsize, tight):
    if tight: plt.tight_layout()
    if show: plt.show()
    plotobj.fig.set_figheight(figsize[0])
    plotobj.fig.set_figwidth(figsize[1])
    if output_path: plotobj.fig.savefig(output_path)

