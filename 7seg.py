# 7-segment display simulator in Minecraft PI
# マイクラ世界に7セグで16進数0からFを表示する

from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

# MCPI空間での7セグ表示、最上位桁の左下座標
X_BASE = 0
Y_BASE = 20
Z_BASE = 5

# 各桁の間隔
X_SIZE = 6

# 7セグの配置
# 各ブロック、左下原点*(0,0)からのオフセット(x,y)
# y:
# 6     A A       A0(1, 6)  A1(2, 6)
# 5   F     B     F1(0, 5)  B1(3, 5)
# 4   F     B     F0(0, 4)  B0(3, 4)
# 3     G G       G0(1, 3)  G1(2, 3)
# 2   E     C     E1(0, 2)  C1(3, 2)
# 1   E     C     E0(0, 1)  C0(3, 1)
# 0   * D D       D0(1, 0)  D1(2, 0)
# x:  0 1 2 3

offset_A = ((1, 6), (2, 6))
offset_B = ((3, 4), (3, 5))
offset_C = ((3, 1), (3, 2))
offset_D = ((1, 0), (2, 0))
offset_E = ((0, 1), (0, 2))
offset_F = ((0, 4), (0, 5))
offset_G = ((1, 3), (2, 3))

# 表示する数字／記号のon/off情報
# セグメントAからGについて7種類、「タプル」で用意する。
# リストではなくタプルを使うのは、情報が定数として扱われ不変であるため。リストでも動く。
# 読み出し方法は同様。タプルは最初の定義以降、書き換える操作ができない。
# 加えて、各セグメントのオフセット情報を16番目の要素、セグメント名を17番目の要素として持つ。
seg_A = (1, 0, 1, 1,   0, 1, 1, 1,   1, 1, 1, 0,   1, 0, 1, 1,  offset_A, "A")
seg_B = (1, 1, 1, 1,   1, 0, 0, 1,   1, 1, 1, 0,   0, 1, 0, 0,  offset_B, "B")
seg_C = (1, 1, 0, 1,   1, 1, 1, 1,   1, 1, 1, 1,   0, 1, 0, 0,  offset_C, "C")
seg_D = (1, 0, 1, 1,   0, 1, 1, 0,   1, 1, 0, 1,   1, 1, 1, 0,  offset_D, "D")
seg_E = (1, 0, 1, 0,   0, 0, 1, 0,   1, 0, 1, 1,   1, 1, 1, 1,  offset_E, "E")
seg_F = (1, 0, 0, 0,   1, 1, 1, 0,   1, 1, 1, 1,   1, 0, 1, 1,  offset_F, "F")
seg_G = (0, 0, 1, 1,   1, 1, 1, 0,   1, 1, 1, 1,   0, 1, 1, 1,  offset_G, "G")

# タプルの読み出し方法。インデックスとして3を指定。0番目、1番目、2番目、3番目。
# print(seg_A[3])

# さらに、タプルのタプルを作る。
segments = (seg_A, seg_B, seg_C, seg_D, seg_E, seg_F, seg_G)


def print_seg(num=4):
    # タプル内のタプルを順次読み出す（リストでも同じやり方）
    # タプルsegments内のタプル(seg_Aからseg_B)をsegmentとして順次取り出し、num番目の要素を読み出す。
    for segment in segments:
        print(segment[num])


def print_style(num=3):
    # 数字0から15までに対応する各セグメントのon/off情報を一覧する
    # jは、セグメント名用のインデックス
    print("number: ", num)
    for segment in segments:
        if segment[num] == 1:
            style = "on"
        else:
            style = "off"
        print(segment[17], ": ", style)


# print("\n")
# print("num=3")
# print_style(num=3)

print("\n")
print("all numbers")
for num in range(16):
    print_style(num=num)
    print("\n")


BLOCK_TYPE_ON = 41
BLOCK_DATA_ON = 0
BLOCK_TYPE_OFF = 0
BLOCK_DATA_OFF = 0


def update_7seg_MCPI(col=0, num=3):  # ある桁をある数字にする関数
    # numをMCPIでcol桁目にブロック表示
    for segment in segments:
        if segment[num] == 1:
            block_type = BLOCK_TYPE_ON
            block_data = BLOCK_DATA_ON
        else:
            block_type = BLOCK_TYPE_OFF
            block_data = BLOCK_DATA_OFF

        x0 = X_BASE + X_SIZE * col
        y0 = Y_BASE
        z0 = Z_BASE

        x1, y1 = segment[16][0]
        x2, y2 = segment[16][1]

        mc.setBlock(x0 + x1, y0 + y1, z0, block_type, block_data)
        mc.setBlock(x0 + x2, y0 + y2, z0, block_type, block_data)


# 0, 1, 2, 3, 4, 5を表示する。

update_7seg_MCPI(col=0, num=0)
update_7seg_MCPI(col=1, num=1)
update_7seg_MCPI(col=2, num=2)
update_7seg_MCPI(col=3, num=3)
update_7seg_MCPI(col=4, num=4)
update_7seg_MCPI(col=5, num=5)

# 0からFを表示。ずっと繰り返し。

while True:
    for i in range(16):
        update_7seg_MCPI(col=0, num=i)
        sleep(1.0)
