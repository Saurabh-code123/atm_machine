class Fraction:
     def __init__(self,n,d):
         self.num=n
         self.den=d

     def __str__(self):
         return "{}/{}".format(self.num,self.den)

     def __add__(self,second):
         add_num=self.num*second.den+second.num+self.den
         add_den=self.den*second.den

         return "{}/{}".format(add_num,add_den)
     
     def __sub__(self,second):
          temp_num=self.num*second.den-second.num*self.den
          temp_den=self.den*second.den

          return "{}/{}".format(temp_num,temp_den)


     def __mul__(self,second):
          temp_num=self.num*second.num
          temp_den=self.den*second.den

          return "{}/{}".format(temp_num,temp_den)

     def __truediv__(self,second):
          temp_num=self.num*second.den
          temp_den=self.num*second.den

          return "{}/{}".format(temp_num,temp_den)
