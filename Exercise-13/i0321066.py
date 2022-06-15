# import matrik
from matrik import buatmatrik


#def buatmatrik(nilaiseed=66, row=7, col=9):
   # "membuat matrik"
    #import random
    # MA = [0] * row
    # random.seed(nilaiseed)
    # for baris in range(row):
        # MA[baris] = [0] * col
        # for j in range(col):
            # MA[baris][j] = random.randrange(1,100)
    # return MA
def main():
    print(buatmatrik(nilaiseed=2021, row=7, col=9))
    matrik1=buatmatrik(2021, 7, 9)
    matrik2=buatmatrik(nilaiseed=66,row=7,col=9)
    print(matrik1)
    print(matrik2)
    return
if __name__=="__main__":
    main()