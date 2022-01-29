def reverse(self, x: int) -> int:

        if(x < -2147483648 or x>2147483648):
             return 0
        else:
            if(x>0):
                sup=str(x)
                rev=sup[::-1]
                sup1=int(rev)
                if(sup1 < -2147483648 or sup1 > 2147483648):
                    return 0
                else:
                    return sup1
                
            elif(x==0):
                return 0
            else:
                sup2=str(x)
                rev1=sup2[1:]
                reveat=rev1[::-1]
                sup3="-"+reveat
                sup4=int(sup3)
                if(sup4 < -2147483648 or sup4 > 2147483648):
                    return 0
                else:
                    return sup4
new=int(input("Enter a number: "))
print(reverse(self,new))