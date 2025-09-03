def client():
    """Cette fonction permet d'avoir une idée sur le client."""
    genre = input("La serveuse voit : ").strip().lower()

    if genre in ["dame", "monsieur"]:
        prenom = input(
            f"Bonjour joli {genre}, comment vous appelez-vous ? ").strip()
        if prenom:
            print(f"{prenom}, bienvenue dans notre café.")
            return True   # ✅ client valide
        else:
            print("Veuillez saisir un prénom.")
            return False
    else:
        print("Veuillez saisir 'dame' ou 'monsieur', merci.")
        return False


def commande():
    """Cette fonction permet au client de passer commande."""
    commander = input("Que voulez-vous commander ?: ").strip().lower()
    if commander:
        print(f"Votre {commander} sera bientôt prêt.\n")
    else:
        print("Veuillez saisir ce que vous voulez manger.")


def menu_principal():
    """Cette fonction permet d'utiliser les fonctions précédentes en une seule fois."""
    try:
        if client():   # ✅ seulement si client() est valide
            commande()
    except ValueError:
        print("Veuillez saisir des valeurs correctes.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


# Le programme démarre ici.

if __name__ == '__main__':
    menu_principal()
