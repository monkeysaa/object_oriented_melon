"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        
        self.species = species
        self.qty = qty
        self.shipped = False
        
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
            
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record whether or not an order has passed inspection."""
        
        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08
    
        
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        
        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    
    def get_total(self):
        """Add $3 interenational fee."""

        international_shipping_fee = 3
        total = super().get_total() + international_shipping_fee

        return total

