import random
import math
from scipy import stats
import matplotlib.pyplot as plt
from queue import Queue


if __name__ == '__main__':
    Numbarray = []   
## Part 1
#Below is the generator, commented out so that the numbers will match the 
#graphs in the report
  #   with open('Netsimrandomnumbers.txt', 'w') as f:
   #     for x in range(0,1000,1):
   #         Numbarray.append(str(random.random())+'\n')
  #          f.write(Numbarray[counter])
   #         print(Numbarray[counter])
   #         counter= counter+1
            
  #  f.close()
    with open('Netsimrandomnumbers.txt', 'r') as f:  #import our numbers generated previously
        x=0
        lines = f.readlines();
        for line in lines:
            Numbarray.append(float(line))
            


  #  for x in range(0,1000,1):
     #   Numbarray.append(random.random())
     #   print(Numbarray[x])
  #  Numbarray.
  #  kolmtest= stats.kstest(Numbarray,'uniform')    
  #  chitest=    stats.chisquare(Numbarray)
 #   plt.figure(1)
  #  n,bins,patches = plt.hist(Numbarray,bins=10)
 #   print(kolmtest)
 
 #Chi square by hand
 #Chi square steps
 #for each observed (from .txt), subtract expected,  (size/bins)
 #Square the difference (Observed - expected)^2
 #divide all the differences by the expected value (will be the same for uniform)
 #Sum all the values from 3, this is the stat with k =10 degrees of freedom
