import argparse


def main(): 
    parser = argparse.ArgumentParser(description= "Script d'analyse")
    parser.add_argument("logpath", help="Chemin vers les fichiers de logs à analyser", type=str)
    args = parser.parse_args()
    
    print(f"Chemin des logs à analyser : { args.logpath}")

    if __name__ == "__main__":
        main()
