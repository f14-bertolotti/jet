from ast import literal_eval
import click

class Color(click.ParamType):
    def convert(self, value, param, ctx):
        color = literal_eval(value)
        assert type(color) == tuple
        assert len(color) == 3
        assert all([type(c) in {float,int} for c in color])
        return color
 
