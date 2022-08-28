#Preço de venda = Custo do produto / (1 – Taxas da venda – % Margem)
def precodevenda(cp,tv,cs=0,mg=0):
    return cp/(1-tv-cs-mg)

preco=precodevenda(10,0.14,0.05,0.40)
print(preco)
