# Converts condensed structural formulas such as CH3CH2OH to IUPAC names

import sys
from rdkit import Chem, RDLogger
import pubchempy as pcp

RDLogger.DisableLog("rdApp.*")

def main():
    while True:
        try:
            formula = input("Please input a condensed structural formula: ").strip()
            if not formula:
                continue
            if formula.lower() in ("quit", "exit", "q"):
                sys.exit("\nThanks for trying me out!")
            smiles_formula = condensed_to_smiles(formula)
            mol = Chem.MolFromSmiles(smiles_formula)
            if mol is None:
                print("Invalid formula :(. Try again.")
                continue
            compounds = pcp.get_compounds(smiles_formula, "smiles")
            if not compounds:
                print("Name could not be found.")
                continue
            print(f"{formula} is {compounds[0].iupac_name}!")

        except EOFError:
            sys.exit("\nThanks for trying me out!")

def condensed_to_smiles(formula):
    formula = formula.replace("COOH", "C(=O)O")
    formula = formula.replace("CHO", "C=O")
    formula = formula.replace("CO", "C=O")
    formula = formula.replace("OH", "O")
    formula = formula.replace("NH2", "N")
    formula = formula.replace("CH3", "C")
    formula = formula.replace("CH2", "C")
    formula = formula.replace("CH", "C")
    return formula

if __name__ == "__main__":
    main()