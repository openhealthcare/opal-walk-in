"""
Discharge summary template for Walkin
"""
from dischargesummary import DischargeTemplate

class WalkinDischargeLetter(DischargeTemplate):
    name = 'walkin'
    template = 'walkin_discharge_letter.html'
