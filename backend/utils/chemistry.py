from rdkit import Chem
from rdkit.Chem import Descriptors

def analyze_molecule(smiles: str):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"error": "Invalid SMILES"}

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    return {"mol_weight": mw, "logP": logp}
