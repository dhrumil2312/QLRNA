import csv

import QLRNA
import pandas as pd
dp = '...................((((((((....))))))))..............................(((((.....)))))(((((((((((((((((....)))))))))))))))).).....(((((...........((((((((((((((((((...))))))))((((((((......))))))))(((((((((....))))))))))))))))))).........)))..))'
# print(dp)
seq = QLRNA.qlrna(dp)
print(seq)
f = open("structures.txt")
count = 0
failed = 0

failedStructures = list()
successStruct = list()
seqList = list()

# fileWriter = open("output.csv", "wb")
# csvWriter = csv.writer(fileWriter, delimiter = ",", quotechar = "|", quoting = csv.QUOTE_MINIMAL)


for line in f.readlines():
    for struct in line.split(","):
        struct = struct.strip()
        try:
            seq = QLRNA.qlrna(struct)
        except:
            seq = "Structure not valid"
            print("Error!!!!!!!!!!!!!!!!" , struct )

        if seq.startswith("Structure") or len(seq) == 0:
            failed += 1
        else:
            count+=1
            successStruct.append(struct)
            seqList.append(seq)

            print(count, struct, seq , failed)


dataFrameData = {"structure": successStruct, "sequence": seqList}
df = pd.DataFrame(dataFrameData)
df.to_excel("mainData.xlsx")
print(failed)
print(failedStructures)