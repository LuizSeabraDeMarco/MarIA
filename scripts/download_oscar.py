import requests
import xarray as xr

# URL do arquivo com os filtros ERDDAP
url = "https://apdrc.soest.hawaii.edu/erddap/griddap/hawaii_soest_5423_4405_a3c7.nc?u[(2024-12-26T22:20:00Z):1:(2024-12-26T22:20:00Z)][(15.0):1:(15.0)][(-80.0):1:(80.0)][(20.0):1:(420.0)],v[(2024-12-26T22:20:00Z):1:(2024-12-26T22:20:00Z)][(15.0):1:(15.0)][(-80.0):1:(80.0)][(20.0):1:(420.0)],um[(2024-12-26T22:20:00Z):1:(2024-12-26T22:20:00Z)][(15.0):1:(15.0)][(-80.0):1:(80.0)][(20.0):1:(420.0)],vm[(2024-12-26T22:20:00Z):1:(2024-12-26T22:20:00Z)][(15.0):1:(15.0)][(-80.0):1:(80.0)][(20.0):1:(420.0)]"

# Baixando o conteúdo do arquivo
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Salvando o arquivo localmente
    with open('dados.nc', 'wb') as f:
        f.write(response.content)
    print("Arquivo baixado com sucesso!")
    
    # Abrindo o arquivo NetCDF usando xarray
    try:
        ds = xr.open_dataset('dados.nc')
        print(ds)
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o arquivo: {e}")
else:
    print(f"Falha ao baixar o arquivo. Status Code: {response.status_code}")
