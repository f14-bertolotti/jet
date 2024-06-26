import seaborn, click, os
from commands import default_options
from utils    import load_data

@click.group(invoke_without_command=True)
@click.pass_obj
@default_options
def scatter(
        plotobj, 
        input_paths, 
        samples,
        nrows, 
        label, 
        color, 
        x, 
        y,
        ax
    ):
    data = load_data(paths = input_paths, nrows = nrows, samples = samples)
    seaborn.scatterplot(
        data  = data,
        x     = x,
        y     = y,
        color = color,
        label = label if label else os.path.basename(input_paths[0]),
        ax    = plotobj.axs[ax[0]][ax[1]]
    )
