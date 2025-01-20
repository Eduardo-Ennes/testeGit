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
git init

git add . && git commit -m "nome"
git add "nome.py"
git commit "nome"

git log
git log --oneline
git checkout id ou nome 
git revert id
git reset id
git reset id --hard
git branch
git branch nome
git branch -d nome -> se tiver commit não deleta 
git branch -D nome -> Deleta tudo e de qualquer forma
git merge nome
git push -u origin main
'''