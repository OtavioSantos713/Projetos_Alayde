import pandas as pd

# Caminho completo do arquivo
arquivo = r"C:\Users\OtavioAugustoSantosD\Técnico 2°C\Python jájá\financeiro.csv"

# Lê o CSV (formato brasileiro)
df = pd.read_csv(
    arquivo,
    sep=';',          # separador é ponto e vírgula
    encoding='latin1', # padrão do Excel no Windows
    thousands='.',     # separador de milhar
    decimal=',',       # separador decimal
    engine='python'
)

# Remove espaços extras nas células
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Remove colunas completamente vazias (caso existam ";;;;" no final)
df.dropna(axis=1, how='all', inplace=True)

# Exibe a tabela formatada
print("\n=== CONTROLE FINANCEIRO ===\n")
print(df.to_string(index=False))