#==============================================================================
#     expected=(1000/10) # for uniform, E=(0+1000)/bins10 =(0+1000)/10 = 100 per bin
#     difference = 0
#     totdifference = 0
#     Bin1=0
#     Bin2=0
#     Bin3=0
#     Bin4=0
#     Bin5=0
#     Bin6=0
#     Bin7=0
#     Bin8=0
#     Bin9=0
#     Bin10=0
#     Chivalue=0
#     for x in range (0,1000,1):
#          if (Numbarray[x]<=.1):
#              Bin1+=1    
#      #==============================================================================
#      #                 
#      #             difference = (float(Numbarray[x] -expected))
#      #             difference = difference*difference
#      #             difference = float(difference/expected)
#      #             totdifference+=difference
#      #             print(difference)
#      #==============================================================================
#          elif (Numbarray[x]<=.2 and Numbarray[x]>=.1):
#              Bin2+=1
#          elif (Numbarray[x]<=.3 and Numbarray[x]>=.2):
#              Bin3+=1
#          elif (Numbarray[x]<=.4 and Numbarray[x]>=.3):
#              Bin4+=1
#          elif (Numbarray[x]<=.5 and Numbarray[x]>=.4):
#              Bin5+=1
#          elif (Numbarray[x]<=.6 and Numbarray[x]>=.5):
#              Bin6+=1
#          elif (Numbarray[x]<=.7 and Numbarray[x]>=.6):
#              Bin7+=1
#          elif (Numbarray[x]<=.8 and Numbarray[x]>=.7):
#              Bin8+=1
#          elif (Numbarray[x]<=.9 and Numbarray[x]>=.8):
#              Bin9+=1
#          elif (Numbarray[x]<=1 and Numbarray[x]>=.9):
#              Bin10+=1
#          
#     Chivalue=(((Bin1-expected)*(Bin1-expected))/expected)
#     Chivalue+=(((Bin2-expected)*(Bin2-expected))/expected)
#     Chivalue+=(((Bin3-expected)*(Bin3-expected))/expected)
#     Chivalue+=(((Bin4-expected)*(Bin4-expected))/expected)
#     Chivalue+=(((Bin5-expected)*(Bin5-expected))/expected)
#     Chivalue+=(((Bin6-expected)*(Bin6-expected))/expected)
#     Chivalue+=(((Bin7-expected)*(Bin7-expected))/expected)
#     Chivalue+=(((Bin8-expected)*(Bin8-expected))/expected)
#     Chivalue+=(((Bin9-expected)*(Bin9-expected))/expected)
#     Chivalue+=(((Bin10-expected)*(Bin10-expected))/expected)
#     print("Critical value at K=(10-1)=9 with alpha=0.05 is 16.9")
#     print("The value we calculated is " +str(Chivalue))
# 
#    # print(chitest)
#   
#   
#   
#   
#   #Kolmgorov test
#   #Because N is greater than 35, Kchi = 1.224/sqrt(1000)
#   #using the same bins as before, as we are concerned with the uniform dist still
#   #(Sum of all observed values, as in the number that fell into this bin) - (Sum of all expected) per bin 
#     Kchi=(1.358/31.62277) 
#     print("the critical value for a Kolmgorov-Smirnoff test with n =1000 is: "+str(Kchi))
#     maxdist=0#this will be the biggest value from the expected value
#     CumulativeProb=0
#     CumulativeCount=0
#     CumulativeCount=Bin1 #increment by adding the next bin per loop
#     CumulativeProb=100#increment by 100 per loop
#     maxdist=(CumulativeCount-CumulativeProb)
#     #HARD WORKING LAZINESS!!! :D
#     CumulativeProb+=Bin2 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#        
#     CumulativeProb+=Bin3 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#         
#     CumulativeProb+=Bin4 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#     
#     CumulativeProb+=Bin5 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#     
#     CumulativeProb+=Bin6 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#     
#     CumulativeProb+=Bin7 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#     
#     CumulativeProb+=Bin8 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#         
#     CumulativeProb+=Bin9 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#         
#     CumulativeProb+=Bin10 #increment by adding the next bin per loop
#     CumulativeProb+=100
#     if ((CumulativeCount-CumulativeProb)>maxdist):
#         maxdist=(CumulativeCount-CumulativeProb)
#         
#     print("The value we have calulated as the largest deviation is: "+ str(maxdist/1000))
#             
#     #    part 1 of assignment done!
#     
#==============================================================================
    
    
    #part 2
    # x2 is the number we are putting into the array
    # lamda is 3 from assignment. We should be rejecting about a third of all
    #samples, or around 1333 calculations
    # x = (-1/Lamda)Ln(R)
    
   # Numbarray2 =[]

  #  with open('NetsimrandomnumbersPart2.txt', 'w') as f:  #
    
  #      for x in range(0,1000,1):
  #          Numbarray2.append((1*(-1/3)*math.log(Numbarray[x])))
   #         f.write(str(Numbarray2[x])+'\n')
  #  plt.figure(2)
  #  n,bins,patches = plt.hist(Numbarray2,bins=10)
  #  f.close()
    
    ### Part 2 done!
    
    ##
    
    ## Part 3
   
    #Its actually saying "Using the numbers generated in part 2 AS THE INTERARRIVAL
    #TIMES" Generate those 1000 values by replacing THAT lambda
    #and repeat this for all 10 lamdas', and plot them all on  the same two grapsh
    
    # Single server queue , "mu" u = 10
    # mu = Average service rate (X per unit of time)
    #Using lamda's of 1 ,2 ,4 , 6 , 8 , 10, 12
    #Lambda = avg arrival rate (X per unit of time)
    # no limit on how many can wait
    #Find Avg number of packets in system
    #
    #to Generate the above data samples, I replaced
    
    Lam1=[]
    Lam2=[]
    Lam4=[]
    Lam6=[]
    Lam8=[]
    Lam10=[]
    Lam12=[]#   not using these as arrays, just resetting and summing
    NumbWaiting=[]
    Workleft = Queue()
    arrivaltime =0; #ai , it is a running "clock" that the below will reference
    Idletime = 0; #bi
    Queuetime = 0; #ci
    servicetime=0#si
    Totalwaittime = 0; #wi add (endtime)
    
    prevarrival=0;
    customerswhowait = 0; # divide totalwait by this
 #do equation with lamda for interarrival
