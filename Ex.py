from pathlib import Path

pasta = Path("Projetos_Senac")
if pasta.exists():
    print("Esta pasta ja existe")
else:
    print("Esse pasta nao existe")
    escolha = input("Deseja cria-lo?:1.sim / 2.nao")
    match escolha:
        case "1":
            pasta.mkdir()
            arquivo = pasta/ "Aprovado.txt"
            arquivo.touch()
            print("A pasta foi criada junto com um arquivo dentro dela")
            print(f"Pasta:{pasta} | Arquivo: {arquivo.name}")
        case "2":
            print("Voce nao criou o arquivo :(")
