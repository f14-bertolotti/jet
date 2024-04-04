from collections import namedtuple
import matplotlib.pyplot as plt
import seaborn, pandas, click


@click.group(invoke_without_command=True, context_settings={'show_default': True})
def cli(): pass

@cli.group(invoke_without_command=True, context_settings={'show_default': True})
@click.option("--input-path"  , "input_paths" , type=click.Path() , default=["data.jsonl"] , multiple = True, help="jsonl input data file.")
@click.option("--x"           , "xs"          , type=str          , default=["x"]        , multiple = True, help="X-axis values.")
@click.option("--y"           , "ys"          , type=str          , default=["y"]        , multiple = True, help="Y-axis values.")
@click.option("--output-path" , "output_path" , type=click.Path() , default=None         , help="output plot path.")
@click.option("--nrows"       , "nrows"       , type=int          , default=None         , help="The number of lines from the line-delimited jsonfile that has to be read.")
@click.option("--show"        , "show"        , type=bool         , default=True         , help="True if the plot has to be shown.")
@click.pass_context
def jet(context, input_paths, output_path, nrows, xs, ys, show):
    Options = namedtuple("Options", "input_paths output_path xs ys data show")
    context.obj = Options(
        input_paths  = input_paths,
        output_path  = output_path,
        data         = [pandas.read_json(path, lines=True, nrows=nrows)[[x, y]] for path,x,y in zip(input_paths, xs, ys)],
        xs           = xs,
        ys           = ys, 
        show         = show,
    )

@jet.command()
@click.pass_obj
def line(options): 
    for data,x,y in zip(options.data, options.xs, options.ys):
        seaborn.lineplot(
            data = data,
            x    = x,
            y    = y,
        )
    if options.show: plt.show()



if __name__ == "__main__":
    cli()
