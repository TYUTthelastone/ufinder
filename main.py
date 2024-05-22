import module.Logger.logger as log
log.init()
log.info("Starting")
for i in range(0,1000):
    log.debug(f"{i}")
log.info("end")