import os
import sys

from src.handler.handler import Handler

if __name__ == '__main__':
    try:
        handler = Handler()
        handler.execute()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
