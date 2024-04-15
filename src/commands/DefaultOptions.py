from utils import Color
from utils import chain
import click

default_options = chain(
    click.option("--input-path" , "input_path" , type = click.Path() , default = "data.jsonl" , help = "jsonl input data file."),
    click.option("--nrows"      , "nrows"      , type = int          , default = None         , help = "The number of lines from the line-delimited jsonfile that has to be read."),
    click.option("--label"      , "label"      , type = str          , default = "0"          , help = "label for the legend."),
    click.option("--color"      , "color"      , type = Color()      , default = None         , help = "plot color."),
    click.option("--x"          , "x"          , type = str          , default = "x"          , help = "X-axis values."),
    click.option("--y"          , "y"          , type = str          , default = "y"          , help = "Y-axis values."),
    click.option("--ax"         , "ax"         , type = (int,int)    , default = (0,0)        , help = "grid indices for the plot."),
)


