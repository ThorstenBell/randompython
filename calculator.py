def calculateAnswer():
    notation = input('Enter a sum: ')
    if (notation == "exit"):
        return
    else:
        try:
            print(eval(notation)) 
        except:
            print("invalid notation")
        finally:
            calculateAnswer()
    
calculateAnswer()
