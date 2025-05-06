def contador(inicio, fim, passo):
    if fim > inicio:
        for n in range(inicio,fim+1,passo):
            print(n)
    else:
        for n in range(inicio,fim-1,-(passo)):
            print(n)

contador(1,10,1)
contador(10,0,2)

inicio = int(input('Digite o inicio da contagem'))
fim = int(input('Digite o fim da contagem'))
passo = int(input('Digite o passo da contagem.'))

contador(inicio, fim, passo)