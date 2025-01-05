from utils import Where
from utils import chain
from utils import nint
import click

default_options = chain(
    click.option("--input-path" , "input_paths" , type = click.Path()        , default = ["data.jsonl"]   , help = "jsonl input data files.", multiple = True),
    click.option("--samples"    , "samples"     , type = int                 , default = None             , help = "The number of lines in the final data."),
    click.option("--slice"      , "dataslice"   , type = (nint,nint,nint)    , default = (None,None,None) , help = "The number of lines to skip."),
    click.option("--label"      , "label"       , type = str                 , default = "0"              , help = "label for the legend."),
    click.option("--x"          , "x"           , type = str                 , default = "x"              , help = "X-axis values."),
    click.option("--y"          , "y"           , type = str                 , default = "y"              , help = "Y-axis values."),
    click.option("--ax"         , "ax"          , type = (int,int)           , default = (0,0)            , help = "grid indices for the plot."),
    click.option("--where"      , "where"       , type = Where()             , default = []               , help = "evaluatable condition used as filter", multiple=True),
    click.option("--legend"     , "legend"      , type = str                 , default = "auto"           , help = "legend type"),
    click.option("--color"      , "color"       , type = (float,float,float) , default = None             , help = "plot color."),
    click.option("--linewidth"  , "linewidth"   , type = float               , default = 1.0              , help = "line width."),
)


