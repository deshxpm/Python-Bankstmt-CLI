import sys
from .bankstdata import Bank
#from .funcmodule import my_function
def main():
    print('\tBank Statement\n')
    args = sys.argv[1:5]
    print('\tcount of args :: {}'.format(len(args)))
    for arg in args:
        print('\tpassed argument :: {}'.format(arg))
   # my_function('Python-Bankstmt')
   # my_object = MyClass('Deepak')
   # my_object.say_name()
if __name__ == '__main__':
    main()