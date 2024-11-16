if __name__ == "__main__":
    import logging
    import sys

    # Configuração básica do logging para enviar os logs ao stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    logging.info("Iniciando a execução do script...")
    logging.info("Processando dados...")
    logging.info("Execução concluída.")
    logging.warn("Falha ao executar procedimento, code 912MEDHH")
