import hashlib


frase = input('Digite a frase: ')
chavesha256fei = input('Digite a chave SHA256: ')
chaveMD5fei = input('Digite a chave MD5: ')


h = hashlib.sha256()
h.update(frase.encode('utf-8'))
chavesha256gerada = (h.hexdigest())

a = hashlib.md5()
a.update(frase.encode('utf-8'))
chaveMD5gerada = (a.hexdigest())

if (chavesha256fei==chavesha256gerada):
  if (chaveMD5fei==chaveMD5gerada):
    print ('SHA256 e MD5 corretos')
  else:
    print ('Somente SHA256 correto')
elif (chaveMD5fei==chaveMD5gerada):
  print ('Somente MD5 correto')
else:
  print ('Nenhum dos dois corretos')