class FlajoletMartin:
    def __init__(self,dataStream,hash):
        self.dataStream = dataStream
        self.hash = hash
    def average(self,lists):
        s = sum(lists)
        return int(s/len(lists))
    def median(self,lists):
        x = []
        x.extend(lists)
        x.sort()
        if len(x)%2:
            return x[(len(x)-1)//2]
        return (x[(len(x)-1)//2]  + x[(len(x)-1)//2+1]  )/2.0
    def intToBin(self,val):
        bin = []
        while val > 0:
            bin.append(val%2)
            val = int(val/2)
        return bin
    def getTrailingZeros(self,bin):
        t = 0
        for i in bin:
            if i != 0:
                return t
            t += 1
        return t
    def runFMAlgorithm(self):
        a = int(self.hash[0])
        b = int(self.hash[1])
        c = int(self.hash[2])
        self.trailingZeros = []
        for i in self.dataStream:
            v = (a*i+b)%c
            s = self.intToBin(v)
            n = self.getTrailingZeros(s)
            self.trailingZeros.append(n)
        r = max(self.trailingZeros)
        print('*****NORMAL FM ALGORITHM*****\n')
        print('r = ',r)
        print('R(number of distinct elements) =',2**r)

    def extendedFMAlgorithm(self):
        self.hashes = []
        tmp = [int(m) for m in self.hash]
        self.hashes.append(tmp)
        self.no_of_hash = int(input('enter the number of hash you require?\n'))
        for i in range(1,self.no_of_hash):
            if i+1 == 2:
                tmp = input('enter the '+str(i+1)+'nd hash coefficients\n' ).strip().split()
            elif i+1 == 3:
                tmp = input('enter the '+str(i+1)+'rd hash coefficients\n' ).strip().split()
            else:
                tmp = input('enter the '+str(i+1)+'th hash coefficients\n' ).strip().split()
            tmp = [int(m) for m in tmp]
            self.hashes.append(tmp)
        self.allHashTrailZeros = []
        for i in self.hashes:
            a = i[0]
            b = i[1]
            c = i[2]
            self.trailingZeros = []
            for j in self.dataStream:
                v = (a*j+b)%c
                s = self.intToBin(v)
                n = self.getTrailingZeros(s)
                self.trailingZeros.append(n)
            self.allHashTrailZeros.append(max(self.trailingZeros))
        r = self.average(self.allHashTrailZeros)
        print('*****EXTENDED FM ALGORITHM with Average of all r`s*****\n')
        print('avg r =',r)
        print('R(number of distinct elements) =',2**r)

    def extendedFMAlgorithmMedian(self):
        r = self.median(self.allHashTrailZeros)
        print('*****EXTENDED FM ALGORITHM with median of all r`s*****\n')
        print('median r =',r)
        print('R(number of distinct elements) =',2**r,'(~ =)',int(2**r)+1)

    def combineApproach(self):
        if len(self.hashes) < 4:
            print('combine approach is not possible due to less no of hashes. we wont be able to group them.')
            return
        self.groupSize = int(input('enter the grouping size\n'))
        i = 0
        newAr = []
        while i< len(self.allHashTrailZeros):
            avg = self.average(self.allHashTrailZeros[i:i+self.groupSize])
            newAr.append(avg)
            i += self.groupSize

        r = self.median(newAr)
        print('combined r =',r)
        print('R =',2**r)




x = input('enter the data stream\n').strip().split()
x = [int(m) for m in x]
print('hash format = (ax+b)%c')
print('enter a, b and c space seperated in the next line')
abc = input().strip().split()
object = FlajoletMartin(x,abc)
object.runFMAlgorithm()
object.extendedFMAlgorithm()
object.extendedFMAlgorithmMedian()
object.combineApproach()
