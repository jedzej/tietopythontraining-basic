import os
import re
import argparse
import datetime
import sys
import logging


def create_example_test_files(path, source_folder_param):
    index = 100
    os.chdir(path)
    print('Current working folder ', os.getcwd() + os.linesep)
    src_dir = ""

    """Create source folder(extend date/time approach)"""
    if source_folder_param is not None:
        if os.path.exists(source_folder_param):
            random_folder = os.path.join(source_folder_param + '_' +
                                         str(datetime.datetime.now().date()) +
                                         '_' + str(datetime.datetime.now().
                                                   time()).replace(':', '.'))
            src_dir = random_folder
        else:
            src_dir = source_folder_param

    """ Create example of few files """
    file_list = [os.path.join(src_dir, "file_1.txt"),
                 os.path.join(src_dir, "file_2.txt"),
                 os.path.join(src_dir, "file_3.txt"),
                 os.path.join(src_dir, "file_4.txt"),
                 os.path.join(src_dir, "file_5.txt"),
                 os.path.join(src_dir, "file_6.txt"),
                 os.path.join(src_dir, "file_7.txt"),
                 ]

    for elem in file_list:
        if not os.path.exists(os.path.dirname(elem)):
            os.makedirs(os.path.dirname(elem))
        with open(elem, "w") as test_file:
            index = index + 1
            test_file.write(str(index))
            test_file.close()

    return os.path.join(os.getcwd(), src_dir)


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='regex search helper'
                                                 ' for validate parameters')
    parser.add_argument('-r', '--regex',
                        help='regex user definition',
                        required='True',
                        # default='\d'  # uncomment if workaround for fast
                        #  testing
                        )
    parser.add_argument('-s', '--source',
                        help='source folder',
                        # default='regex_search' # uncomment if workaround
                        # for fast testing
                        )
    parser.add_argument('-vo', '--verbose_output',
                        help='verbosity level: disabled, warning, info',
                        choices=['disabled', 'warning', 'info'],
                        default='info')
    results = parser.parse_args(args)
    return results.regex, results.source, results.verbose_output


def set_verbosity_level(verbosity_level):
    if verbosity_level == 'disabled':
        logging.getLogger().setLevel(logging.CRITICAL)
    elif verbosity_level == 'warning':
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.INFO)


def main():
    """Parse arguments"""
    regex_param, source_param, verbosity_param = parse_args(sys.argv[1:])

    """Set logging configuration"""
    logging.basicConfig(level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    set_verbosity_level(verbosity_param)
    logging.info("verbose level:{0}".format(verbosity_param))

    """Set regular expression"""
    path = create_example_test_files(os.getcwd(), source_param)
    print("Regex parameters is equal r'{0}'".format(regex_param))
    regex = re.compile(r'{}'.format(regex_param))
    logging.info("Regex param:{0}".format(regex_param))

    """Find content by regex functionality"""
    for elem in os.listdir(path):
        if elem.lower().endswith('.txt'):
            input_file = open(os.path.join(path, elem), "r")
            logging.warning("Selected file is opened!")
            content = input_file.readlines()
            for line in content:
                if regex.match(line):
                    print("Content: >>> {0} <<< in {1}".format(line, elem))


if __name__ == '__main__':
    main()
