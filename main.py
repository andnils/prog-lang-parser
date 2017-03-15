from proglangs.proglangs import ProgLangParser

if __name__ == '__main__':
    parser = ProgLangParser()
    programming_languages = parser.parse()
    print(programming_languages[0:10])