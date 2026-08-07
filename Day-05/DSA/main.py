class Solution():
    def pattern01(self,n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

    def pattern02(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()

    def pattern03(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end="")
            print()

    def pattern04(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i, end="")
            print()

    def pattern05(self,n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print("*", end="")
            print()


    def pattern06(self,n):
        for i in range(1,n+1):
            for j in range(1,n-i+2):
                print(j, end = "")
            print()


    def pattern07(self,n):
        for i in range(n):

            #spaces
            for j in range(n-i-1):
                print(" ", end = "")
            #stars
            for j in range(0,2*i+1):
                print("*", end = "")
            print()

    def pattern08(self,n):
        for i in range(n):
            for j in range(i):
                print(" ", end = "")

            for j in range(2*n - 2*i - 1):
                print("*", end = "")
            print()


    def pattern09(self,n):
        for i in range(n):

            for j in range(n-i-1):
                print(" ", end = "")
            for j in range(2*i+1):
                print("*", end = "")
            print()

        for i in range(n):
            for j in range(i):
                print(" ", end = "")
            for j in range(2*n - 2*i - 1):
                print("*", end = "")
            print()

    def pattern10(self, n):
        for i in range(2*n+1):
            if i>n:
                for j in range(2*n-i):
                    print("*", end = "")
            else:
                for j in range(i):
                    print("*", end = "")
            print()


    def pattern11(self,n):
        for i in range(n):
            num = 0
            if i%2 == 0:
                num = 1
            for j in range(i+1):
                print(num, end = " ")
                num = 1- num
            print()

    def pattern12(self,n):
        for i in range(n):
            for j in range(1,i+2):
                print(j, end = "")

            for j in range(2*(n-i-1)):
                print(" ", end = "")


            for j in range(i+1,0,-1):
                print(j, end = "")
                
            print()


    def pattern13(self,n):
        num = 1
        for i in range(n):
            for j in range(1,i+2):
                print(num ,end = " ")
                num += 1

            print()


    def pattern14(self,n):
        for i in range(n):
            char = 65
            for j in range(1,i+2):
                print(chr(char) ,end = "")
                char+= 1
            print()


    def pattern15(self,n):
        for i in range(n):
            char = 65
            for j in range(n-i):
                print(chr(char), end = "")
                char += 1
            print()

    def pattern16(self,n):
        for i in range(n):
            char = 65 + i
            for j in range(1,i+2):
                print(chr(char), end = "")
            print()


    def pattern17(self,n):
        
        for i in range(n):
            
            chars = 64
            for j in range(n-i-1):
                print(" ", end = "")

            for j in range(2*i+1):
                if j > (2*i+1)/2:
                    chars -= 1
                else:
                    chars += 1
                print(chr(chars), end = "")

            print()


    def pattern18(self,n):
        for i in range(n):
            chars = 64 + n
            for j in range(i+1,0,-1):
                print(chr(chars-i), end = " ")
                chars += 1

            print()

                





                    
  



sol = Solution()

n = 5
# sol.pattern01(n)
# sol.pattern02(n)
# sol.pattern03(n)
# sol.pattern04(n)
# sol.pattern05(n)
# sol.pattern06(n)
# sol.pattern07(n)
# sol.pattern08(n)
# sol.pattern09(n)
# sol.pattern10(n)
# sol.pattern11(n)
# sol.pattern12(n)
# sol.pattern13(n)
# sol.pattern14(n)
# sol.pattern15(n)
# sol.pattern16(n)
# sol.pattern17(n)
sol.pattern18(n)


#Then trailing zeroes in factorial, digit sum, count of digits without loop.
