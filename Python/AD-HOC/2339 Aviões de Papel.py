competidores, quantidade_folhas, folhas_receber = map(int, input().split())
if quantidade_folhas // competidores >= folhas_receber:
    print('S')
else:
    print('N')
