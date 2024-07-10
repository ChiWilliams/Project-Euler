#Problem 8

#We start by breaking the number into an array

from functools import reduce

num = [""]* 21
num[0] = ""
num[1] = str(73167176531330624919225119674426574742355349194934)
num[2] = str(96983520312774506326239578318016984801869478851843)
num[3] = str(85861560789112949495459501737958331952853208805511)
num[4] = str(12540698747158523863050715693290963295227443043557)
num[5] = str(66896648950445244523161731856403098711121722383113)
num[6] = str(62229893423380308135336276614282806444486645238749)
num[7] = str(30358907296290491560440772390713810515859307960866)
num[8] = str(70172427121883998797908792274921901699720888093776)
num[9] = str(65727333001053367881220235421809751254540594752243)
num[10] = str(52584907711670556013604839586446706324415722155397)
num[11] = str(53697817977846174064955149290862569321978468622482)
num[12] = str(83972241375657056057490261407972968652414535100474)
num[13] = str(82166370484403199890008895243450658541227588666881)
num[14] = str(16427171479924442928230863465674813919123162824586)
num[15] = str(17866458359124566529476545682848912883142607690042)
num[16] = str(242190226710556263211111093705442175069416589604080)
num[17] = str(7198403850962455444362981230987879927244284909188)
num[18] = str(845801561660979191338754992005240636899125607176060)
num[19] = str(5886116467109405077541002256983155200055935729725)
num[20] = str(71636269561882670428252483600823257530420752963450)



big_num = reduce(lambda a,b: a+b,num)
max_prod = 0
prod_length = 13

for i in range(len(big_num) - prod_length):
    prod = reduce(lambda a,b:int(a)*int(b),list(big_num[i:i+prod_length]))
    if prod > max_prod:
        max_prod = prod

print("The answer is", max_prod)