import logging

log = logging
log.basicConfig(level=log.DEBUG)


log.debug('Mensaje a nivel debug')
log.info('Mensaje a nivel info')
log.warning('Mensaje a nivel warning')
log.error('Mensaje a nivel error')
log.critical('Mensaje a nivel critico')
