# Copyright (c) 2024 by
# MICHO NGABO Daniel;
# MUSHAGALUSA MURHULA Ines;
# KAZINGUFU ZABILO Marcelin;
# MULAMBA TAMBWE Gregory et
# OMBA JOEL Joel


import hashlib

def hachage (message: str) -> str:
    # Converssion du message en bytes
    message = message.encode('utf-8')
    
    # hachage du message avec SHA-256
    hashage = hashlib.sha256(message)

    # recuperation de la valeur de hachage
    value_hash = hashage.hexdigest()

    return value_hash

while True:
    mes = input('Entrez le message à hacher svp exit pour exit pour quitter: ')

    if mes == 'exit':
        break
    else: 
        print(hachage(mes))