#do equation with mu for service time
#add 
#Solve for = Average number of packets in system
#
#Solve for = Average delay in the system
    with open ('NetsimrandomnumbersLamda1.txt') as f:
         for x in range (0,1000,1):
             hold = f.readline();
             Lam1.append(hold);
         print("Loaded Lam1")
         for x in range (1,999,1):
             if Workleft.empty() == False: #meaning theres someone waiting
                 #print("Queue")
                 Totalwaittime += Workleft.get()
                 servicetime= random.expovariate(10) + Totalwaittime  #10 represents a mu of 10, the amount of "customers" served per "time unit"
                 arrivaltime+= float(Lam1[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 
             else:# Workleft.empty() == True: # nothing to work on so were idle        
 #               #we start work upon arrival
                         
                 servicetime = arrivaltime +random.expovariate(10) 
                 arrivaltime+= float(Lam1[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                    # print('Idle')
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 else:
                     Idletime+=float(arrivaltime-servicetime)
 
         print((Queuetime/NumbWaiting.__len__()))
         del NumbWaiting[:]
         Workleft.empty
         arrivaltime =0; #ai , it is a running "clock" that the below will reference
         Idletime = 0; #bi
         Queuetime = 0; #ci
         servicetime=0#si
         Totalwaittime = 0; #wi add (endtime)
           

                
#==============================================================================
#         It was after doing all this I discovered:
    # Python has a built in Queue().
#         
#         for x in range (1,1000,1): # start at 1 because we dont care when actually arrives, we start measuring from there [0]
#             prevarrival = Lam1[x-1]
#             arrivaltime+= Lam1[x]
#             servicetime+= random.expovariate(10)  #10 represents a mu of 10, the amount of "customers" served per "time unit"
#             if servicetime > arrivaltime:
#                 endtime += (servicetime-arrivaltime)
#                 Totalwaittime += (servicetime-arrivaltime)
#                 
#==============================================================================

         with open ('NetsimrandomnumbersLamda2.txt') as f:
             for x in range (0,1000,1):
                 hold = f.readline();
                 Lam2.append(hold);
         for x in range (1,999,1):
             if Workleft.empty() == False: #meaning theres someone waiting
                 #print("Queue")
                 Totalwaittime += Workleft.get()
                 servicetime= random.expovariate(10) + Totalwaittime  #10 represents a mu of 10, the amount of "customers" served per "time unit"
                 arrivaltime+= float(Lam2[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 
             else:# Workleft.empty() == True: # nothing to work on so were idle        
 #               #we start work upon arrival
                         
                 servicetime = arrivaltime +random.expovariate(10) 
                 arrivaltime+= float(Lam2[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     #print('Idle')
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 else:
                     Idletime+=float(arrivaltime-servicetime)
 
         print((Queuetime/NumbWaiting.__len__()))
         NumbWaiting=[]
         Workleft.empty
         arrivaltime =0; #ai , it is a running "clock" that the below will reference
         Idletime = 0; #bi
         Queuetime = 0; #ci
         servicetime=0#si
         Totalwaittime = 0; #wi add (endtime)
         with open ('NetsimrandomnumbersLamda4.txt') as f:
             for x in range (0,1000,1):
                 hold = f.readline();
                 Lam4.append(hold);
         for x in range (1,999,1):
             if Workleft.empty() == False: #meaning theres someone waiting
                 #print("Queue")
                 Totalwaittime += Workleft.get()
                 servicetime= random.expovariate(10) + Totalwaittime  #10 represents a mu of 10, the amount of "customers" served per "time unit"
                 arrivaltime+= float(Lam4[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 
             else:# Workleft.empty() == True: # nothing to work on so were idle        
 #               #we start work upon arrival
                         
                 servicetime = arrivaltime +random.expovariate(10) 
                 arrivaltime+= float(Lam4[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                    # print('Idle')
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 else:
                     Idletime+=float(arrivaltime-servicetime)
 
         print((Queuetime/NumbWaiting.__len__()))
         NumbWaiting=[]
         Workleft.empty
         arrivaltime =0; #ai , it is a running "clock" that the below will reference
         Idletime = 0; #bi
         Queuetime = 0; #ci
         servicetime=0#si
         Totalwaittime = 0; #wi add (endtime)
         with open ('NetsimrandomnumbersLamda6.txt') as f:
             for x in range (0,1000,1):
                 hold = f.readline();
                 Lam6.append(hold);
         for x in range (1,999,1):
             if Workleft.empty() == False: #meaning theres someone waiting
                 #print("Queue")
                 Totalwaittime += Workleft.get()
                 servicetime= random.expovariate(10) + Totalwaittime  #10 represents a mu of 10, the amount of "customers" served per "time unit"
                 arrivaltime+= float(Lam6[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 
             else:# Workleft.empty() == True: # nothing to work on so were idle        
 #               #we start work upon arrival
                         
                 servicetime = arrivaltime +random.expovariate(10) 
                 arrivaltime+= float(Lam6[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                  #   print('Idle')
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 else:
                     Idletime+=float(arrivaltime-servicetime)
 
         print((Queuetime/NumbWaiting.__len__()))
         NumbWaiting=[]
         Workleft.empty
         arrivaltime =0; #ai , it is a running "clock" that the below will reference
         Idletime = 0; #bi
         Queuetime = 0; #ci
         servicetime=0#si
         Totalwaittime = 0; #wi add (endtime)
         with open ('NetsimrandomnumbersLamda8.txt') as f:
             for x in range (0,1000,1):
                 hold = f.readline();
                 Lam8.append(hold);
         for x in range (1,999,1):
             if Workleft.empty() == False: #meaning theres someone waiting
                 #print("Queue")
                 Totalwaittime += Workleft.get()
                 servicetime= random.expovariate(10) + Totalwaittime  #10 represents a mu of 10, the amount of "customers" served per "time unit"
                 arrivaltime+= float(Lam8[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 
             else:# Workleft.empty() == True: # nothing to work on so were idle        
 #               #we start work upon arrival
                         
                 servicetime = arrivaltime +random.expovariate(10) 
                 arrivaltime+= float(Lam8[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                    # print('Idle')
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 else:
                     Idletime+=float(arrivaltime-servicetime)
 
         print((Queuetime/NumbWaiting.__len__()))
         NumbWaiting=[]
         Workleft.empty
         arrivaltime =0; #ai , it is a running "clock" that the below will reference
         Idletime = 0; #bi
         Queuetime = 0; #ci
         servicetime=0#si
         Totalwaittime = 0; #wi add (endtime)
         with open ('NetsimrandomnumbersLamda10.txt') as f:
             for x in range (0,1000,1):
                 hold = f.readline();
                 Lam10.append(hold);
         f.close()
         for x in range (1,999,1):
             if Workleft.empty() == False: #meaning theres someone waiting
                 #print("Queue")
                 Totalwaittime += Workleft.get()
                 servicetime= random.expovariate(10) + Totalwaittime  #10 represents a mu of 10, the amount of "customers" served per "time unit"
                 arrivaltime+= float(Lam10[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 
             else:# Workleft.empty() == True: # nothing to work on so were idle        
 #               #we start work upon arrival
                         
                 servicetime = arrivaltime +random.expovariate(10) 
                 arrivaltime+= float(Lam10[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                 #    print('Idle')
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 else:
                     Idletime+=float(arrivaltime-servicetime)
 
         print((Queuetime/NumbWaiting.__len__()))
         NumbWaiting=[]
         Workleft.empty
         arrivaltime =0; #ai , it is a running "clock" that the below will reference
         Idletime = 0; #bi
         Queuetime = 0; #ci
         servicetime=0#si
         Totalwaittime = 0; #wi add (endtime)
         with open ('NetsimrandomnumbersLamda12.txt') as f:
             for x in range (0,1000,1):
                 hold = f.readline();
                 Lam12.append(hold);
         for x in range (1,999,1):
             if Workleft.empty() == False: #meaning theres someone waiting
                 #print("Queue")
                 Totalwaittime += Workleft.get()
                 servicetime= random.expovariate(10) + Totalwaittime  #10 represents a mu of 10, the amount of "customers" served per "time unit"
                 arrivaltime+= float(Lam12[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 
             else:# Workleft.empty() == True: # nothing to work on so were idle        
 #               #we start work upon arrival
                         
                 servicetime = arrivaltime +random.expovariate(10) 
                 arrivaltime+= float(Lam12[x+1]) # ARRIVAL OF THE next PACKET
                 if servicetime > arrivaltime: #
#                     print('Idle')
                     Queuetime+=float(servicetime-arrivaltime)
                     Workleft.put(float(servicetime-arrivaltime))
                     NumbWaiting.append(Workleft.qsize()) #create a list and divide the sum by 1000 for avg number waiting
                 else:
                     Idletime+=float(arrivaltime-servicetime)
 
         print((Queuetime/NumbWaiting.__len__()))
         print("tdas")
 
#         
#     
#==============================================================================
    
            
            
    pass