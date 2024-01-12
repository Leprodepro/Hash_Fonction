# Fait par un groupe d'étudiant en Math-info de la faculté de sciences à de l'UNIKIN :
#     MICHO NGABO Daniel
#     MUSHAGALUSA MURHULA Ines
#     KAZINGUFU ZABILO Marcelin
#     MULAMBA TAMBWE Gregory
#     OMBA JOEL Joel
# 
# Dans le cadre d'un travail pratique de criptographie
# Où il nous est démande d'implementater une fonction de hachage remplissant le critère ci-après :
#    - Déterministe : La fonction est déterministe , c’est-à-dire qu’une même entrée aura toujours
#      la même valeur de hachage.
#    - Fonction à sens unique : Il ne doit pas être possible de générer le contenu original à 
#      partir de la valeur de hachage.
#    - Sécurité contre les collisions : La même valeur de hachage ne doit pas être attribuée
#      aux différents textes. En d’autres termes, pour chaque entrée différente, le résultat doit
#      être différent.
#    - La rapidité : La procédure de calcul de la valeur de hachage doit être rapide.
#    - Resistance : Doit être résistante à la falsification (la moindre modification du message
#      aboutit à un résultat totalement différent)
#    - une valeur de hashage à longeur fixe avec cette forme "ab557953e6057cbeddc3"
# 
# Après avoir fait des recherche nous avons conclus que nous implementerons la fonction SHA-256
# bien qu'il y a des fonction plus performante nous choissons celle- ci car elle remplie le mieux
# toutes les contraintes citées ci-haut surtout celles de la rapididité.
