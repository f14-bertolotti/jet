import seaborn, pandas, click
from commands import default_options

@click.group(invoke_without_command=True)
@click.pass_obj
@default_options
def line(
        plotobj, 
        input_path, 
        nrows, 
        label, 
        color, 
        x, 
        y,
        ax
    ): 
    seaborn.lineplot(
        data  = pandas.read_json(input_path, lines=True, nrows=nrows)[[x, y]],
        x     = x,
        y     = y,
        color = color,
        label = label if label else os.path.basename(input_path),
        ax    = plotobj.axs[ax[0]][ax[1]]
    )
    
