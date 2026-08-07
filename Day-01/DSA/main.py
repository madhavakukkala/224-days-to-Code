class Solution():

    def Sum_of_first_N(self,n):
        sum = 0
        for i in range(1,n+1):
            sum += i
        return sum

    def reverse_a_number(self,number):
        reverse = 0
        while number > 0:
            digit = number % 10
            reverse = reverse *10 + digit
            number //= 10
        return reverse     

    def count_digits(self,num):
        count = 0
        while num > 0:
            num % 10
            count += 1
            num //=10
        return count

    def palindrome_number(self,num):
        number = num
        reverse = 0
        while number > 0:
            digit = number % 10
            reverse = reverse *10 + digit
            number //= 10
        return num == reverse

    def armstrong_number(self,num):
        temp = num
        count = 0
        while temp > 0:
            temp % 10
            count += 1
            temp //=10


        temp = num
        sum = 0
        while temp>0:
            digit = temp % 10
            sum += digit ** count 
            temp //= 10

        return sum == num




sol = Solution()

print(sol.Sum_of_first_N(10))
print(sol.reverse_a_number(453))
print(sol.count_digits(1082945))
print(sol.palindrome_number(32523))
print(sol.armstrong_number(153))




#prime check, GCD by Euclid, LCM.
# These are pending

