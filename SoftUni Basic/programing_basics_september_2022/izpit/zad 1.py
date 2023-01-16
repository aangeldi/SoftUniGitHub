#  Опаковъчна
# хартия - 5.80
# лв.за
# ролка
#  Плат - 7.20
# лв.за
# ролка
#  Лепило - 1.20
# лв.за
# литър

rolls_paper = int(input())
rolls_cloth = int(input())
glue = float(input())
discoutn = int(input())

rolls_paper_price = 5.80
rolls_cloth_price = 7.20
glue_price = 1.20
total = rolls_paper * rolls_paper_price + rolls_cloth * rolls_cloth_price + glue * glue_price
total = total - total*discoutn/100
print(f"{total:.3f}")
