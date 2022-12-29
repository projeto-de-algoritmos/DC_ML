jogadores = [
    {
        "id": 1,
        "nome": "Aguero",
        "ptsFIFA": 20,
        "ptsEnzo": 14,
        "ptsRetro": 20,
    },
    {
        "id": 2,
        "nome": "Batistuta",
        "ptsFIFA": 14,
        "ptsEnzo": 19,
        "ptsRetro": 9,
    },
    {
        "id": 3,
        "nome": "Benzema",
        "ptsFIFA": 12,
        "ptsEnzo": 4,
        "ptsRetro": 13,
    },
    {
        "id": 4,
        "nome": "Bergkamp",
        "ptsFIFA": 15,
        "ptsEnzo": 18,
        "ptsRetro": 14,
    },
    {
        "id": 5,
        "nome": "Cristiano Ronaldo",
        "ptsFIFA": 3,
        "ptsEnzo": 3,
        "ptsRetro": 5,
    },
    {
        "id": 6,
        "nome": "Garrincha",
        "ptsFIFA": 5,
        "ptsEnzo": 16,
        "ptsRetro": 2,
    },
    {
        "id": 7,
        "nome": "Haaland",
        "ptsFIFA": 17,
        "ptsEnzo": 7,
        "ptsRetro": 19,
    },
    {
        "id": 8,
        "nome": "Harry Kane",
        "ptsFIFA": 18,
        "ptsEnzo": 10,
        "ptsRetro": 18,
    },
    {
        "id": 9,
        "nome": "Ibrahimovic",
        "ptsFIFA": 19,
        "ptsEnzo": 12,
        "ptsRetro": 17,
    },
    {
        "id": 10,
        "nome": "Johan Cruijff",
        "ptsFIFA": 10,
        "ptsEnzo": 20,
        "ptsRetro": 10,
    },
    {
        "id": 11,
        "nome": "Lewandowski",
        "ptsFIFA": 11,
        "ptsEnzo": 9,
        "ptsRetro": 15,
    },
    {
        "id": 12,
        "nome": "Luis Suárez",
        "ptsFIFA": 16,
        "ptsEnzo": 13,
        "ptsRetro": 16,
    },
    {
        "id": 13,
        "nome": "Maradona",
        "ptsFIFA": 6,
        "ptsEnzo": 5,
        "ptsRetro": 7,
    },
    {
        "id": 14,
        "nome": "Mbappé",
        "ptsFIFA": 8,
        "ptsEnzo": 1,
        "ptsRetro": 12,
    },
    {
        "id": 15,
        "nome": "Messi",
        "ptsFIFA": 2,
        "ptsEnzo": 2,
        "ptsRetro": 6,
    },
    {
        "id": 16,
        "nome": "Neymar Jr.",
        "ptsFIFA": 9,
        "ptsEnzo": 6,
        "ptsRetro": 11,
    },
    {
        "id": 17,
        "nome": "Pelé",
        "ptsFIFA": 1,
        "ptsEnzo": 8,
        "ptsRetro": 1,
    },
    {
        "id": 18,
        "nome": "Romário",
        "ptsFIFA": 7,
        "ptsEnzo": 17,
        "ptsRetro": 4,
    },
    {
        "id": 19,
        "nome": "Ronaldo Fenômeno",
        "ptsFIFA": 4,
        "ptsEnzo": 11,
        "ptsRetro": 3,
    },
    {
        "id": 20,
        "nome": "Thierry Henry",
        "ptsFIFA": 13,
        "ptsEnzo": 15,
        "ptsRetro": 8,
    },
]

print('-=' * 20)
print('Bem-vindo(a) ao Melhores Jogadores !')
print('-=' * 20)

for n, v in enumerate(jogadores):
    print(f'{n + 1:<2} - {v["nome"]}')

print('-' * 20)
print('Escolha 5 atacantes dentre os acima para formar o seu Top 5\n'
      'melhores atacantes do futebol. (em ordem do primeiro ao último)')
print('-' * 30)

listaUsuario = list()
escolhido = []
pos = 0

while pos < 5:
    try:
        num = int(input('Escolha um jogador (número): '))

        if num not in range(1, 21):
            raise ValueError

        if num not in escolhido:
            escolhido.append(num)
        else:
            raise AssertionError

        for jogador in jogadores:
            if jogador["id"] == num:
                listaUsuario.append(jogador)

        pos += 1

    except ValueError:
        print('!! Informe um número válido !!')

    except AssertionError:
        print('Esse jogador já foi selecionado.')

print('-'*30)
print('Este é o seu Top 5 melhores atacantes:')

for n, v in enumerate(listaUsuario):
    print(f'{n+1}°- {v["nome"]}', end='; ')

