#!/usr/bin/env python3

import os
import sys

# Adiciona o diretório atual ao PYTHONPATH se necessário
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.cli import SistemaAlunos

if __name__ == "__main__":
    sistema = SistemaAlunos()
    sistema.executar()
