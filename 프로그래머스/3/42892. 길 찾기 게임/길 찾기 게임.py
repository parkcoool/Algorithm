from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def 전위(tree, node):
    ans = [node]
    for child in tree[node]:
        ans.extend(전위(tree, child))
    return ans

def 후위(tree, node):
    ans = []
    for child in tree[node]:
        ans.extend(후위(tree, child))
    ans.append(node)
    return ans

def solution(nodeinfo):
    tree = defaultdict(list)
    nodes = [(i + 1, node) for i, node in enumerate(nodeinfo)]
    nodes.sort(key=lambda node: (-node[1][1], node[1][0]))
    
    root = -1
    
    # child_ys[y]: y좌표가 y인 부모 노드들의 자식 노드들의 y좌표
    child_ys = {}
    last_y = -1
    for num, (x, y) in nodes:
        if last_y == -1:
            root = num
            last_y = y
        elif last_y != y:
            child_ys[last_y] = y
            last_y = y
    
    def build_tree(parent_index, x1, x2):
        parent_num, (parent_x, parent_y) = nodes[parent_index]
        
        # 자식 찾기
        if parent_y not in child_ys: return
        for child_index in range(parent_index + 1, len(nodes)):
            child_num, (child_x, child_y) = nodes[child_index]
            if child_y < child_ys[parent_y]: break
            if child_y > child_ys[parent_y]: continue
            if not (x1 <= child_x <= x2): continue
            
            tree[parent_num].append(child_num)
            
            nx1 = x1 if child_x < parent_x else parent_x
            nx2 = x2 if child_x > parent_x else parent_x
            build_tree(child_index, nx1, nx2)
    
    build_tree(0, 0, 100000)
    return [전위(tree, root), 후위(tree, root)]
    