# SUBPROGRAMA
def corrigirContrato(digitoErrado, valorDoContrato):
   filtroDoContrato = []
   for valor in valorDoContrato:
       if valor != digitoErrado:
           filtroDoContrato.append(valor)
   if filtroDoContrato == []:
       filtroDoContrato.append('0')

   for i in range(len(filtroDoContrato)):
       if len(filtroDoContrato) > 1 and filtroDoContrato[0] == '0':
           filtroDoContrato.pop(0)

   contratoFiltrado = ''.join(filtroDoContrato)
   filtroDoContrato.clear()

   return contratoFiltrado


# PRINCIPAL
digitoFalho, numeroNegociado = map(str, input().split())
while digitoFalho != '0' or numeroNegociado != '0':
   contratoCorrigido = corrigirContrato(digitoFalho, numeroNegociado)
   print(contratoCorrigido)
   digitoFalho, numeroNegociado = map(str, input().split())
