import argparse
import logging
import sys

logger = logging.getLogger('')
fh = logging.FileHandler('/tmp/passtest_log')
logger.addHandler(fh)

logger.setLevel(logging.INFO)

MOD_OID = '.1.3.6.1.4.1.9999'
SCALAR_OID = '.1.3.6.1.4.1.9999.1'


def main():
    logger.info('command: {}'.format(sys.argv))

    parser = argparse.ArgumentParser()

    parser.add_argument('-g', dest='get_oid', type=str, default=None)
    parser.add_argument('-n', dest='next_oid', type=str, default=None)

    args = parser.parse_args()

    if args.next_oid == MOD_OID or args.get_oid == SCALAR_OID:
        print(SCALAR_OID)
        print('integer')
        print(42)


if __name__ == '__main__':
    main()
