import functools, pandas, json

def set_spine_visibility(ax, right_spine, left_spine, top_spine, bottom_spine):
    ax.spines['right'] .set_visible(right_spine)
    ax.spines['left']  .set_visible(left_spine)
    ax.spines['top']   .set_visible(top_spine)
    ax.spines['bottom'].set_visible(bottom_spine)
    return ax

@functools.cache
def parse_file(path):
    with open(path, "r") as file:
        return [json.loads(line) for line in file]

def load_data(paths, samples=None, where=tuple(), dataslice=(None,None,None)):
    datas = [parse_file(path) for path in paths]

    # slice data
    datas = [data[slice(*dataslice)] for data in datas]

    # filter on conditions
    datas = [[line for line in data if all([cond(line) for cond in where])] for data in datas]

    # keep only sample rows from each data file
    for i in range(len(datas)):
        datas[i] = datas[i][::(max(1,len(datas[i])//samples)) if samples else 1]

    # load in pandas
    return pandas.json_normalize([line for data in datas for line in data], sep="/")
