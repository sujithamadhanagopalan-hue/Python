x= int(input("enter the choice"))
match x:
      case 1:
           print ("monday")
      case 2:
           print("Tuesday")
      case _:
        print("please choose from 1 and 2")
      
       
#nested matchcase programme
x= int(input("enter the choice"))
match x:
    case 0:
         sub_choice = float(input("enter 0.1, 0.2, 0.3"))

         match sub_choice:
                case 0.1:
                   print("sushi")
                case 0.2:
                    print ("pasta")
                case 0.3:
                    print("pizza")
                case _:
                    print ("choose from 0.1, 0.2, 0.3")
    case 1:
        print("Dosa")
    case 2:
        print("Biryani")
   

a=4
b=2
c=3
result = a**b//c+a%b
print(result)

a=10
b=3
c=2
result = (a>b) and (b*c<a) or (a%c==0)
print(result)

