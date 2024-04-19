from collections import namedtuple
import matplotlib.pyplot as plt
from commands import scatter, line, palette, plot, mod
import click

@click.group()
def jet(): pass

@jet.group(invoke_without_command=True)
@click.option("--shape", "shape", type=(int, int), default=(1, 1), help="grid plot size")
@click.pass_context
def init(context, shape):
    if context.obj is not None: return

    fig, axs = plt.subplots(nrows=shape[0], ncols=shape[1])
    if shape[0] == 1: axs = [axs]
    if shape[1] == 1: axs = [[ax] for ax in axs]

    Plot = namedtuple("Plot", "fig axs")
    context.obj = Plot(
        fig = fig,
        axs = axs
    )

jet     .add_command(jet)
init    .add_command(jet)
jet     .add_command(scatter)
jet     .add_command(line)
jet     .add_command(mod)
mod     .add_command(jet)
line    .add_command(jet)
scatter .add_command(jet)
jet     .add_command(plot)
jet     .add_command(palette)

if __name__ == "__main__":
    jet()
