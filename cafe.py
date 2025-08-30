def client():
    """Cette fonction permet d'avoir une idée sur le client."""
    genre = input(f'Que voit la serveuse ? ')
    print(f'La serveuse voit un(e) {genre}\n')
    if genre == 'dame':
        nom_client = input(
            f'Bonjour joli {genre}, comment vous appelez-vous ? ')
        print(f'{nom_client}, bienvenue dans notre cafe.')
    elif genre == 'monsieur':
        nom_client = input(
            f'Bonjour joli {genre}, comment vous appelez-vous ? ')
        print(f'{nom_client}, bienvenue dans notre cafe.')
    else:
        print('Veuillez saisir dame ou monsieur, merci.')


def commande():
    """Cette fonction permet au client de passer commande."""
    commander = input(f'Que voulez-vous commander ?:')
    print(f"Votre {commander} sera bientot pret.\n")


def menu_principal():
    """Cette fonction permet d'utiliser les fonctions précédente en une seule fois."""
    client()
    commande()

# Le programme démarre ici.

if __name__ == '__main__':
    menu_principal()
    menu_principal()
