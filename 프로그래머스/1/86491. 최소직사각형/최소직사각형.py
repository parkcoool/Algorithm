def solution(sizes):
    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    w = max(max(widths), max(heights))
    h = max(min(size) for size in sizes)
    
    return w * h