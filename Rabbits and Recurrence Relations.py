n = 30                      
k = 5                      
big = 1                    
small = 1                  
for months in range(1,n-1):
      bigger = big + small*k   
      small = big              
      big = bigger             
print(big)   