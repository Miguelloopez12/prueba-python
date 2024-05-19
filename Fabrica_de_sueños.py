class PointAutomation:

    """
    The PointAutomation class serves to automate the process of assigning points based on the minimum sales quota, sales quantity, product selection, and segment.

    Attributes:
    quota (int): minimum sales quota.
    sale (int): Total sale.
    product (str): The type of product ("Gomas" or "Galletas").
    segment (str): The customer segment ("Oro", "Plata", or "Bronce").
    """

    def __init__(self, quota, sale, product, segment):
        self.quota = quota
        self.sale = sale
        self.product = product
        self.segment = segment

    def assign_points(self):
        points = 0

        # Check if sales exceed the quota
        if self.sale > self.quota:
            if self.product == "Gomas" and self.segment == "Oro":
                points = 234000
                if self.sale > 1.5 * self.quota:
                    points += 20000
        #Comply with the rules for point assignment.
            elif self.product == "Galletas" and self.segment == "Oro":
                points = 156000
                if self.sale > 1.5 * self.quota:
                    points += 30000
            elif self.product == "Galletas" and self.segment == "Bronce":
                points = 120000
        # Check if sales are below the quota
        elif self.sale < self.quota:
            if self.segment == "Plata" and (self.product == "Gomas" or self.product == "Galletas"):
                points = 1000

        # Return points or a message if no points are assigned
        if points == 0:
            return "Debes realizar más ventas para que puedas obtener puntos"
        else:
            return points
        
# Ejemplo de uso

#provide parameters of the sale made
        
quota = 139999
sale = 159000
product = "Gomas"
segment = "Oro"

# Create an instance of the PointAutomation class
run_class = PointAutomation(quota, sale, product, segment)

# Assign points based on the provided parameters
points = run_class.assign_points()

# Print the number of points obtained from the sale
print(f"Cantidad de puntos obtenidos en su venta: {points}")




           


