def find_batch_letter(number):
    batch_number  =  (number-1)  // 5+1
    batch_letter= chr(64 + batch_number)
    return batch_letter
def main() :
    while True :
        number =int(input("enter the serial number :"))
        if((number>40)and(number<=0)):
            print("he is not from ur class:")
            break
        else:
            batch_letter = find_batch_letter(number)
            print("batch letter for number",number,"is:",batch_letter)
if __name__  ==  "__main__": 
         main() 
