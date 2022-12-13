from fastapi import APIRouter

# from rem.routers import files, sensor, command, machines
# from .processes import processes_router, details_router, kill_router
#
router = APIRouter(prefix='/api/v1')
# processes_router.include_router(details_router)
# processes_router.include_router(kill_router)
# router.include_router(processes_router)
# router.include_router(files.router)
# router.include_router(sensor.router)
# router.include_router(command.router)
# router.include_router(machines.router)