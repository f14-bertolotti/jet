from commands import reference, legend, scatter, line, palette, plot, mod
from collections  import namedtuple
import matplotlib.pyplot as plt
import matplotlib
import click

@click.group()
def jet(): pass

@jet.group(invoke_without_command=True)
@click.option("--shape", "shape", type=(int, int), default=(1, 1), help="grid plot size")
@click.option("--font"         , "font"         , type = str           , default = "serif" , help = "Font style.")
@click.option("--font-size"    , "fontsize"     , type = int           , default = 12      , help = "Font size.")
@click.pass_context
def init(context, shape, font, fontsize):

    if context.obj is not None: return

    matplotlib.rc('font', **{
        'family': font,
        'size': fontsize,
        'weight': 'normal'
    })

    fig, axs = plt.subplots(nrows=shape[0], ncols=shape[1])
    if shape[0] == 1: axs = [axs]
    if shape[1] == 1: axs = [[ax] for ax in axs]

    context.obj = namedtuple("Plot", "fig axs")(
        fig = fig,
        axs = axs
    )

def recursive_help(cmd, parent=None, visited=[]):
    ctx = click.core.Context(cmd, info_name=cmd.name, parent=parent)
    print(cmd.get_help(ctx))
    print()
    commands = getattr(cmd, 'commands', {})
    for sub in commands.values():
        if sub not in visited:
            recursive_help(sub, ctx, visited + [cmd])

@jet.command()
def dumphelp():
    recursive_help(jet, visited=[])

jet      .add_command(jet)
init     .add_command(jet)
jet      .add_command(scatter)
jet      .add_command(line)
jet      .add_command(mod)
jet      .add_command(legend)
legend   .add_command(jet)
mod      .add_command(jet)
line     .add_command(jet)
scatter  .add_command(jet)
reference.add_command(jet)
jet      .add_command(plot)
jet      .add_command(palette)
jet      .add_command(reference)

if __name__ == "__main__":
    jet()
