from operator import index

times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Bragantino', 'Ceara', 'Corinthians', 'Cruzeiro', 'Vasco',
         'Juventude', 'Sao Paulo', 'Mirassol', 'Internacional', 'Bahia', 'Fortaleza', 'Botafogo',
         'Vitoria', 'Atletico MG', 'Santos', 'Gremio', 'Sport')

print(times[:5])
print(times[16:20])
print(sorted(times))
print(times.index('Flamengo')+1)