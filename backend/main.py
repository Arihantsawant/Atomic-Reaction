from fastapi import FastAPI
from routes.simulation import router as sim_router

app = FastAPI(title="ChemSim MVP")

app.include_router(sim_router, prefix="/simulate")
