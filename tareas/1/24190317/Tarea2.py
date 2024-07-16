def CalcularExcesoTela(pulgadas):
    return pulgadas % 36

def CalcularYardasNecesarias(pulgadas):
    return pulgadas // 36

pulgadas_comprar = 100
exceso_tela = CalcularExcesoTela(pulgadas_comprar)
yardas_comprar = CalcularYardasNecesarias(pulgadas_comprar)

print("Si compras", pulgadas_comprar, "pulgadas de tela, te sobrarán", exceso_tela, "pulgadas y necesitarás al menos", yardas_comprar, "yardas.")