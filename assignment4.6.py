def computepay(h,r):
    if(h>40):
          result=h*r;
          res=((h-40.0)*(r*0.5));
          x=result+res;
    else:
           result=h*r;
           x=result;
    return x;

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
r=float(rate)
a=computepay(h,r);
print("Pay",a);
