import sys
import os
import shutil
from pathlib import Path

def resource_path(relative_path):
    """Obtém o caminho correto dos recursos empacotados"""
    try:
        # PyInstaller cria pasta temp e armazena caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def copiar_pasta_fortinet():
    """Copia pasta FortClient do .exe para C:\Program Files\Fortinet"""
    
    # Caminho da pasta dentro do .exe
    pasta_origem = resource_path("FortClient_Conector_x64")
    
    # Caminho de destino
    pasta_destino = r"C:\Program Files\Fortinet\FortClient_Conector_x64"
    
    try:
        # Criar pasta Fortinet se não existir
        os.makedirs(r"C:\Program Files\Fortinet", exist_ok=True)
        
        # Verificar se pasta origem existe
        if not os.path.exists(pasta_origem):
            print(f"ERRO: Pasta {pasta_origem} não encontrada!")
            return False
        
        # Remover pasta destino se já existir
        if os.path.exists(pasta_destino):
            print("Removendo instalação anterior...")
            shutil.rmtree(pasta_destino)
        
        # Copiar toda a pasta
        print(f"Copiando de: {pasta_origem}")
        print(f"Para: {pasta_destino}")
        shutil.copytree(pasta_origem, pasta_destino)
        
        print("✓ Pasta copiada com sucesso!")
        return True
        
    except PermissionError:
        print("ERRO: Sem permissão! Execute como Administrador.")
        return False
    except Exception as e:
        print(f"ERRO ao copiar: {e}")
        return False

if __name__ == "__main__":
    print("=== Instalador FortClient ===")
    
    if copiar_pasta_fortinet():
        print("Instalação concluída!")
    else:
        print("Falha na instalação!")
        input("Pressione ENTER para sair...")