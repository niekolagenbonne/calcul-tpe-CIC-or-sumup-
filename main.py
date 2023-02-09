#ce code calcul selon ton salaire ce qui est le plus rentable de prendre comme tpe
def salaire_de_la_personne():
    salaire_int = 0 
    while salaire_int == 0:
        salaire_str = input("Quel est votre salaire par mois ? ")
        try:
            salaire_int = int(salaire_str)
        except:
            print("Desolé il faut rentrer un nombre")
        
    nb_mois_int = None
    while nb_mois_int == None:
        nb_mois_str = input("Combien de mois vous voulez essayer l'abonnement de CIC? ")
        try:
            nb_mois_int = int(nb_mois_str)
        except:
            print("Desolé il faut rentrer un nombre")
    total_par_mois = salaire_int * nb_mois_int
    frais_sumup = total_par_mois * (1.75/100)
    salaire_moins_frais_sumup = total_par_mois - frais_sumup
    print("-----------------------------------------------------------")
    print("Votre salaire avec les frais de sumup est de: " + str(salaire_moins_frais_sumup) + "€")
    prix_lecteur = 16
    salaire_frais_sumup_moins_prix_lecteur = salaire_moins_frais_sumup - prix_lecteur
    if salaire_frais_sumup_moins_prix_lecteur < 0:
        print("vous allez perdre: " + str(salaire_frais_sumup_moins_prix_lecteur) + "€ avec les frais de Sumup")
    else:
        print("Votre salaire moins le prix du lecteur cb Sumup et avec les frais est de: " + str(salaire_frais_sumup_moins_prix_lecteur) + "€")
    prix_tpe_cic = 21
    salaire_moins_prix_mois_cic = total_par_mois - (prix_tpe_cic * nb_mois_int)
    if salaire_moins_prix_mois_cic < 0:
        print("Vous allez perdre :" + str(salaire_moins_prix_mois_cic) + "€ avec l'abonnement de CIC")
    else:
        print("Votre salaire avec l'abonnement CIC est de: " + str(salaire_moins_prix_mois_cic) + "€")
    
    if salaire_frais_sumup_moins_prix_lecteur > salaire_moins_prix_mois_cic:
        print("il est plus rentable de choisir Sumup que le TPE de CIC")
    else:
        print("il est plus rentable de choisir le TPE de CIC que Sumup")
    print("-----------------------------------------------------------")
    
salaire_de_la_personne()



