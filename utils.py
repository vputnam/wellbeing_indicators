import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import date2num

def plot_pie(values, labels, title, name):
    plt.pie(values, autopct='%1.1f%%')
    plt.legend(labels, bbox_to_anchor=(0, 0), loc="lower left", fontsize='x-small')
    plt.title(title)
    plt.axis('equal')
    plt.savefig('plots/'+name+'.png')
    plt.show()
    return(plt)

def plot_time_series(values, labels, title, name):
    plt.plot(values,labels,'-o')
    plt.xticks(rotation=45, fontsize='x-small')
    plt.title(title)
    plt.axvspan(date2num(datetime(2020,3,25)), date2num(datetime(2020,4,27)),label="Level-4 lockdown",color="green", alpha=0.3)   
    plt.tight_layout()
    plt.legend()
    plt.savefig('plots/'+name+'.png')
    plt.show()
    return(plt)

def plot_time_series_no_ref(values, labels, title, name):
    plt.plot(values,labels,'-o')
    plt.locator_params(axis='x', nbins=10)
    plt.xticks(rotation=45, fontsize='x-small')
    plt.title(title) 
    plt.tight_layout()
    plt.savefig('plots/'+name+'.png')
    plt.show()
    return(plt)