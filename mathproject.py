
class Math:

    def __init__(self,count,num1,num2):
        self.count= count
        self.num1 = num1
        self.num2 = num2

    def fractions(self):
        pre_answer = (num1/num2)
        if ".0" not in str(pre_answer):
            num1 = str(num1)
            num2 = str(num2)
            answer = str(num1+"/"+num2)

        if num1 > num2:
            return answer
        if num2 >= num1:
            return answer


    def multiplication(self):

        answer = (self.num1 * self.num2)

        return answer

    def subtraction(self):

        if self.num1 > self.num2:
            answer = (self.num1 - self.num2)
            print(answer)
        if self.num1 < self.num2:
            answer = (self.num2 - self.num1)
            return answer

    def mix_numbers(self):
        if self.num1 > self.num2:
            answer = (self.num1/self.num2)
            if ".0" not in str(answer):
                whole = int(answer)
                numerator = self.num1 - (whole * self.num2)
                denominator = self.num2
                if numerator != 0:
                    return "{} {}/{}".format(whole,numerator,denominator)
            if ".0" in str(answer):
                return answer

    def neg_numbers(self):
        if self.num2 > self.num1:
            answer = (self.num1 - self.num2)
        if self.num1 > self.num2:
            answer = (self.num2 - self.num1)

        return answer

if __name__ == '__main__':
    user1 = input("Enter a number> ")
    user2 = input("Enter a Number> ")
    math = Math(count=0,num1=int(user1),num2=int(user2))
    print(math.mix_numbers())
