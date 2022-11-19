from multipledispatch import dispatch
class Calculator:
    @dispatch(int,int)
    def  sum(self,a,b):
        self.a=a
        self.b=b
        print(a+b)
  
    @dispatch (int,int,int) 
    def sum(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(a+b+c)
        
store=Calculator()
store2=Calculator()
store2.sum(1,2,3)
store.sum(1,2)



