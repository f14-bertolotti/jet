from ast import literal_eval
import click

class Where(click.ParamType):
    def convert(self, value, param, ctx):
        name,op,value = value.split(",")
        value = literal_eval(value)
        assert type(name) == str
        assert type(op) == str
        tokens = name.split("/")

        def isok(line):
            for tok in tokens: line = line[tok]
            match op:
                case "==": return line == value
                case "!=": return line != value
                case ">=": return line >= value
                case "<=": return line <= value
                case ">" : return line >  value
                case "<" : return line <  value
            raise ValueError(f"invalid operator. Allowed ==, !=, >=, <=, >, <. got: {op}.")

        return isok
 
