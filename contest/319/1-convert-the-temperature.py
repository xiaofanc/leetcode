class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Kelvin = Celsius + 273.15
        k = celsius + 273.15
        # Fahrenheit = Celsius * 1.80 + 32.00
        f = celsius * 1.80 + 32.00
        return k, f