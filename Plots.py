import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt


def diagnostic_plots(df, variable):
    plt.figure(figsize=(16,4))
    
    #histogram
    
    plt.subplot(1,3,1)
    sns.histplot(df[variable], bins=30)
    plt.title('Histogram')
    
    #Q-Q plot
    
    plt.subplot(1,3,2)
    stats.probplot(df[variable], dist='norm', plot=plt)
    plt.ylabel('RM quantiles')
    
    #boxplot
    plt.subplot(1,3,3)
    sns.boxplot(y=df[variable])
    plt.title('Boxplot')
    
    plt.show()
    
