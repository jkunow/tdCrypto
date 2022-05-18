### TP CRYPTO ARITHMETIQUE MODULAIRE ###
### RSA

import random
from math import sqrt

# consider changing it to test stability
random.seed(1)


##Q1
# retourne le pgcd de deux entiers naturels
def pgcd(x, y):
    while x % y != 0:
        if y > x:
            x, y = y, x
        x = x % y
    return y


# print(pgcd(91,14))

##algo euclide etendu
# retourne d,u,v avec pgcd(x,y)=d=ux+vy
def euclide_ext(x, y):
    if x == 0:
        return y, 0, 1

    pgcd, x1, y1 = euclide_ext(y % x, x)

    u = y1 - (y // x) * x1
    v = x1

    return pgcd, u, v


# x,y=57000,77
# pgcd,u,v = euclide_ext(x,y)

# print(x, ' * ', u, ' + ', y, ' * ', v, ' = ', pgcd)

##Q2
##retourne un entier b dans [1,N-1] avec ab=1 modulo N
def inverse_modulaire(a, n):
    g, x, y = euclide_ext(a, n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % n
    return a

#print(inverse_modulaire(7,20))

##Q3
##retourne (b**e) % n
##ne manipule que des entiers <= b*b-b
def expo_modulaire(e, b, n):
    if n == 1:
        return 0
    opCount = 0
    result = b
    for i in range(e - 1):
        result = (result * b) % n
        opCount += 1
    print("opcount = " + str(opCount))
    return result


# print(expo_modulaire(1048576, 4, 497))


##Q4
# retourne la representation de n en base 2, poids faible a gauche
def int_to_bin(n):
    result = str(bin(n))
    result = result[2:len(result)]
    return result[::-1]


##retourne (b**e) % n
##ne manipule que des entiers <= b*b-b
## O(log(e)) operations
def expo_modulaire_rapide(e, b, n):
    ebin = int_to_bin(e)
    print(ebin)
    opCount = 0
    result = 1
    b = b % n
    for i in ebin:
        if i == '1':
            result = (result * b) % n
            opCount += 1
        b = (b * b) % n
        opCount += 1
    print("opcount = " + str(opCount))
    return result


#print(expo_modulaire_rapide(17, 4, 497))


###tests de primalite###

# retourne True ssi x est premier
def is_prime_naive(x):
    if x <= 1:
        return False
    for i in range(2,int(x/2)):
        if x % i == 0:
            return False
    return True

#print(is_prime_naive(13))

# retourne un entier premier, aleatoire, uniforme sur [a , a+delta]
def generate_prime(a, delta):
    r = random.randint(a, a+delta)
    i=0
    while is_prime_naive(r) == False:
        if i > 100000:
            raise Exception('After 100000 iterations no prime was found in the given intervall [{},{}]\nPlease retry with a new intervall'.format(a,a+delta))
        r = random.randint(a, a+delta)
        i+=1
    return r

#print(generate_prime(9,1))


# retourne un entier premier avec n, aleatoire, uniforme sur [2, n-1]
def prime_with(n):
    return 2


##Q5
# retourne la liste des nombres premiers <= n
# methode du crible d Eratosthene
def crible_eras(n):
    primes = []  
    numbers = list(range(2, n+1)) 
    c = 2           
    while c * c < n: 
        for k in range(c, (n+1), c): 
            if k in numbers:              
                numbers.remove(k)         
        primes.append(c)             
        c = numbers[0]                    
    return primes + numbers          

#print(crible_eras(25))

# retourne True ssi n est premier;methode du crible
def is_prime_eras(n):
    if n in crible_eras(n):
        return True
    return False


##Q6

# returne True si n est pseudo-premier pour le temoin a
def temoin_fermat(a, n):
    return True


# n entier a tester, t nombre de tests
def test_fermat(n, t):
    return True


##Q7
# returns r,u such that 2^r * u = n and u is odd
def find_ru(n):
    return 1, 1


##Q8
# n entier
# a entier dans [1,n-2]
# pgcd(a,n)=1
# retourne True , si a est un temoin de Rabin de non-primalite de n
def temoin_rabin(a, n):
    return True


# n entier a tester, t nombre de tests
# retourne True , si n est premier
# retourne False , avec proba > 1-(1/4)**t, si n est compose
def test_rabin(n, t):
    return True


##Q9
# retourne un nombre probablement premier de n bits
def gen_prime(n):
    return 2


##print(gen_prime(2048))

# retourne un triplet e,d,N avec
# N = pq, p,q premier de n bits
# ed = 1 mod phi(N)
def gen_rsa(n):
    return 1, 1, 2


##Q10
# pk = (e,N)
# m entier; retourne un entier
def enc_rsa(m, pk):
    return 1


# sk = (d,N)
# c entier; retourne un entier
def dec_rsa(c, sk):
    return 1


##Q11
##traductions: chaines --> entiers puis entiers--> chaines
##en base 256
##poids faibles a gauche
def str_to_int(m):
    s = 0
    b = 1
    for i in range(len(m)):
        s = s + ord(m[i]) * b
        b = b * 256
    return s


def int_to_str(c):
    s = ""
    q, r = divmod(c, 256)
    s = s + str(chr(r))
    while q != 0:
        q, r = divmod(q, 256)
        s = s + str(chr(r))
    return s


# m est une chaine
# retourne un entier
def Enc_rsa(pk, m):
    return enc_rsa(str_to_int(m), pk)


# c est un entier
# retourne une chaine
def Dec_rsa(sk, c):
    return int_to_str(dec_rsa(c, sk))


##Q12
# cle de longueur 512 bits
# chiffrer: "ceci est le message de la question 12"


#################################################################
##Q13## small N de l enonce 
c = 203167233604391
e = 105153818938879
n = 204274274459681
# print("Q13 enonce solution", m)

##Q14## n1,n2 have common factor
e_1 = 3910690008818283670868637293583807472406071014855467369376562453386568115118575549998307514095977446821904723128834716386012345019774749462224705453754125884105038313503535027306620172125186316567937615638323556850956880936518300302602805131676135113108484963880039142798231895843109891553380806740147280757
n_1 = 69062688172064155658911250623824437247555723148603353738302253474984234478451724017342927200711212198561324986531605253193903441692089256620618833106961546429636445891984627695781384630013598341331689939178245781706540076751973610738227963889376714904403031694051296788833443496526885726775528827375948071929
c_1 = 24611251859812674169475796819303494911673745448473749394264526728162562685914074480537612941297670059801437381400024027253730653656476905281069179513708218469741624630326718738842101073851660606585444810976721216050363222115416379071737436541444450899126931955382088463221366246065910447241755253937828596484
e_2 = 50397573445568763030099703004373898485585249797981757548804415428108299083942229312259373614894595903577758246150442182256560679304788412233292957789570033238043365999611082606264134175517480208252580509041639010254535825802825318897321850834897940554139541328154602147460933321382694123780993639943682579161
n_2 = 133996121506180462100555893114601434003049417003992050068931466928433702114247562694298268069726711436045516534210904716141897493553167880291439666527456807577995348332438299166875918790184716514217950877638447810365245678429514775529856742797659000032921952599049570889869462864202149565613900963189237850671
pk_1 = [e_1, n_1]
pk_2 = [e_2, n_2]
# print("Q14 enonce solution m1:", m1)
# print("Q14 enonce solution m2:", m2)

##Q15## same-small e
e_345 = 3
n_3 = 209972710381843986019222724306085916069
c_3 = 98607549210059445213327744289011210961
n_4 = 205189342117195706999905843901134883221
c_4 = 132884908601266001427764987011290838595
n_5 = 153796631843893344041809725352383124009
c_5 = 143095419972589988082906041499952513358
pk_3 = [e_345, n_3]
pk_4 = [e_345, n_4]
pk_5 = [e_345, n_5]
# print("Q15 enonce solution m:", m)

##Q16## same N=N6=N7 and pair (e7,d7) is known
pk_6 = [
    335005463960816278593867316896417983166152916344794573850343153194217911312049872711136325234993418003668720236803986830311580268508550980361654685346311,
    5091051477963388231001637916796944302688369871753703137277176206069939465618876740391747924500711710028638413264341759139522270049313860235633263862054043]
c_6 = 4145467078845472644712994806773571070731259201297400785818159271701026566350697311159454042538512643215451570946380981445723923315865474776196912541298967
pk_7 = [
    3880522386929786816439757650057726253188135798562155960090443809425982789187841739707198985802185440418350010118211685642720469665257056875247463135661403,
    5091051477963388231001637916796944302688369871753703137277176206069939465618876740391747924500711710028638413264341759139522270049313860235633263862054043]
sk_7 = [
    2270270259341137360152942794271619370360758459724185928285877626378514257525937090103380531321958458730253721937068263828249543225253424826884975859409347,
    5091051477963388231001637916796944302688369871753703137277176206069939465618876740391747924500711710028638413264341759139522270049313860235633263862054043]
# print("Q16 enonce solution m6:", m6)
