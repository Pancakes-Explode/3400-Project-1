
import os;
from config import Data


if __name__ == "__main__":
    chart = Data(input("Enter latitude: "), input("Enter Longitude: "))

    chart.display_Weather()
    
    # Current display is working but we need the param conditions to be dynamic as well.