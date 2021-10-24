import requests
class FlajoletMartin:
    def __init__(self,hash,hashes):
        #self.dataStream = dataStream
        self.hash = hash
        self.hashes = hashes
        self.groupSize = int(input('enter the grouping size\n'))
        self.startStream()
    def convertImg2listOfpixels(self,image):
        l = [x for x in image]
        return l
    def startStream(self):
        url = input('enter the url to get video stream:- \n')
        while True:
            try:
                image = requests.get(url)
                image = self.convertImg2listOfpixels(image.content)
                self.dataStream = image
                self.runFMAlgorithm()
                self.extendedFMAlgorithm()
                self.extendedFMAlgorithmMedian()
                self.combineApproach()
            except KeyboardInterrupt:
                break
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
        print('\n*****NORMAL FM ALGORITHM*****')
        print('r = ',r)
        print('R(number of distinct elements) =',2**r)

    def extendedFMAlgorithm(self):
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
        print('\n*****EXTENDED FM ALGORITHM with Average of all r`s*****')
        print('avg r =',r)
        print('R(number of distinct elements) =',2**r)

    def extendedFMAlgorithmMedian(self):
        r = self.median(self.allHashTrailZeros)
        print('\n*****EXTENDED FM ALGORITHM with median of all r`s*****')
        print('median r =',r)
        if int(2**r) == 2**r:
            print('R(number of distinct elements) =',2**r)
        else:
            print('R(number of distinct elements) =',2**r,'(~= '+str(int(2**r)+1)+')')

    def combineApproach(self):
        if len(self.hashes) < 4:
            print('\n*****combine approach is not possible due to less no of hashes. we wont be able to group them.*****')
            return
        i = 0
        newAr = []
        while i< len(self.allHashTrailZeros):
            avg = self.average(self.allHashTrailZeros[i:i+self.groupSize])
            newAr.append(avg)
            i += self.groupSize

        r = self.median(newAr)
        print('\n*****COMBINE APPROACH with making groups of size '+str(self.groupSize)+' and taking avg of each group and finally taking the median of all avg`s.*****')
        print('combined r =',r)
        print('R(number of distinct elements) =',2**r)

#x = input('enter the data stream\n').strip().split()
#x = [int(m) for m in x]
print('hash format = (ax+b)%c')
hashes = []
no_of_hash = int(input('enter the number of hash you require?\n'))
for i in range(no_of_hash):
    if i+1 == 1:
        tmp = input('enter the '+str(i+1)+'st hash coefficients\n' ).strip().split()
        abc = []
        abc.extend(tmp)
    elif i+1 == 2:
        tmp = input('enter the '+str(i+1)+'nd hash coefficients\n' ).strip().split()
    elif i+1 == 3:
        tmp = input('enter the '+str(i+1)+'rd hash coefficients\n' ).strip().split()
    else:
        tmp = input('enter the '+str(i+1)+'th hash coefficients\n' ).strip().split()
    tmp = [int(m) for m in tmp]
    hashes.append(tmp)

#abc = input().strip().split()
object = FlajoletMartin(abc,hashes)
#object.runFMAlgorithm()
#object.extendedFMAlgorithm()
#object.extendedFMAlgorithmMedian()
#object.combineApproach()
