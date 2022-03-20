from LQ import*
from listor import*
from molgrafik import*
from atom2 import*

atomlista = skapaatomlista()
tabell = lagraHashtabell(atomlista)

class Syntaxerror(Exception):
    pass

def delaupp(ordet):
    w=list(ordet)
    q=LinkedQ()
    for z in w:
        q.enqueue(z)
    q.enqueue("\n")
    return q

def readformel(q):
    mol = readmol(q)
    empty = q.isEmpty()
    if empty is False:
        nästa=q.peek()
        if nästa=="\n":
            return mol
        elif nästa == ")":
            mol=readmol(q)
        else:
            return mol

def readmol(q):
    mol=readgroup(q)
    nästa=q.peek()
    if nästa == "\n" or nästa == ")":
        return mol
    else:
        mol.next=readmol(q)
        return mol


def readgroup(q):
    ruta = Ruta()
    ftecken=q.peek()
    if ftecken =="(":
        q.dequeue()
        ruta.down = readmol(q)
        atecken=q.peek()
        if atecken!=")":
            f=write(q)
            raise Syntaxerror("Saknad högerparantes vid radslutet "+f)
        if atecken==")":
            q.dequeue()
            tredje=q.peek()
            if num(tredje) is True:
                ruta.num=readnum(q)
                return ruta
            else:
                f=write(q)
                raise Syntaxerror("Saknad siffra vid radslutet "+f)
    else:
        ruta.atom=readatom(q)
    ny=q.peek()
    if num(ny) is True:
        ruta.num=readnum(q)
    return ruta

def readatom(q):
    fbok=q.peek()
    if StorB(fbok) is True:
        q.dequeue()
        empty=q.isEmpty()
        if empty is False and LitenB(q.peek()) is True:
            abok=q.dequeue()
            fbok+=abok
    elif LitenB(fbok) is True:
        f=write(q)
        raise Syntaxerror("Saknad stor bokstav vid radslutet "+f)
    else:
        f=write(q)
        raise Syntaxerror("Felaktig gruppstart vid radslutet "+f)
    if fbok in Atomerlista:
        return fbok
    else:
        f=write(q)
        raise Syntaxerror("Okänd atom vid radslutet "+f)

def readnum(q):
    numlista = ""
    fsiffra=q.peek()
    if num(fsiffra) is True:
        if fsiffra in siffror:
            if fsiffra== siffror[0]:
                q.dequeue()
                f=write(q)
                raise Syntaxerror("För litet tal vid radslutet "+f)
            if fsiffra == siffror[1]:
                q.dequeue()
                asiffra=q.peek()
                if num(asiffra) is True:
                    tal=fsiffra+asiffra
                else:
                    f=write(q)
                    raise Syntaxerror("För litet tal vid radslutet "+f)
        while num(q.peek()) is True:
            numlista += q.dequeue()
        return int(numlista)

def Weight(ruta):
    if ruta != None:
        if ruta.down is None:
            vikt = ruta.num * tabell.get(ruta.atom).vikt
        else:
            vikt = (ruta.num * Weight(ruta.down))
        total= vikt+Weight(ruta.next)
        return total
    else:
        return 0

def write(q):
    str1=""
    while q.isEmpty() is False:
        x=q.dequeue()
        if x == "\n":
            break
        else:
            str1=str1+x
    return str1

def StorB(bokstav):
    if bokstav in storaA:
        return True
    else:
        return False
def LitenB(bokstav):
    if bokstav in lillaA:
        return True
    else:
        return False
def num(x):
    if x in siffror:
        return True
    else:
        return False

def main():
    while True:
        molekyl = input("Molekyl: ")
        if '#' in molekyl:
            return False
        else:
            try:
                x=Molgrafik()
                syntax=delaupp(molekyl)
                mol=readformel(syntax)
                vikt=Weight(mol)
                print("Vikten är:", vikt ,"mol")
                x.show(mol)
            except Syntaxerror as fel:
                return str(fel)

main()