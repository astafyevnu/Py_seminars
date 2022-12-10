spis = ['дерево', 'мир', 'земля', 'губернаторство', 'убрава',
'жеребьёвка', 'заботливость', 'меблировка', 'набивка', 'рабство']
inp = set(input('Введите строку с символами: ').lower())
print(spis, [new_spis for new_spis in spis if not inp.issubset(
set(new_spis.lower()))], sep='\n')