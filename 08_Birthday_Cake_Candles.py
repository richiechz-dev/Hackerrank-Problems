def birthdayCakeCandles(candles):
    tallest = max(candles)
    contador = candles.count(tallest)
    
    return contador
    


if __name__ == "__main__":
    candles = [3, 2, 1, 3]
    print(birthdayCakeCandles(candles))
    
