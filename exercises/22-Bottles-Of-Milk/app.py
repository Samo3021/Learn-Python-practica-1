def number_of_bottles():
     i = 99
     while i >= 0:
            if i <=99 and i > 2:
                print(f"{i} bottles of milk on the wall, {i} bottles of milk.")
                print(f"Take one down and pass it around, {i-1} bottles of milk on the wall.")
            elif i == 2:
                print(f"{i} bottles of milk on the wall, {i} bottles of milk.")
                print(f"Take one down and pass it around, {i-1} bottle of milk on the wall.")       
            elif i == 1:
                print(f"{i} bottle of milk on the wall, {i} bottle of milk.")
                print("Take one down and pass it around, no more bottles of milk on the wall.")
            else:
                print("No more bottles of milk on the wall, no more bottles of milk.")
                print("Go to the store and buy some more, 99 bottles of milk on the wall.")
            i=i-1
number_of_bottles()                   
             
     
   
