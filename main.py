#receipt calculator
from pyscript import display, document 


def receipt(e): #code for calculating
    document.getElementById('results').innerHTML = "" 
    subtotal = float(document.getElementById('subtotal').value)

    #getting the vat and total
    vat = subtotal * 0.12 
    total = subtotal + vat

    display(f"Subtotal: {subtotal:.2f} silver", target ='results')
    display(f"VAT: {vat:.2f} silver", target ='results')
    display(f"Total: {total:.2f} silver", target ='results')