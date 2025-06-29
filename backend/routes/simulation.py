from fastapi import APIRouter
from pydantic import BaseModel
from utils.chemistry import analyze_molecule

router = APIRouter()

class MoleculeInput(BaseModel):
    smiles: str

@router.post("/")
def simulate(input: MoleculeInput):
    result = analyze_molecule(input.smiles)
    return {"input": input.smiles, "analysis": result}
