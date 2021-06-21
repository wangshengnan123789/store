data1 = 1
name1 = "羽绒服"
price1 = 253.6
num1 = 500
sale1 = 10

data2 = 2
name2 = "牛仔裤"
price2 = 86.3
num2 = 600
sale2 = 60

data3 = 3
name3 = "风衣"
price3 = 96.8
num3 = 335
sale3 = 43

data4 = 4
name4 = "皮草"
price4 = 135.9
num4 = 855
sale4 = 63

data5 = 5
name5 = "T血"
price5 = 65.8
num5 = 632
sale5 = 63

data6 = 6
name6 = "衬衫"
price6 = 49.3
num6 = 562
sale6 = 120

data7 = 7
name7 = "牛仔裤"
price7 = 86.3
num7 = 600
sale7 = 72

data8 = 8
name8 = "羽绒服"
price8 = 253.6
num8 = 500
sale8 = 69

data9 = 9
name9 = "牛仔裤"
price9 = 86.3
num9 = 600
sale9 = 35

data10 = 10
name10 = "羽绒服"
price10 = 253.6
num10 = 500
sale10 = 140

data11 = 11
name11 = "牛仔裤"
price11 = 86.3
num11 = 600
sale11 = 90

data12 = 12
name12 = "皮草"
price12 = 135.9
num12 = 855
sale12 = 24

data13 = 13
name13 = "T血"
price13 = 65.8
num13 = 632
sale13 = 45

data14 = 14
name14 = "风衣"
price14 = 96.8
num14 = 335
sale14 = 25

data15 = 15
name15 = "牛仔裤"
price15 = 86.3
num15 = 600
sale15 = 60

data16 = 16
name16 = "T血"
price16 = 65.8
num16 = 632
sale16 = 129

data17 = 17
name17 = "羽绒服"
price17 = 253.6
num17 = 500
sale17 = 10

data18 = 18
name18 = "风衣"
price18 = 96.8
num18 = 335
sale18 = 43

data19 = 19
name19 = "T血"
price19 = 65.8
num19 = 632
sale19 = 63

data20 = 20
name20 = "牛仔裤"
price20 = 86.3
num20 = 600
sale20 = 60

data21 = 21
name21 = "皮草"
price21 = 135.9
num21 = 855
sale21 = 63

data22 = 22
name22 = "风衣"
price22 = 96.8
num22 = 335
sale22 = 60

data23 = 23
name23 = "T血"
price23 = 65.8
num23 = 632
sale23 = 58

data24 = 24
name24 = "牛仔裤"
price24 = 86.3
num24 = 600
sale24 = 140

data25 = 25
name25 = "T血"
price25 = 65.8
num25 = 632
sale25 = 48

data26 = 26
name26 = "风衣"
price26 = 96.8
num26 = 335
sale26 = 43

data27 = 27
name27 = "皮草"
price27 = 135.9
num27 = 855
sale27 = 57

data28 = 28
name28 = "羽绒服"
price28 = 253.6
num28 = 500
sale28 = 10

data29 = 29
name29 = "T血"
price29 = 65.8
num29 = 632
sale29 = 63

data30 = 30
name30 = "风衣"
price30 = 96.8
num30 = 335
sale30 = 78

# 销售占比
# 羽绒服
print((sale1+sale8+sale10+sale17+sale28)/
      (sale1+sale2+sale3+sale4+sale5+sale6+sale7+sale8+sale9
       +sale10+sale11+sale12+sale13+sale14+sale15+sale16+sale7
       +sale18+sale19+sale20+sale21+sale22+sale23+sale24+sale25
       +sale26+sale27+sale28+sale29+sale30))
# 牛仔裤
print((sale2+sale7+sale9+sale11+sale15+sale20+sale24)/
      (sale1+sale2+sale3+sale4+sale5+sale6+sale7+sale8+sale9
       +sale10+sale11+sale12+sale13+sale14+sale15+sale16+sale7
       +sale18+sale19+sale20+sale21+sale22+sale23+sale24+sale25
       +sale26+sale27+sale28+sale29+sale30))
# 风衣
print((sale3+sale14+sale18+sale22+sale26+sale30)/
      (sale1+sale2+sale3+sale4+sale5+sale6+sale7+sale8+sale9
       +sale10+sale11+sale12+sale13+sale14+sale15+sale16+sale7
       +sale18+sale19+sale20+sale21+sale22+sale23+sale24+sale25
       +sale26+sale27+sale28+sale29+sale30))
# 皮草
print((sale4+sale12+sale21+sale27)/
      (sale1+sale2+sale3+sale4+sale5+sale6+sale7+sale8+sale9
       +sale10+sale11+sale12+sale13+sale14+sale15+sale16+sale7
       +sale18+sale19+sale20+sale21+sale22+sale23+sale24+sale25
       +sale26+sale27+sale28+sale29+sale30))
#T血
print((sale5+sale13+sale16+sale19+sale23+sale25+sale29)/
      (sale1+sale2+sale3+sale4+sale5+sale6+sale7+sale8+sale9
       +sale10+sale11+sale12+sale13+sale14+sale15+sale16+sale7
       +sale18+sale19+sale20+sale21+sale22+sale23+sale24+sale25
       +sale26+sale27+sale28+sale29+sale30))
