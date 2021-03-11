print("Please Input Query. First Letter Of Amino Acids Must Be Capitalized\n")
while 1==1:
  
  
  Q = input(">")
  if Q == "Phe":
    print("UUU/UUC")
  elif Q == "Leu":
    print("UUA/UUG/CUU/CUC/CUA/CUG")
  elif Q == "Ile":
    print("AUU/AUC/AUA")
  elif Q == "Val":
    print("GUU/GUC/GUA/GUG")
  elif Q == "Ser":
    print("UCU/UCC/UCA/UCG")
  elif Q == "Pro":
    print("CCU/CCC/CCA/CCG")
  elif Q == "Thr":
    print("ACU/ACC/ACA/ACG")
  elif Q == "Ala":
    print("GCU/GCC/GCA/GCG")
  elif Q == "Tyr":
    print("UAU/UAC")
  elif Q == "Stop":
    print("UAA/UAG/UGA")
  elif Q == "stop":
    print("UAA/UAG/UGA")
  elif Q == "His":
    print("CAU/CAC")
  elif Q == "Gln":
    print("CAA/CAG")
  elif Q == "Asn":
    print("AAU/AAC/AAA")
  elif Q == "Lys":
    print("AAA/AAG")
  elif Q == "Asp":
    print("GAU/GAC")
  elif Q == "Glu":
    print("GAA/GAG")
  elif Q == "Cys":
    print("UGU/UGC")
  elif Q == "Trp":
    print("UGG")
  elif Q == "Arg":
    print("CGU/CGC/CGA/CGG")
  elif Q == "Ser":
    print("AGU/AGC/AGA/AGG")
  elif Q == "Gly":
    print("GGU/GGC/GGA/GGG")
  elif Q == "Start":
    print("AUG")
  else:
    print("No Results Found For Your Search. Please Try Again.")