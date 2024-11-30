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
        label, 
        color, 
        linewidth,
        x, 
        y,
        ax,
        where,
        legend
    ):
    data = load_data(paths = input_paths, samples = samples, where = where)
    seaborn.scatterplot(
        data  = data,
        x     = x,
        y     = y,
        color = color,
        linewidth = linewidth,
        label = label if label else os.path.basename(input_paths[0]),
        legend= False if legend == "none" else legend,
        ax    = plotobj.axs[ax[0]][ax[1]]
    )
