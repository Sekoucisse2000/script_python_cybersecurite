import argparse

def main():
    parse  =argparse.ArgumentParser(description= "Script d'analyse")
    parse .add_argument("logpath", help="Chemin vers les fichiers de logs à analyser", type=str)
    args = parse.parse_args()
    
    print ( f"Chemin des logs à analyser : { args.logpath}")

    if __name__ == "__main__":
    
        main()