
import numpy as np

import matplotlib.pyplot as plt

# The hashfunction compresses the n bits key into table_size bits

def hash(key,table_size):

    c = (np.sqrt(5)-1)/2.# constant value

    temp=(key*c)%1 # keep fractional part

    return int((np.floor(table_size*temp)))

# Analyze the performance of the hash function

def analyze_hash (physical_memory_size= int(np.power(2,40)),\

    page_size=int(np.power(2,30)),nr_processes=32,\
        
    vrt_add_width=48):

    nr_entries=physical_memory_size//page_size

    print ('physical_memory_size ',physical_memory_size,' Bytes')

    print ('page_size ',page_size,' Bytes')

    print ('nr_entries ',nr_entries,' Bytes')

    acc_array=np.zeros((nr_entries),dtype=np.int32)

    lin_array=np.arange(nr_entries)

    nr_vpn_bits=vrt_add_width-np.log2(page_size)

    vpn_range=int(np.power(2,nr_vpn_bits))

    nr_entries_bits=np.log2(nr_entries)

    for pid in range (32): # exhaustive process id generation

        for vpn in range (vpn_range):# exhaustive virtual address generation

            hash_result=hash(vpn + pid * vpn,nr_entries)

            acc_array[hash_result]+=1

    st_dev=np.std(acc_array)

    mean=np.mean(acc_array)

#plot result

plt.plot(lin_array,acc_array)

ax = plt.gca()

ax.set_xlim((0, nr_entries))

plt.savefig('histogram.png')

plt.show()

num_bins = acc_array.max() - acc_array.min() + 1

# the histogram of the data

n, bins, patches = plt.hist(acc_array, num_bins, density=True, align='mid',\

            facecolor='red', alpha=0.8)

plt.xlabel('Bins')

plt.ylabel('Probability')

st_dev_str=str(round(st_dev,2))

plt.title(r'Distribution of hash result: $\mu=$'+str(mean)+' '\

            +r'$\sigma=$'+st_dev_str)

plt.savefig('distribution.png')

# Tweak spacing to prevent clipping of ylabel

plt.subplots_adjust(left=0.15)

plt.show()

analyze_hash()