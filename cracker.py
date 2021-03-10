import optparse
import zipfile
from threading import Thread


def extract_zip(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("[+]Password Found: " + password + "\n")
    except:
        pass


def Main():
    parser = optparse.OptionParser("[-]Incorrect Usage: -f <zipfile> -d <dictionary>")

    parser.add_option("-f", "--filename", dest="zname", type="string", help="Specify zip file")
    parser.add_option("-d", "--dictionary", dest="dname", type="string", help="Specify dictionary/wordlist file")
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip("\n")
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()


if __name__ == "__main__":
    Main()
