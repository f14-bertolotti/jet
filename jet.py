from collections import namedtuple
import matplotlib.pyplot as plt
import seaborn, pandas, click, os

from ast import literal_eval

class Color(click.ParamType):
    def convert(self, value, param, ctx):
        color = literal_eval(value)
        assert type(color) == tuple
        assert len(color) == 3
        assert all([type(c) in {float,int} for c in color])
        return color
    

@click.group(invoke_without_command=True, context_settings={'show_default': True})
@click.option("--shape", "shape", type=(int, int), default=(1, 1), help="grid plot size")
@click.pass_context
def jet(context, shape):
    if context.obj is not None: return

    fig, axs = plt.subplots(nrows=shape[0], ncols=shape[1])
    if shape[0] == 1: axs = [axs]
    if shape[1] == 1: axs = [[ax] for ax in axs]
    Plot = namedtuple("Plot", "fig axs")
    context.obj = Plot(
        fig = fig,
        axs = axs
    )

@jet.command()
@click.option("--name"   , "name"   , type=str , default="plasma" , help="palette name")
@click.option("--length" , "length" , type=int , default=5        , help="palette samples")
@click.option("--index"  , "index"  , type=int , default=0        , help="palette index")
def palette(name, length, index):
    print(",".join(map(str,seaborn.color_palette(name, length)[index])))


@jet.group()
@click.pass_obj
@click.option("--input-path" , "input_path" , type = click.Path() , default = "data.jsonl" , help = "jsonl input data file.")
@click.option("--nrows"      , "nrows"      , type = int          , default = None         , help = "The number of lines from the line-delimited jsonfile that has to be read.")
@click.option("--label"      , "label"      , type = str          , default = "0"          , help = "label for the legend.")
@click.option("--color"      , "color"      , type = Color()      , default = None         , help = "plot color.")
@click.option("--x"          , "x"          , type = str          , default = "x"          , help = "X-axis values.")
@click.option("--y"          , "y"          , type = str          , default = "y"          , help = "Y-axis values.")
@click.option("--ax"         , "ax"         , type = (int,int)    , default = (0,0)        , help = "grid indices for the plot.")
def line(plotobj, input_path, nrows, label, color, x, y, ax): 
    seaborn.lineplot(
        data  = pandas.read_json(input_path, lines=True, nrows=nrows)[[x, y]],
        x     = x,
        y     = y,
        color = color,
        label = label if label else os.path.basename(input_path),
        ax    = plotobj.axs[ax[0]][ax[1]]
    )

@jet.command()
@click.pass_obj
@click.option("--show"        , "show"        , type = bool         , default = True , help = "True if the plot has to be shown.")
@click.option("--output-path" , "output_path" , type = click.Path() , default = None , help = "output plot path.")
def plot(plotobj, show, output_path):
    if show: plt.show()
    if output_path: plotobj.fig.savefig(output_path)

line.add_command(jet)

if __name__ == "__main__":
    jet()
