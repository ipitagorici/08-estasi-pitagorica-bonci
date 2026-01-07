class RulesSet:
    def __init__(self, rules, source):
        self.rules = rules
        self.source = source

rules_pt1 = [
    "1. Astieniti dalle fave.",
    "2. Non raccogliere ciò che è caduto.",
    "3. Non toccare un gallo bianco.",
    "4. Non spezzare il pane.",
    "6. Non attizzare il fuoco con il ferro.",
    "10. Non mangiare il cuore.",
    "14. Non guardare in uno specchio accanto ad un lume."
]

rules_pt2 = [
    "8. Non attizzare il fuoco col coltello.",
    "10. Aiuta l'uomo che si carica un fardello,\nnon aiutare chi lo depone.",
    "11. Per calzarti avanza prima il piede destro,\nper il pediluvio il sinistro.",
    "12. Non parlare di cose pitagoriche al buio.",
    "37. Astieniti dalle fave."
]

rulesSet_pt1 = RulesSet(rules_pt1, r"Diels - Die Fragmente der Vorsokratiker")
rulesSet_pt2 = RulesSet(rules_pt2, r"Giamblico – 'Protrettico' (IV A.C.)")