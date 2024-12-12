import click

class Nint(click.ParamType):
    name = "nint"

    def convert(self, value, param, ctx):
        match value:
            case "None": return None
            case _     : return int(value)

nint = Nint()
