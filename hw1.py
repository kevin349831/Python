
#程式練習1：貸款攤銷表#


ir = 0.0237 #利率 -元大商業銀行利率
np = 20 #年
pv = 7000000 #貸款金額

ir = ir / 12
np = np * 12

#最後本金償還計算函數
def final(ir, np, pv):
    final = ( ir * ( pv * (ir+1)**np) ) / ( ( ir + 1 ) * ( (ir+1)**np -1 ) )
    #ir = interest rate per month
    #np = number of periods (months)
    #pv = present value
    return final
    

final_num = final(ir, np, pv) #將變數帶入函數計算 final_num為最後本金償還
pmt = final_num + (final_num * ir) #round 四捨五入 pmt為分期支出金額

print('+--------------------------------------------------------+')
print('| 期數 | 期   初 |  每期支出 | 利 息 | 本金償還 |   期末欠款   |')
print('+--------------------------------------------------------+')
print('|  0  |    0    |    0    |   0   |    0    |  ',pv,' |')

i = 1
while i != (np+1):
    print('+--------------------------------------------------------+')
    num1 = i
    num2 = pv
    num3 = pmt
    num4 = pv * ir
    num5 = num3 - num4
    pv = pv - num5
    num6 = pv
    if i != np:
        print('| ',num1,' |',round(num2),'|  ',round(num3),'|',round(num4),'| ',round(num5),' |  ',round(num6),' |')
    else:
        print('| ',num1,' |',round(num2),'|  ',round(num3),'|',round(num4),' | ',round(num5),' |  ',round(num6),'    |')
    i = i+1 # 調整控制變數值
print('+------------------------------------------------------+')

