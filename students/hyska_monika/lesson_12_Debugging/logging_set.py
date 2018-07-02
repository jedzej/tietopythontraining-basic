import os
import logging


def create_logsfile(logs_name, directory='.\logs', log_level='INFO'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name_wit_path = directory + '\\' + logs_name
    logging.basicConfig(level=log_level, filename=file_name_wit_path,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.info('******* start logging *******')
