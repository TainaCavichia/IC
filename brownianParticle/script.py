import matplotlib.pyplot as plt
endereco_arquivo = "dump.lammpstrj"

with open(endereco_arquivo, "r") as arquivo:
    #salva arquivo lido 
    linhas = arquivo.read()
    arquivo.close()
    dados_posicoes = []
    #cria lista de linhas => linhas = ['l0','l1','l2','l3', ...]
    linhas = linhas.split('\n')
    #laço que pega quantidade de linhas do arquivo de dados
    for i in range(1, len(linhas)+1):
        if i%10 == 0:
            #cria lista com as 3 posições => posicoes = ['x','y','z']
            posicoes = linhas[i-1].split()[:3]
            #adiciona as 3 posições a lista de todas as posições => dados_posicoes = [x1,y1,z1,x2,y2,z2...]
            dados_posicoes.append(float(posicoes[0]))
            dados_posicoes.append(float(posicoes[1]))
            dados_posicoes.append(float(posicoes[2]))
    #posições de referencia
    xo = dados_posicoes[0]
    yo = dados_posicoes[1]
    zo = dados_posicoes[2]
    #como só temos uma partícula, o msd, no instante t, será simplesmente (x(t)-xo)² + (y(t)-yo)² + (z(t)-zo)²
    msd = []
    #tem algo dando errado aqui... vou assumir que deu certo para seguir em frente, pois não acho o erro
    for i in range(0, len(dados_posicoes),3):
        dx2 = (dados_posicoes[i]-xo)**2
        dy2 = (dados_posicoes[i+1]-yo)**2
        dz2 = (dados_posicoes[i+2]-zo)**2
        r = dx2 + dy2 + dz2
        msd.append(r)
    #gera lista com steps
    xpoints = []
    for i in range(0, int(linhas[int(len(linhas))-10])+1, int(linhas[11])):
        xpoints.append(i)
    plt.plot(xpoints, msd)
    plt.show()
