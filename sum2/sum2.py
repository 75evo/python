def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution_i=0
        solution_j=0
        solution_sum=0
        combination=2
        sum1=0
        i=0
        j=0
        max_sum=0
        exit_script=0
        found_solution=0
        foo=len(nums)
        print (foo)
        print ("list size:",foo)
        if (found_solution==0):
          for i in range (0,foo):
            if (found_solution==1):
              break
            complement=target-nums[i]
            print ("Complement = ",complement)
            if complement in nums:
             for j in range (0,foo):
              print ("for loop for explanation, but slows program")
              print (nums[j],j,complement)
              if (complement == nums[j]):
                print ("Solution is ",j,"and",i)
                for j in range(len(nums)):
                  if nums[j] == complement:
                    if (i!=j):
                     print (i,j)
                     found_solution=1;
                     return (i,j)
                     break
        else:
          print ("Done")

twoSum([2,7,11,15,9],18)
