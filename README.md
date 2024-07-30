# CSV Checker and Splitter

Este script em Python verifica duplicatas em um arquivo CSV e divide o arquivo em arquivos menores de até 1000 itens.

## Requisitos

- Python 3.x
- Biblioteca `pandas`

## Instalação

1. **Instale o Python**:
   - Baixe e instale a versão mais recente do Python a partir do [site oficial](https://www.python.org/).

2. **Instale o Pandas**:
   - Instale a biblioteca `pandas` usando o pip:
     ```sh
     pip install pandas
     ```

## Uso

1. **Clone ou baixe o repositório**.
2. **Prepare o arquivo CSV**:
   - Crie ou obtenha um arquivo CSV com os dados que deseja verificar e dividir. Certifique-se de que o CSV possui uma coluna chamada `barcode`.

3. **Execute o Script**:
   - Abra um terminal (Prompt de Comando no Windows ou Terminal no macOS/Linux).
   - Navegue até o diretório onde você salvou o script `split_csv.py` e o arquivo CSV.
   - Execute o script usando o comando:
     ```sh
     python split_csv.py <caminho_para_o_arquivo_csv>
     ```

### Exemplo

Se você tem um arquivo `dados.csv` com o seguinte conteúdo:

```csv
itemnumber,barcode
335074,EST00000001
335075,EST00000002
335076,EST00000003
335077,EST00000004
335078,EST00000005
335079,EST00000006
335080,EST00000007
335081,EST00000008
335082,EST00000009
335083,EST00000010
335084,EST00000011
335085,EST00000012
335086,EST00000013
335087,EST00000014
335088,EST00000015
335089,EST00000016
335090,EST00000017
335091,EST00000018
335092,EST00000019
335093,EST00000020
335094,EST00000021
335095,EST00000022
335096,EST00000023
335097,EST00000024
335098,EST00000025
335099,EST00000026
335100,EST00000027
335101,EST00000028
335102,EST00000029
335103,EST00000030
335104,EST00000031
335105,EST00000032
335106,EST00000033
335107,EST00000034
335108,EST00000035
335109,EST00000036
335110,EST00000037
335074,EST00000001
335075,EST00000002
```

Execute o script com o comando:

```sh
python split_csv.py dados.csv
```

A saída será algo como:

```
Barcodes duplicados encontrados:
EST00000001: 2 vezes
EST00000002: 2 vezes
Arquivo split_files/chunk_1.csv criado com sucesso.
```

O script dividirá o arquivo `dados.csv` em arquivos menores, cada um contendo até 1000 itens, e os salvará na pasta `split_files`.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Este README fornece instruções claras sobre como instalar, configurar e executar o script, bem como um exemplo de uso e informações sobre a licença.