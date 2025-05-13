class TemperatureConvertor:
    @staticmethod
    def c_to_f(celsius):
        return (celsius * 9/5) + 32
    
print(TemperatureConvertor.c_to_f(32))