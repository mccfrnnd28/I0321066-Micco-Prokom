def buatmatrik(nilaiseed=66, row=7, col=9):
    "membuat matrik"
    import random
    MA = [0] * row
    random.seed(nilaiseed)
    for baris in range(row):
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1,100)
    return MA

def main():
    return

if __name__=="__main__":
    main()    