# Function to find maximum product  
# pair in arr[0..n-1] 
def maxProduct(arr, n): 
  
    if (n < 2): 
        print("No pairs exists") 
        return
  
    if (n == 2): 
        print(arr[0]*arr[1]) 
        return
  
    # Iniitialize maximum and  
    # second maximum 
    posa = 0
    posb = 0
  
    # Iniitialize minimum and  
    # second minimum 
    nega = 0
    negb = 0
  
    # Traverse given array 
    for i in range(n): 
      
        # Update maximum and second 
        # maximum if needed 
        if (arr[i] > posa): 
            posb = posa 
            posa = arr[i] 
          
        elif (arr[i] > posb): 
            posb = arr[i] 
  
        # Update minimum and second  
        # minimum if needed 
        if (arr[i] < 0 and abs(arr[i]) > abs(nega)): 
            negb = nega 
            nega = arr[i] 
          
        elif(arr[i] < 0 and abs(arr[i]) > abs(negb)): 
            negb = arr[i] 
  
    if (nega * negb > posa * posb): 
        print(nega*negb) 
    else: 
        print(posa*posb)
# Driver Code 
t = input()
arr = input().split()	
arr = [int(e) for e in arr ] 
n = len(arr) 
maxProduct(arr, n) 
