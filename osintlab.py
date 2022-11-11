from os import system, name, path, getcwd
import time, asyncio, sys



def clear() -> None:
    if name == 'nt':
        system('cls')
        return None
    system('clear')


if sys.version_info[0] == 3:
    version = "pip3"
else:
    version = "pip"

async def command(cmd: str) -> None:
    system(f"{version} {cmd}")

clear()
print("Installation des packages...\n\n\n\n\n\n\n")
asyncio.run(command('install gitpython'))
import git
data = {
        1: pseudo,
        2: email,
        3: numtel,
        4: linkedin,
        5: mc,
        6: rs,
        7: of,
        0: tout
}

async def main():

    clear()

    
    print("""
            ____ ____ _ _  _ ___    _    ____ ___  
            |  | [__  | |\ |  |     |    |__| |__] 
            |__| ___] | | \|  |     |___ |  | |__] 

                By Sale Gosse & Noémie - discord.gg/osint                     """)
    

    # Les petits choix

    choix = input("""
 Marquez le/les chiffre(s) de la/des catégorie(s) que vous voulez installer.

[1] - Pseudo
[2] - Email
[3] - Numéro de téléphone
[4] - Linkedin
[5] - Minecraft
[6] - Réseaux Sociaux
[7] - Outils Français


[0] - Tout

                    """)
    
    for i in choix:
        try:
            await data[int(i)]
        except KeyError:
            print(f"Option invalide {i}")
        except ValueError:
            print(f"Nous pensions avoir un nombre, obtenu : {type(i)}\n{i}")


async def tout():
    for i, k in data:
        if i != 0:
           await k
    main()



async def pseudo():
    print('\n--> Les tools Pseudo sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/sherlock-project/sherlock', path.abspath(getcwd())+'/Pseudo/Sherlock/')
    main()
    

async def email(): 


    print('\n--> Les tools Email sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/holehe', path.abspath(getcwd())+'/Email/Holehe/')
    git.Repo.clone_from('https://github.com/novitae/emdofi', path.abspath(getcwd())+'/Email/Emdofi/')
    git.Repo.clone_from('https://github.com/mxrch/GHunt', path.abspath(getcwd())+'/Email/GHunt/')
    main()
    

async def numtel(): 


    print('\n--> Les tools de Numéro de téléphone sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/ignorant', path.abspath(getcwd())+'/NumeroDeTelephone/Ignorant/')
    git.Repo.clone_from('https://github.com/sundowndev/phoneinfoga', path.abspath(getcwd())+'/NumeroDeTelephone/Phoneinfoga/')
    main()
    

async def linkedin(): 


    print('\n--> Les tools Linkedin sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/nqntnqnqmb', path.abspath(getcwd())+'/Linkedin/nqntnqnqmb/')
    git.Repo.clone_from('https://github.com/mxrch/revealin', path.abspath(getcwd())+'/Linkedin/Revealin/')
    main()
    

async def mc(): 


    print('\n--> Les tools Minecraft sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/gg-osint/rinaorc-osint', path.abspath(getcwd())+'/Minecraft/Rinaorc/')
    main()
    

async def rs(): 


    print('\n--> Les tools "Réseaux Sociaux" sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/facebook_totem', path.abspath(getcwd())+'/ReseauxSociaux/Facebook/Facebook_totem/')
    git.Repo.clone_from('https://github.com/megadose/toutatis', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/toutatis')
    git.Repo.clone_from('https://github.com/Datalux/Osintgram', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/Osintgram')
    main()
    

async def of(): 


    print('\n--> Les tools Français sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/Fl0wj0b', path.abspath(getcwd())+'/OutilsFrance/Numero/Fl0wj0b/')
    git.Repo.clone_from('https://github.com/daprofiler/DaProfiler', path.abspath(getcwd())+'/OutilsFrance/Global/DaProfiler/')
    main()
    

asyncio.run(main())


