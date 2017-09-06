from cycleList import *
from triangle import *



def get_first_earFor(c:CycleList)->(int,int):
    
    for e in c:
        triangle=Triangle(e.previous_node.data,e.data,e.next_node.data)
        if triangle.is_valid():
            continue

        if triangle.any_inside(map(lambda y:y.data,filter(lambda x: x.data not in triangle ,c))):
            continue
        else:
            return e,triangle

def get_first_ear(cycle_list: CycleList) -> (Node, Triangle):
    node = cycle_list.pointer
    while True:
        triangle = Triangle(node.previous_node.data, node.data, node.next_node.data)

        any_inside = False

        node_2 = node.next_node
        while not any_inside and node != node_2:
            if node_2.data not in triangle:
                any_inside = any_inside or triangle.is_inside(node_2.data)
            node_2 = node_2.next_node

        if triangle.is_valid() and not any_inside:
            return node, triangle

        node = cycle_list.next()


def get_triangle_list_from_polygon(l: list()) -> list():
    cycle_list = CycleList()
    for element in l:
        cycle_list.push(element)

    triangle_list = []

    for _ in range(len(l) - 2):
        ear_node, triangle = get_first_ear(cycle_list)
        triangle_list.append(triangle)
        cycle_list.pop()

    return triangle_list


if __name__ == "__main__":
    #    print(get_first_ear(CycleList().push((0, 0)).push((10, 0)).push((0, 10)).push((1, 1)).push((10, 5))))
    print(get_triangle_list_from_polygon([(0, 0), (5, 0), (0, 5), (-5, 5)]))
