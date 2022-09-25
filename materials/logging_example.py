import logging
import somelib

def main():
    #
    logging.basicConfig(
        filename='myapp.log',
        level=logging.INFO,
        format="%(asctime)-15s %(levelname)s %(message)s"
                        )
    # logging.warning("Warning")
    logging.info('Started')
    somelib.call()
    logging.info('Finished')

if __name__ == '__main__':
    main()