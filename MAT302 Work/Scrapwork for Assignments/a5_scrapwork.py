# print((4*8+27*7)%23)

# for y in range(1, 23):
#     print(f"y = {y}, y^2 = {pow(y,2,23)}")
# for x in range(1, 23):
#     print(f"x = {x}, f(x) = {(pow(x,3,23)+2*x+7)%23}")
import sys
sys.path.append(".")
import EllipticCurves.addition as ec

point_set = [(5,2),(5,21),(8,11),(8,12),(9,8),(9,15),(11,7),(11,16),(15,10),
             (15,13),(16,8),(16,15),(17,3),(17,20),(19,2),(19,21),(21,8),
             (21,15),(22,2),(22,21),(0,0)]
generator_list = []
with open("Scrapwork for Assignments\generators_output.txt", "w") as f:
    for point in point_set:
        curr = point
        set = [point]
        for i in range(2, 8):
            curr = ec.add_points(curr, point, 2, 23)
            if curr == (0,0):
                f.write(f"{point} is not a generator; it has order {i}\n")
                break
        if curr != (0,0):
            generator_list.append(point)
            f.write(f"{point} is a generator\n")
    f.write(f"Generator list: {generator_list}\n")
    f.write(f"Each element generates E(F_23) in the following order:\n")
    for gen in generator_list:
        curr = gen
        gen_set = [gen]
        for i in range(2, 22):
            curr = ec.add_points(curr, gen, 2, 23)
            gen_set.append(curr)
        f.write(f"{gen} generates the elliptic curve in the order {gen_set}\n")


