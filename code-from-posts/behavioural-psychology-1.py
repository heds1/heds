import matplotlib.pyplot as plt
import random

# let's make females = 1, males = 0

# function to simulate yearly births, and return
# the total number of days over one year where 
# the number of males born was >60%.
def simulate_yearly_births(births_per_day):

    # instantiate empty list
    total_uneven_days = []

    # for each day
    for day in range(365):

        # today's births list
        births = []

        # for each baby
        for baby in range(births_per_day):
            
            # assign male or female
            births.append(random.randint(0, 1))

        # get total number of females
        females = sum(births)

        # check if there are <40% females; if so, append '1' to
        # total_uneven_days list
        if (females / births_per_day < .4):
            total_uneven_days.append('1')

    # return the number of days
    return(len(total_uneven_days))

# example results
simulate_yearly_births(45)
simulate_yearly_births(15)

# instantiate lists to append results to 
large_hospital = []
small_hospital = []

# run simulation 100 times
for i in range(100):
    large_hospital.append(simulate_yearly_births(45))
    small_hospital.append(simulate_yearly_births(15))

# plot both lists as histograms on one plot
fig, ax1 = plt.subplots()
ax1.hist([large_hospital, small_hospital],
    label = ['Large hospital', 'Small hospital'],
    bins = 30)
ax1.set_xlabel('Number of days with uneven birth rates')
ax1.set_ylabel('Count')
ax1.legend(loc = 'upper right')
plt.show()