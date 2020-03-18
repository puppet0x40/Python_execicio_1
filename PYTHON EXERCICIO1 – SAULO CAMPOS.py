# 1 º Exercício de Python – (0.5 pts)


# criar dicionário aluno
aluno = dict()


# criar lista de alunos
alunos = list()


# criar contador
contador = 1


# Criar Coeficiente de Rendimento (CR)
hora_total = 0  # total de horas do alunos
produto_media_hora = 0  # produto da media e da hora  do aluno
cr_valor = 0  # Coeficiente de Rendimento


# calcular a media
def media_aluno(a, b):
    return (a + b) / 2


# verifica o estado do aluno
def aprovado(a):
    if a >= 6:
        return "aprovado"
    else:
        return "reprovado"


# cr conceito de acordo com o resultado
def cr_infor(a):
    if a < 5:
        return "D (Deficiente)"
    elif a <= 6.9:
        return "C (Regular)"
    elif a <= 8.9:
        return "B (Bom) "
    elif a <= 10:
        return "A (Excelente)"


#entrada com intevalo de 0 a 10
def inputRange(text):
    while True:
        valor = float(input(text))
        if valor >= 0 and valor <= 10:
            return valor
        print("apenas intevalo de 0 a 10 :  tente novamente")


# inserir dados do aluno
while contador <= 10:
    aluno.clear()  # limpa dados antigos
    print('--------------Aluno %d---------------------' % contador)
    aluno['nome'] = str(input("Nome: "))
    aluno["AV1"] = inputRange("Nota do AV1: ")
    aluno["AV2"] = inputRange("Nota do AV2: ")
    aluno["hora"] = int(inputRange("Hora: "))

    # adiciona aluno na lista de alunos
    alunos.append(aluno.copy())

    # incrementa o contador
    contador += 1

    # pre calculo Coeficiente de Rendimento
    hora_total += aluno["hora"]
    produto_media_hora += aluno["hora"] * media_aluno(aluno["AV1"], aluno["AV2"])


# calcula  o Coeficiente de Rendimento
cr_valor = produto_media_hora / hora_total


# mostra os alunos
for aluno in alunos:
    media = media_aluno(aluno['AV1'], aluno['AV2'])
    print('Nome:%s\t' % aluno.get('nome'),
          '\tAV1: %.1f\t' % aluno.get('AV1'),
          '\tAV2: %.1f\t' % aluno.get('AV2'),
          '\tMedia: %.1f' % media,
          '\tHora: %d' % aluno.get('hora'),
          '\tEstado:', aprovado(media))


print("Coeficiente de Rendimento (CR) da turma foi : %.1f" % cr_valor, "\tresultado: ", cr_infor(cr_valor))