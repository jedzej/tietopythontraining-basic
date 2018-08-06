import csv
import os
import logging


# save data to new line or replace row when data from fist column is the same
def save_data_to_csv(filename, header, data):
    logging.info('filename: %s, header: %s, data: %s'
                 % (filename, header, data))
    if not (os.path.isfile(filename)):
        with open(filename, 'w', newline='') as emty_csv:
            writer = csv.writer(emty_csv)
            logging.info('empty csv file: %s crated' % filename)
            writer.writerow(header)
            logging.info('header - columns name: (%s) are saved' % header)
    with open(filename) as inf:
        reader = csv.reader(inf.readlines())
    with open(filename, 'w', newline='') as outf:
        writer = csv.writer(outf)
        repalced = 0
        for line in reader:
            logging.info('Line in file: %s' % line)
            if not line:
                logging.error('IndexError: list index out of range. '
                              'Empty line in file.  Next lines are lost.')
            logging.info('Check that %s(old value) = %s(new value)'
                         % (line[0], data[0]))
            if line[0] == data[0]:
                logging.info('%s = %s' % (line[0], data[0]))
                writer.writerow(data)
                logging.info('line is replased by %s. Break loop.: ' % data)
                repalced = 1
                break
            else:
                writer.writerow(line)
                logging.info('line is rewrite')
        if repalced != 1:
            logging.info('new line is added: %s' % data)
            writer.writerow(data)
        writer.writerows(reader)
