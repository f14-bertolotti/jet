import matplotlib.pyplot as plt
import click

@click.group(invoke_without_command=True)
@click.pass_obj
@click.option("--show"         , "show"         , type = bool         , default = True  , help = "True if the plot has to be shown.")
@click.option("--output-path"  , "output_path"  , type = click.Path() , default = None  , help = "Output plot path.")
def plot(plotobj, show, output_path):
    if show: plt.show()
    if output_path: plotobj.fig.savefig(output_path)


