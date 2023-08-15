# %% import
import pandas as pd
# %% convert
def convert(fi):
    # romaji extraction and conversion
    fo=[]
    for k in range(len(fi)):
        buff=fi[k]
        o=''
        l=len(buff)
        i=0
        while(i<l):
            roma=buff[i]
            roma2=roma+(buff[i+1] if i+1<l else ' ')
            roma3=roma2+(buff[i+2] if i+2<l else ' ')
            if(df[df.romaji==roma3].empty):
                if(roma in ('a', 'i', 'u', 'e', 'o')):
                    romaf=roma
                    i+=1
                elif(roma2[0]==roma2[1]):
                    if(roma=='n'):
                        romaf=roma
                    else:
                        romaf='smalltsu'
                    i+=1
                elif(roma=='n' and roma2[1] not in ('a', 'i', 'u', 'e', 'o')):
                    romaf=roma
                    i+=1
                else:
                    romaf=roma2
                    i+=2
            else:
                romaf=roma3
                i+=3
            kana=df[df.romaji==romaf].kana.tolist()[0] #conversion
            o+=kana
        fo.append(o)
    return fo
# %% dataframe creation
df=pd.read_csv("hiragana.csv")
# %% read the input file
path=input("Enter the location of the file to transliterate\n")
f=open(r"{}".format(path), 'r')
print("Reading your file...")
parse=f.read()
f.close()
print("Done.")
# %% extract target text
lim=input("Enter the delimiter wrapping the romaji\n")
print("Extracting romaji texts...")
fi=[]
j=0
while(j<len(parse)):
    pos=parse.find(lim, j)
    if(pos==-1):
        if len(fi)==0:
            print("no delimiter occurrence found\n")
        break
    else:
        j=pos+1
        pos2=parse.find(lim, j)
        if(pos2==-1):
            print("odd number of delimiter occurrences found\n")
            break
        j=pos2+1
        fi.append(parse[pos+1:pos2])
print("Done.")
if len(fi)!=0:
    print("Converting romaji to hiragana...")
    fo=convert(fi)
    # produce output
    print("Creating the output text...")
    for i in range(len(fi)):
        parse=parse.replace(fi[i], fo[i])
        parse=parse.replace(lim,'')
        parse=parse.replace(lim,'')
    # write output to a file
    path=input("Enter output file path, where the file, if not already existing, will be created\n")
    f=open(r"{}".format(path), 'w')
    print("Writing to your output file.")
    f.write(parse)
    f.close()
    print("Done.")