# 衬衫
print((sale6)/
      (sale1+sale2+sale3+sale4+sale5+sale6+sale7+sale8+sale9
       +sale10+sale11+sale12+sale13+sale14+sale15+sale16+sale7
       +sale18+sale19+sale20+sale21+sale22+sale23+sale24+sale25
       +sale26+sale27+sale28+sale29+sale30))

# 销售额占比
# 羽绒服
print((sale1*price1+sale8*price8+sale10*price10+sale17*price17+sale28*price28)/
      (sale1*price1+sale2*price2+sale3*price3+sale4*price4
       +sale5*price5+sale6*price6+sale7*price7+sale8*price8+sale9*price9
       +sale10*price10+sale11*price11+sale12*price12+sale13*price13
       +sale14*price14+sale15*price15+sale16*price16+sale7*price17
       +sale18*price18+sale19*price19+sale20*price20+sale21*price21
       +sale22*price22+sale23*price23+sale24*price24+sale25*price25
       +sale26*price26+sale27*price27+sale28*price28+sale29*price29+sale30*price30))
# 牛仔裤
print((sale2*price2+sale7*price7+sale9*price9+sale11*price11
       +sale15*price15+sale20*price20+sale24*price24)/
      (sale1*price1+sale2*price2+sale3*price3+sale4*price4
       +sale5*price5+sale6*price6+sale7*price7+sale8*price8+sale9*price9
       +sale10*price10+sale11*price11+sale12*price12+sale13*price13
       +sale14*price14+sale15*price15+sale16*price16+sale7*price17
       +sale18*price18+sale19*price19+sale20*price20+sale21*price21
       +sale22*price22+sale23*price23+sale24*price24+sale25*price25
       +sale26*price26+sale27*price27+sale28*price28+sale29*price29
       +sale30*price30))
# 风衣
print((sale3*price3+sale14*price14+sale18*price18
       +sale22*price22+sale26*price26+sale30*price30)/
      (sale1*price1+sale2*price2+sale3*price3+sale4*price4
       +sale5*price5+sale6*price6+sale7*price7+sale8*price8+sale9*price9
       +sale10*price10+sale11*price11+sale12*price12+sale13*price13
       +sale14*price14+sale15*price15+sale16*price16+sale7*price17
       +sale18*price18+sale19*price19+sale20*price20+sale21*price21
       +sale22*price22+sale23*price23+sale24*price24+sale25*price25
       +sale26*price26+sale27*price27+sale28*price28+sale29*price29
       +sale30*price30))
# 皮草
print((sale4*price4+sale12*price12+sale21*price21+sale27*price27)/
      (sale1*price1+sale2*price2+sale3*price3+sale4*price4
       +sale5*price5+sale6*price6+sale7*price7+sale8*price8+sale9*price9
       +sale10*price10+sale11*price11+sale12*price12+sale13*price13
       +sale14*price14+sale15*price15+sale16*price16+sale7*price17
       +sale18*price18+sale19*price19+sale20*price20+sale21*price21
       +sale22*price22+sale23*price23+sale24*price24+sale25*price25
       +sale26*price26+sale27*price27+sale28*price28+sale29*price29
       +sale30*price30))
# T血
print((sale5*price5+sale13*price13+sale16*price16+sale19*price19
       +sale23*price23+sale25*price25+sale29*price29)/
      (sale1*price1+sale2*price2+sale3*price3+sale4*price4
       +sale5*price5+sale6*price6+sale7*price7+sale8*price8+sale9*price9
       +sale10*price10+sale11*price11+sale12*price12+sale13*price13
       +sale14*price14+sale15*price15+sale16*price16+sale7*price17
       +sale18*price18+sale19*price19+sale20*price20+sale21*price21
       +sale22*price22+sale23*price23+sale24*price24+sale25*price25
       +sale26*price26+sale27*price27+sale28*price28+sale29*price29
       +sale30*price30))
# 衬衫
print((sale6*price6)/
      (sale1*price1+sale2*price2+sale3*price3+sale4*price4
       +sale5*price5+sale6*price6+sale7*price7+sale8*price8+sale9*price9
       +sale10*price10+sale11*price11+sale12*price12+sale13*price13
       +sale14*price14+sale15*price15+sale16*price16+sale7*price17
       +sale18*price18+sale19*price19+sale20*price20+sale21*price21
       +sale22*price22+sale23*price23+sale24*price24+sale25*price25
       +sale26*price26+sale27*price27+sale28*price28+sale29*price29
       +sale30*price30))

#本月总销售额
print(sale1*price1+sale2*price2+sale3*price3+sale4*price4
       +sale5*price5+sale6*price6+sale7*price7+sale8*price8+sale9*price9
       +sale10*price10+sale11*price11+sale12*price12+sale13*price13
       +sale14*price14+sale15*price15+sale16*price16+sale7*price17
       +sale18*price18+sale19*price19+sale20*price20+sale21*price21
       +sale22*price22+sale23*price23+sale24*price24+sale25*price25
       +sale26*price26+sale27*price27+sale28*price28+sale29*price29
       +sale30*price30)