# Bhanu Verma
# This class contains the dynamic programming algorithm which will help out Amrita in getting the best interest rates

import os
import time
from os import listdir
from os.path import isfile, join

class dynamic_programming(object):
    def __init__(self):
        # Initializing data structure here

        self.day_arr = []       # each entry in this array contains array of interests
        self.data_files = []    # each entry in this array contains file name for each file in data folder
        

    def load_file_data(self,input_path):
        # populating data files
        self.data_files = [f for f in listdir(input_path) if '.txt' in f and isfile(join(input_path, f))]


    def load_day_data(self,file_name):
        # reading data from file, formatting it and storing it in day_arr

        with open(file_name) as f:
            content = [line.strip('\n') for line in f.readlines()]
            temp = content[0].split(',')
            no_of_days, no_of_instances = int(temp[0]), int(temp[1])

            for i in range(1,no_of_instances+1,1):
                temp_days = content[i].split(',')
                days = [float(rate) for rate in temp_days]
                self.day_arr.append(days)
        

    def get_max_arr(self,nums):
        # Algorithm for calculating maximum sum from continguous sub-array
        max_till_here = nums[0]
        max_total = nums[0]
        temp_start = 0
        start = 0
        end = 0

        for i in range(1,len(nums)):
            if nums[i] >= max_till_here+nums[i]:
                temp_start = i

            max_till_here = max(nums[i],max_till_here+nums[i])

            if max_till_here >= max_total:
                start = temp_start
                end = i

            max_total = max(max_total,max_till_here)

        return max_total,start,end


    def save_output(self,file_name,data):
        # saving output in the output files for each input file

        file_name = 'output/bverma3_output_dp_' + file_name

        with open(file_name,'w') as f:
            for i in range(len(data)):
                f.write(data[i])

                # avoid printing extra line in the end
                if i < len(data)-1:
                    f.write('\n')


    def run_dp(self):
        path = os.path.join(os.path.dirname(__file__), 'data/')
        self.load_file_data(path)

        for file in self.data_files:
            print("Loading data for file",file,"....")
            self.load_day_data('data/'+file)
            print("Finished loading data for file",file,"....")
            output = []

            print()
            print("Running DP Algorithm for file",file,"....")
            for day in self.day_arr:
                start_time = time.time() * 1000
                val,i,j = self.get_max_arr(day)
                exec_time = (time.time() * 1000) - start_time
                val = "%.2f" % val
                exec_time = "%.2f" % exec_time

                out_str = val + ',' + str(i+1) + ',' + str(j+1) + ',' + exec_time
                output.append(out_str)
                # break
            print("Finished running DP Algorithm for file",file,"....")
            print()

            self.save_output(file,output)
            # break


if __name__ == '__main__':
    dp = dynamic_programming()
    dp.run_dp()

