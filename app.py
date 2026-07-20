'''
 this is the main entry point of the app 
'''

from ui.web import render_web
import sys 

def main():
    render_web()

if __name__ == '__main__':
    sys.exit(main())
