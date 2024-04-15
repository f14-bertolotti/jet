import seaborn, click

@click.group(invoke_without_command=True)
@click.option("--name"   , "name"   , type=str , default="plasma" , help="palette name")
@click.option("--length" , "length" , type=int , default=5        , help="palette samples")
@click.option("--index"  , "index"  , type=int , default=0        , help="palette index")
def palette(name, length, index):
    print(",".join(map(str,seaborn.color_palette(name, length)[index])))

