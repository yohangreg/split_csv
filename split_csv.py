import pandas as pd # type: ignore
import sys
import os

library = ""

def check_duplicates(file_path):
    # Carregando o arquivo CSV
    df = pd.read_csv(file_path)

    # Contando a ocorrência de cada código de barras
    duplicate_counts = df['barcode'].value_counts()

    # Filtrando apenas os códigos de barras que aparecem mais de uma vez
    duplicates = duplicate_counts[duplicate_counts > 1]

    if not duplicates.empty:
        print("Barcodes duplicados encontrados:")
        for barcode, count in duplicates.items():
            print(f"{barcode}: {count} vezes")
    else:
        print("Nenhum barcode duplicado encontrado.")

def split_csv(file_path, chunk_size=1000):
    # Carregando o arquivo CSV
    df = pd.read_csv(file_path)

    # Criando um diretório para os arquivos divididos
    output_dir = "split_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Dividindo o DataFrame em pedaços de chunk_size linhas
    num_chunks = (len(df) // chunk_size) + 1
    for i in range(num_chunks):
        chunk = df[i*chunk_size:(i+1)*chunk_size]
        if not chunk.empty:
            output_file = os.path.join(output_dir, library + f"_{i+1}.csv")
            chunk.to_csv(output_file, index=False)
            print(f"Arquivo {output_file} criado com sucesso.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python check_and_split_csv.py <caminho_para_o_arquivo_csv>")
    else:
        file_path = sys.argv[1]
        # check_duplicates(file_path)
        split_csv(file_path)
