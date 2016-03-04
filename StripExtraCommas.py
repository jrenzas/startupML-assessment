import argparse, re, os
from tempfile import mkstemp
from shutil import move
from os import remove, close

def replace(file_path):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(re.sub(r',\n', "\n", line))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def main():
    parser = argparse.ArgumentParser(description="This program strips excess commas and otherwise leaves the file(s) untouched.")
    parser.add_argument('--file', dest='fname', required=True)
    # parser.add_argument('--dir', dest='path', required=False)
    args = parser.parse_args()
    if args.fname:
        fname = args.fname
        replace(fname)
    #elif args.path:
    #    path = args.path
    #    many(path)
    else:
        print('No valid file or directory')
        exit(0)
    print('Success. No more frustrating trailing commas.')

if __name__ == '__main__':
    main()