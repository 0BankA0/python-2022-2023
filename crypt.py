from cryptography.fernet import Fernet

atslega = Fernet.generate_key()
print (atslega)

tekst= b'Slepenie dati'

sifDati = a.encrypt(tekst)
print(sifDati)

print(a.decrypt(sifDati))