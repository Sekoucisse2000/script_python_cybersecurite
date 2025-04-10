import os


def trouver_fichiers_logs(dossier, extension='.log'):
    """
    Parcourt un dossioer et renvoie une liste de fichiers avec l'extension spécifiée.
    """
    fichiers_logs = []
    try:
        # Parcoourt le dossier et recuprere tous les fichiers avec l'extension donnée
            for fichier in os.listdir(dossier):
                if fichier.endswith(extension):
                    fichiers_logs.append(os.path.join(racine, fichier))
                    return fichiers_logs
    except FileNotFoundError:
        print(f"Erreur : Le dossier {dossier} n'a pas ete trouvé.")
        return []
    
    def Lire_fichier_log(fichier_log):
        """
        Lit un fichier de logs et renvoie son contenu sous forme de liste de lignes.
        """
        try:
            with open(fichier, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"Erreur : Le fichier {fichier} n'a pas été trouvé.")
            return []
        
    