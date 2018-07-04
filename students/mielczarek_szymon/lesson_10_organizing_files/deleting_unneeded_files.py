#! python3
import os
import argparse


class DirValidator(argparse.Action):
    """Validate whether a given directory path is really a directory.
    Raise an exception if not."""
    def __call__(self, parser, namespace, values, option_string=None):
        dir_path = values
        if not os.path.isdir(dir_path):
            raise argparse.ArgumentTypeError("Given path {} is not a "
                                             "directory.".format(dir_path))
        setattr(namespace, self.dest, values)


def main():
    parser = argparse.ArgumentParser(
        description="""
    Delete Unneeded Files program.
    The program walks through a folder tree and search for files that
    have a size of more than maximum file size given.""",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--dir',
                        help="Directory path.",
                        action=DirValidator,
                        dest='dir_path',
                        required=True)
    parser.add_argument('--max-file-size',
                        type=int,
                        required=True,
                        help='Maximum file size in MB.')

    args = parser.parse_args()

    for foldername, _, filenames in os.walk(args.dir_path):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            # Get the file size in megabytes
            filesize_mb = os.path.getsize(filepath) >> 20
            if filesize_mb > args.max_file_size:
                print("{} {}MB".format(filepath, filesize_mb))


if __name__ == "__main__":
    main()
