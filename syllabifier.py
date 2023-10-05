#Phones: a b c d̪ e f i j k l m n o p r s tʃ t̪ u w x ç ð ŋ ɟ ɟʝ ɡ ɣ ɲ ɾ ʃ ʎ ʝ β θ

def syllabify(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    syllables = []
    start = 0
    for c in range(len(word)):
        if word[c] in vowels:
            #check next character
            if c + 1 < len(word):
                
                #VV - split in between
                if word[c + 1] in vowels:
                    syllables.append(word[start:c + 1])
                    start = c + 1
                    
                #check character immediately after consonant
                elif c + 2 < len(word):
                    affricate = False
                    
                    ## treat multi-character ipa symbols as one symbol not 2
                    if (word[c+1] == 't' and word[c+2] == 'ʃ') or (word[c+1] == 'ɟ' and word[c+2] == 'ʝ'):
                            c += 1
                            affricate = True
                            
                    if word[c + 2] in vowels:
                        #VCV - split after first V
                        if affricate:
                            syllables.append(word[start:c])
                            start = c
                        else:
                            syllables.append(word[start:c+1])
                            start = c + 1
                        
                    else:
                        #VCC - split between two Cs
                        syllables.append(word[start:c+2])
                        start = c + 2
                        
                else: 
                    #word ends after consonant
                    syllables.append(word[start:c+2])
                    
            else:
                #word ends after vowel
                syllables.append(word[start:c+1])
                
    syllables = [x.split() for x in syllables]
    print(syllables)
