import os


def get_search_directory():
    return os.path.abspath(os.sep)


def find_files(search_directory, predicate):
    matched_files = []
    for current_dir, sub_dirs, file_names in os.walk(search_directory):
        files_portion = [
            file_path for file_path in [
                os.path.join(current_dir, file_name)
                for file_name in file_names]
            if predicate(file_path)]

        matched_files.extend(files_portion)

    return matched_files


def print_matched_files(matched_files):
    print()
    for matched_file in matched_files:
        print(matched_file)


def predicate(file_path):
    max_size = 100 * 1024 * 1024

    try:
        return os.path.getsize(file_path) > max_size
    except Exception:
        # WIN files with path longer than 260 characters
        # https://stackoverflow.com/questions/3555527/python-win32-filename-length-workaround/3557977
        return False


if __name__ == '__main__':
    search_directory = get_search_directory()

    matched_files = find_files(search_directory, predicate)

    print_matched_files(matched_files)
