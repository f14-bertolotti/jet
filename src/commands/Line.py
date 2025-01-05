import seaborn, click, os
from commands import default_options
from utils    import load_data


@click.group(invoke_without_command=True)
@click.pass_obj
@default_options
@click.option("--linestyle", "linestyle", type = str, default = "-", help = "line style.")
def line(
        plotobj, 
        input_paths, 
        samples,
        dataslice,
        label, 
        color, 
        linewidth,
        linestyle,
        x, 
        y,
        ax, 
        where, 
        legend
    ): 

    data = load_data(paths=input_paths, samples=samples, where=where, dataslice=dataslice)
    seaborn.lineplot(
        data   = data,
        x      = x,
        y      = y,
        color  = color,
        linewidth = linewidth,
        linestyle = linestyle,
        label  = label if label else os.path.basename(input_paths[0]),
        legend = False if legend == "none" else legend,
        ax     = plotobj.axs[ax[0]][ax[1]],
    )
    
