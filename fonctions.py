class Exercices:
    def __init__(self):
        pass

    """
        EXERCICE 1 : Afficher votre nom complet sur l’écran 5 fois.
    """
    def nom_sur_ecran(self, n):
       i = 0
       while i < 5:
           print("Doine Jacquenson")
           i = i + 1
       print("\n=================Thanks1====================\n")
    """ 
        EXERCICE 2 : Afficher votre nom complet, votre rue-et-numéro, votre ville, 
            votre pays, votre courriel ; chaque information sur 
    """
    def demographie(self):
        name = "Jacquenson Doine\n" ; rue_numero = "La Tremblay 10\n"; ville = "Croix des bouquets\n"; pays = "Haiti\n"; courriel = "doinejacquenson@gmail.com\n"
        print(name, rue_numero, ville, pays, courriel)
        print("\n=================Thanks2====================\n")



    """
        EXERCICE 3 :  Utiliser une boucle pour afficher un rectangle sur l’écran avec des étoiles (20 par 5)
    """
    def rectangle_etoiles(self, longeur, largeur):
        for longuer in range(0, 5):
            print(" ")
            for largeur in range(0, 20):
                print("*", end="")

        print("\n=================Thanks3====================\n")

    """
        EXERCICE 4 : Utiliser une boucle pour afficher un triangle sur l’écran comme suit:
        *
        ***
        *****
        *******
        *********
        ***********
        *************
    """
    def triangle1(self):
       for i in range(1, 7):
           print("*")
           for j in range(i):
                print("*", end="*")
       print("*")
       print("\n=================Thanks4====================\n")



    """
        EXERCICE 5 :  Utiliser une boucle pour afficher un triangle sur l’écran, chaque ligne contient un nombre impair
        d’étoiles: 1, 5, 9, 13, 17, 21, 25
        *
        ** ** *
        ** ** ** ** *
        ** ** ** ** ** ** *
        ** ** ** ** ** ** ** ** *
        ** ** ** ** ** ** ** ** ** ** *
        ** ** ** ** ** ** ** ** ** ** ** ** *
    """
    def triangle2(self):
        for i in range(7):
            print("*")
            for j in range(i, i+i+i+2):
                print("**", end=" ")

        print("\n=================Thanks5====================\n")

    """
        EXERCICE 6 : Écrivez un programme qui affiche les n premiers termes de la table 
        de multiplication par Nombre. 
    """
    def table_multiplication_par_7(self, n, Nombre):
       n = 7
       print("Voici la table de multiplication de", n)
       for Nombre in range(0, 20):
           print(Nombre, "* ", n, " = ", Nombre * n, end=" \n")
           Nombre = Nombre + 1

       print("\n=================Thanks6====================\n")

    """
        EXERCICE 7 : Écrivez un programme qui affiche une table de conversion de sommes 
        d’argent exprimées en euros, en dollars canadiens. La progression des sommes de la table sera « géométrique », comme dans l’exemple ci-dessous : 1 euro(s) = 1.65 dollar(s) 2 euro(s) = 3.30 dollar(s) 4 euro(s) = 6.60 dollar(s) 8 euro(s) = 13.20 dollar(s) etc. (S’arrêter à 16384 euros.)  
    """
    def conversion(self):
        a = 1
        while a <= 16384:
            print(a, "euros = ", a*1.65, "dollars")
            a=a*2
        print("\n=================Thanks7====================\n")

    """
        EXERCICE 8 : Écrivez un programme qui affiche une suite de 12 nombres 
        en commençant par le nombre N dont chaque terme soit égal au triple du 
        terme précédent.  
    """

    def tripple(self, N):
        n = 1
        nbre1= n * 3
        while n <= 12:
            nbre1 *= 3
            print(nbre1)
            n += 1
        print("\n=================Thanks8====================\n")