import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

===========================================================================

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logging.warning('Total time the function({}) was executed: {} minutes {} seconds'.format(func.__name__, minutes, seconds))
