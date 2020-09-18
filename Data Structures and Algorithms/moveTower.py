# coding: utf-8

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)  # 将除了最后一个盘子以外的其他所有盘子移到中点柱子
        move_disk(from_pole, to_pole)  # 将最后一个盘子移到终点柱子
        move_tower(height - 1, with_pole, to_pole, from_pole)  # 将之前的塔从中间柱子移到终点柱子


def move_disk(fp, tp):
    print("moving disk from", fp, "to", tp)

move_tower(3, "A", "B", "C")