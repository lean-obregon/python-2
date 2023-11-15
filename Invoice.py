from dataclasses import dataclass

@dataclass(frozen=False, order=True)
class Invoice:

    invoice_id: str
    user_id: str
    amount: str
    paid: str

    def get_invoice(self):
        return f"{self.invoice_id} {self.user_id} {self.amount} {self.paid}"
