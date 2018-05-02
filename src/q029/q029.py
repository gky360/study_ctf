# -*- coding: utf-8 -*-

E1 = 11
N = 236934049743116267137999082243372631809789567482083918717832642810097363305512293474568071369055296264199854438630820352634325357252399203160052660683745421710174826323192475870497319105418435646820494864987787286941817224659073497212768480618387152477878449603008187097148599534206055318807657902493850180695091646575878916531742076951110529004783428260456713315007812112632429296257313525506207087475539303737022587194108436132757979273391594299137176227924904126161234005321583720836733205639052615538054399452669637400105028428545751844036229657412844469034970807562336527158965779903175305550570647732255961850364080642984562893392375273054434538280546913977098212083374336482279710348958536764229803743404325258229707314844255917497531735251105389366176228741806064378293682890877558325834873371615135474627913981994123692172918524625407966731238257519603614744577
C1 = 80265690974140286785447882525076768851800986505783169077080797677035805215248640465159446426193422263912423067392651719120282968933314718780685629466284745121303594495759721471318134122366715904

E2 = 13
C2 = 14451037575679461333658489727928902053807202350950440400755535465672646289383249206721118279217195146247129636809289035793102103248547070620691905918862697416910065303500798664102685376006097589955370023822867897020714767877873664


def gcd(a, b):
    """Calculate greatest common divider of a and b."""
    if b == 0:
        return a
    return gcd(b, a % b)


def extgcd(a, b):
    """Find x and y such that `ax + by = gcd(a, b)` ."""
    if b == 0:
        return 1, 0
    y, x = extgcd(b, a % b)
    y -= (a // b) * x
    return x, y


def modinv(a, m):
    """Calculate `a^{-1}` ."""
    x, _ = extgcd(a, m)
    return x % m


def pow_m(a, n, m):
    """Calculate `(a^n) % m` with O(log n) time complexity."""
    ret = 1
    if n < 0:
        n = -n
        a = modinv(a, m)
    p = a % m
    while n > 0:
        if n & 1:
            ret *= p
            ret %= m
        p *= p
        p %= m
        n >>= 1
    return ret % m


s1, s2 = extgcd(E1, E2)

m = pow_m(C1, s1, N) * pow_m(C2, s2, N) % N

print(m)
