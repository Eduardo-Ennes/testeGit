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


'''
git init
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



CONFIGURAÇÃO DA SSH:
ssh-keygen -t ed25519 -C "seu_email@example.com"
git remote -v
git remote remove origin

'''