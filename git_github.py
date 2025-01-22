num = 5
valor = 1
for c in range(num, 0, -1):
    print(c,end='')
    if c > 1:
        print(' x ', end='')
    else: 
        print(' = ', end='')
    valor = valor * c
print(valor)

print()
name = str(input('Digite o seu nome: '))
print(f'Seja bem vindo {name}')




'''
passDesteCurso testegithub
git  - Para iniciar um projeto git

ls -a -> para mostrar arquivos ocultos

git add "nome.py" -> preparar o codigo no arquivo para commit 
git commit -m "nome" -> para commitar o codigo no arquivo

git status -> mostra se o arquivo ja foi add ou não

FORMA DE SE VER INFORMAÇÕES DE COMMIT:
git log
git log --oneline

DESFAZER COMMIT:
git checkout id ou nome -> não apaga o historico podendo voltar de onde parou
git checkout main -> para voltar todo o ponto que parou
git revert id -> apaga os codigos mas conserva o historico dos commits 
git reset id -> volta para o ponto do commit que voce digitou, apagando todos em diante. presevando o codigo construido
git reset id --hard -> volta para o ponto do commit que voce digitou, apagando todos em diante e apagando todo o codigo já construido

git branch -> mostra todas as branchs
git branch nome -> cria uma branch
git checkout nome -> para trocar de branch
git branch -d nome -> deletar branch, se tiver commit não deleta 
git branch -D nome -> Deleta branch com tudo e de qualquer forma
git merge nome -> para fundir branchs, deve-se estar na branch principal para fundi-las.

git push ssh nomedabranch -> subir commits com a ssh 

git remote add origin ssh -> para dar um nome padrão a chave ssh
git push -u origin nomedabranch -> subir commits com origin

git remote -v -> mostra a ssh nomeada

git clone ssh nomedoprojeto -> para clonar um repositorio, nome do projeto é opcional, se não colocar virá com o nome padrão
'''