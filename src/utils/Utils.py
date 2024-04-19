import json

def set_spine_visibility(ax, right_spine, left_spine, top_spine, bottom_spine):
    ax.spines['right'] .set_visible(right_spine)
    ax.spines['left']  .set_visible(left_spine)
    ax.spines['top']   .set_visible(top_spine)
    ax.spines['bottom'].set_visible(bottom_spine)
    return ax

def load_data(paths, nrows):
    files = [open(path, "r") for path in paths]
    data = [json.loads(line) for file in files for _,line in (zip(range(nrows), file) if nrows else enumerate(file))]
    for file in files: file.close()
    return data
 
