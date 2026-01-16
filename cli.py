#!/usr/bin/env python3
"""
Interface de Linha de Comando (CLI) para o Sistema de Gerenciamento de Alunos
Execute: python cli.py
"""
import os
import sys

# Adiciona o diretório atual ao PYTHONPATH se necessário
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.cli import SistemaAlunos

if __name__ == "__main__":
    sistema = SistemaAlunos()
    sistema.executar()
