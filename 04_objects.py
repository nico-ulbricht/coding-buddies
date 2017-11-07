# QUELLE
dictionaryGermanToSpanish = {
	'hallo': 'hola'
}

dictionaryGermanToEnglish = {
	'hallo': 'hello'
}

dictionaryGermanToKorean = {
	'hallo': '안녕하세요'
}


# CODE
languageToDictionary = {
	'english': dictionaryGermanToEnglish,
	'spanish': dictionaryGermanToSpanish,
	'korean': dictionaryGermanToKorean
}

whichLanguage = input('Which language to translate to? ')
whichLanguage = whichLanguage.lower()
dictionaryToUse = languageToDictionary[whichLanguage]

whichWord = input('Which word to translate? ')
print(dictionaryToUse[whichWord])
