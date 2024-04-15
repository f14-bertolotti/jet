
def set_spine_visibility(ax, right_spine, left_spine, top_spine, bottom_spine):
    ax.spines['right'] .set_visible(right_spine)
    ax.spines['left']  .set_visible(left_spine)
    ax.spines['top']   .set_visible(top_spine)
    ax.spines['bottom'].set_visible(bottom_spine)
    return ax
