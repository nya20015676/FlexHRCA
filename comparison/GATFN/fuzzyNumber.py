import numpy as np
from scipy.stats import norm, nbinom, f
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
import time
import random

class FuzzyNumber:
    mean = 0
    l_std = 0
    l_dist = None
    r_std = 0
    r_dist = None
    low = 0
    up = 0
    l_confidence = 0
    r_confidence = 0
    samples = []
    def __init__(self, l_std, mean, r_std, min=float('-inf'), l_confidence = 0.997, r_confidence = 0.997):
        if l_std != None and r_std != None:
            self.mean = mean
            self.l_std = l_std
            self.r_std = r_std
            self.l_dist = norm(loc=mean, scale=l_std)
            self.r_dist = norm(loc=mean, scale=r_std)
            self.l_confidence = l_confidence
            self.r_confidence = r_confidence
            l_quantile = (1 - l_confidence)/2 # 左分位数
            r_quantile = 1-(1-r_confidence)/2 # 右分位数
            self.min = min
            self.low = max(self.l_dist.ppf(l_quantile), min)
            self.up = self.r_dist.ppf(r_quantile)
            
    def sampling(self):
        if self.samples != []:
            return self.samples
        # 定义原始概率分布函数
        def target_distribution(x):
            if x < self.mean:
                return self.l_dist.pdf(x)
            else:
                return self.r_dist.pdf(x)
        # 进行拒绝采样
        def rejection_sampling(iterations):
            # 定义辅助分布函数（均匀分布）
            def proposal_distribution():
                return np.random.uniform(self.low, self.up)  # 选择一个足够大的范围，以覆盖两个正态分布的取值范围
            samples = []
            for _ in range(iterations):
                x = proposal_distribution()
                u = np.random.uniform(0, 1)
                if u < target_distribution(x):
                    samples.append(x)
            return samples
        # 进行拒绝采样
        self.samples = rejection_sampling(iterations=100000)
        return self.samples
    def random(self):
        if self.samples != []:
            return random.sample(self.samples, 1)[0]
        else:
            return -1


class Triangular(FuzzyNumber):
    def __init__(self, l_std, mean, r_std, min=float('-inf'), l_confidence = 0.997, r_confidence = 0.997):
        super().__init__(l_std, mean, r_std, min, l_confidence, r_confidence)

    def set_triangular(self, low, mean, up):
        # l_quantile = (1 - self.l_confidence)/2 # 左分位数
        # r_quantile = 1-(1-self.r_confidence)/2 # 右分位数
        self.low = low
        self.mean = mean
        self.up = up
        # self.l_std = (low-mean)/norm.ppf(l_quantile)
        # self.r_std = (up-mean)/norm.ppf(r_quantile)
        # self.l_dist = norm(loc=mean, scale=self.l_std)
        # self.r_dist = norm(loc=mean, scale=self.r_std)

    def __gt__(self, number):
        if not isinstance(number, self.__class__): # 说明number是数字
            overall_number = number
            mean_number = number
            spread_number = 0
        else:
            overall_number = (number.low+number.mean*2+number.up)/4
            mean_number = number.mean
            spread_number = number.up - number.low
        
        overall_self = (self.low+self.mean*2+self.up)/4
        mean_self = self.mean
        spread_self = self.up - self.low
        
        if overall_self > overall_number:
            return True
        elif overall_self == overall_number:
            if mean_self > mean_number:
                return True
            elif mean_self == mean_number:
                return spread_self > spread_number
        return False

    def __lt__(self, number):
        if not isinstance(number, self.__class__): # 说明number是数字
            overall_number = number
            mean_number = number
            spread_number = 0
        else:
            overall_number = (number.low+number.mean*2+number.up)/4
            mean_number = number.mean
            spread_number = number.up - number.low
        
        overall_self = (self.low+self.mean*2+self.up)/4
        mean_self = self.mean
        spread_self = self.up - self.low
        
        if overall_self < overall_number:
            return True
        elif overall_self == overall_number:
            if mean_self < mean_number:
                return True
            elif mean_self == mean_number:
                return spread_self < spread_number
        return False
    
    def __eq__(self, number): # 只有在收集optimal CHS list时使用了
        if not isinstance(number, self.__class__): # 说明number是数字
            return self.mean == number
        else:
            return self.mean == number.mean and self.low == number.low and self.up == number.up
    
    def __add__(self, number):
        if isinstance(number, self.__class__):
            return self.plus(self, number)
        else: # 说明number是数字
            return Triangular(self.l_std, self.mean+number, self.r_std)
    def __radd__(self, number):
        if isinstance(number, self.__class__):
            return self.plus(self, number)
        else:
            return Triangular(self.l_std, self.mean+number, self.r_std)
    def __truediv__(self, number):
        if isinstance(number, self.__class__):
            return self.mean/number.mean
        return self.mean/number
    def __rtruediv__(self, number):
        if isinstance(number, self.__class__):
            return number.mean/self.mean
        return number/self.mean
    def __format__(self, format_spec):
        return "TFN = [{:.2f} {:.2f} {:.2f}]".format(self.low, self.mean, self.up)

    @staticmethod
    def plus(triangular1, triangular2):
        up = triangular1.up + triangular2.up
        low = triangular1.low + triangular2.low
        mean = triangular1.mean + triangular2.mean
        result = Triangular(None, None, None)
        result.set_triangular(low, mean, up)
        return result
    
    @staticmethod
    def maximum(triangular_list):
        max_mean = max(triangular_list, key=lambda x: x.mean if isinstance(x, Triangular) else x).mean # 如果进来这个函数，一般最大的是triangular
        max_low = max(triangular_list, key=lambda x: x.low if isinstance(x, Triangular) else x-9999).low
        max_up = max(triangular_list, key=lambda x: x.up if isinstance(x, Triangular) else x-9999).up
        result = Triangular(None, None, None)
        result.set_triangular(max_low, max_mean, max_up)
        return result

    @staticmethod
    def calculate_value(Triangular):
        return (Triangular.low+Triangular.mean*2+Triangular.up)/4
    @staticmethod
    def calculate_spread(Triangular):
        return Triangular.up - Triangular.low
    
class SVTNN(Triangular):

    weight = [0.25, 0.75, 0.75]
    Truth = []
    Indeterminacy = []
    Falsity = []

    def __init__(self,l_std, mean, r_std, min=float('-inf'), alpha=0.682, beta=0.997):
       super().__init__(l_std, mean, r_std, min, l_confidence=beta, r_confidence=beta)
       self.Truth = [self.mean, self.mean, self.mean]
       tmp = FuzzyNumber(l_std, mean, r_std, min, l_confidence=alpha, r_confidence=alpha)
       self.Indeterminacy = [tmp.low, tmp.mean, tmp.up]
       self.Falsity = [self.low, self.mean, self.up]

    def set_TIF(self, T, I, F):
        self.Truth = T
        self.Indeterminacy = I
        self.Falsity = F
        # # 设置父类均值方差
        # l_quantile = (1 - self.l_confidence)/2 # 左分位数
        # r_quantile = 1-(1-self.r_confidence)/2 # 右分位数
        self.low = F[0]
        self.mean = F[1]
        self.up = F[2]
        # self.l_std = (self.low-self.mean)/norm.ppf(l_quantile)
        # self.r_std = (self.up-self.mean)/norm.ppf(r_quantile)
        # self.l_dist = norm(loc=self.mean, scale=self.l_std)
        # self.r_dist = norm(loc=self.mean, scale=self.r_std)

    def set_weight(self, T_w, I_w, F_w):
        self.weight = [T_w, I_w, F_w]

    def __gt__(self, number):
        if not isinstance(number, self.__class__): # 说明number是数字
            number_value = self.calculate_quantity_value([[number,number,number],[number,number,number],[number,number,number]], self.weight)
        else:
            number_value = self.calculate_quantity_value(number, number.weight)
        self_value = self.calculate_quantity_value(self, self.weight)
        if self_value > number_value:
            return True
        elif self_value < number_value:
            return False

        if not isinstance(number, self.__class__): # 说明number是数字
            return True
        self_ambiguity = self.calculate_ambiguity(self, self.weight)
        number_ambiguity = self.calculate_ambiguity(number, number.weight)
        return self_ambiguity > number_ambiguity

    def __lt__(self, number):
        if not isinstance(number, self.__class__): # 说明number是数字
            number_value = self.calculate_quantity_value([[number,number,number],[number,number,number],[number,number,number]], self.weight)
        else:
            number_value = self.calculate_quantity_value(number, number.weight)
        self_value = self.calculate_quantity_value(self, self.weight)
        if self_value < number_value:
            return True
        elif self_value > number_value:
            return False

        if not isinstance(number, self.__class__): # 说明number是数字
            return False
        self_ambiguity = self.calculate_ambiguity(self, self.weight)
        number_ambiguity = self.calculate_ambiguity(number, number.weight)
        return self_ambiguity < number_ambiguity

    def __eq__(self, number):
        if not isinstance(number, self.__class__): # 说明number是数字
            return False
        number_value = self.calculate_quantity_value(number, number.weight)
        number_ambiguity = self.calculate_ambiguity(number, number.weight)    
        self_value = self.calculate_quantity_value(self, self.weight)
        self_ambiguity = self.calculate_ambiguity(self, self.weight)
        return self_value == number_value and self_ambiguity == number_ambiguity

    def __add__(self, number):
        if not isinstance(number, self.__class__): # 说明number是数字
            return self.plus(self, [[number,number,number],[number,number,number],[number,number,number]])
        else:
            return self.plus(self, number)

    def __radd__(self, number):
        if not isinstance(number, self.__class__): # 说明number是数字
            return self.plus(self, [[number,number,number],[number,number,number],[number,number,number]])
        else:
            return self.plus(self, number)

    def __truediv__(self, other):
        if type(self) == type(other):
            return self.mean/other.mean
        return self.mean/other
    def __rtruediv__(self, other):
        if type(self) == type(other):
            return other.mean/self.mean
        return other/self.mean

    def __format__(self, format_spec):
        a = self[0][0]
        b = self[0][1]
        c = self[0][2]
        i = self[1][0]
        j = self[1][1]
        k = self[1][2]
        p = self[2][0]
        q = self[2][1]
        r = self[2][2]
        return "SVTNN = [{:.2f} {:.2f} {:.2f}], [{:.2f} {:.2f} {:.2f}], [{:.2f} {:.2f} {:.2f}]".format(a,b,c,i,j,k,p,q,r)
    def __getitem__(self, idx):
        if idx == 0:
            return self.Truth.copy()
        elif idx == 1:
            return self.Indeterminacy.copy()
        elif idx == 2:
            return self.Falsity.copy()
        else:
            raise IndexError("Index out of range")
    
    @staticmethod
    def calculate_quantity_value(SVTNN, weight):
        a = SVTNN[0][0]
        b = SVTNN[0][1]
        c = SVTNN[0][2]
        i = SVTNN[1][0]
        j = SVTNN[1][1]
        k = SVTNN[1][2]
        p = SVTNN[2][0]
        q = SVTNN[2][1]
        r = SVTNN[2][2]
        weight1 = weight[0]
        weight2 = weight[1]
        weight3 = weight[2]
        # truth_value =           weight1* ((1/3) * i + (1/6) * a) + (1-weight1) * ((1/3) * i + (1/6) * p)
        # indeterminacy_value =   weight2* ((1/6) * j + (1/3) * b) + (1-weight2) * ((1/6) * j + (1/3) * q)
        # falsity_value =         weight3* ((1/6) * k + (1/3) * c) + (1-weight3) * ((1/6) * k + (1/3) * r)
        truth_value =           weight1* (a+4*b+c)/6
        indeterminacy_value =   weight2* (i+4*j+k)/6
        falsity_value =         weight3* (p+4*q+r)/6
        return truth_value + indeterminacy_value + falsity_value
    
    @staticmethod
    def calculate_ambiguity(SVTNN, weight):
        a = SVTNN[0][0]
        b = SVTNN[0][1]
        c = SVTNN[0][2]
        i = SVTNN[1][0]
        j = SVTNN[1][1]
        k = SVTNN[1][2]
        p = SVTNN[2][0]
        q = SVTNN[2][1]
        r = SVTNN[2][2]
        weight1 = weight[0]
        weight2 = weight[1]
        weight3 = weight[2]
        truth_value =           weight1* (c-a)/6
        indeterminacy_value =   weight2* (k-i)/6
        falsity_value =         weight3* (r-p)/6
        return truth_value + indeterminacy_value + falsity_value
    
    @staticmethod 
    def plus(SVTNN1, SVTNN2):
        a1 = SVTNN1[0][0]
        b1 = SVTNN1[0][1]
        c1 = SVTNN1[0][2]
        i1 = SVTNN1[1][0]
        j1 = SVTNN1[1][1]
        k1 = SVTNN1[1][2]
        p1 = SVTNN1[2][0]
        q1 = SVTNN1[2][1]
        r1 = SVTNN1[2][2]
        a2 = SVTNN2[0][0]
        b2 = SVTNN2[0][1]
        c2 = SVTNN2[0][2]
        i2 = SVTNN2[1][0]
        j2 = SVTNN2[1][1]
        k2 = SVTNN2[1][2]
        p2 = SVTNN2[2][0]
        q2 = SVTNN2[2][1]
        r2 = SVTNN2[2][2]

        a = a1+a2
        b = b1+b2
        c = c1+c2
        i = i1+i2
        j = j1+j2
        k = k1+k2
        p = p1+p2
        q = q1+q2
        r = r1+r2
        
        result = SVTNN(None, None, None)
        result.set_TIF([a,b,c], [i,j,k],[p,q,r])
        result.set_weight(SVTNN1.weight[0], SVTNN1.weight[1], SVTNN1.weight[2])
        return result
    
    @staticmethod
    def maximum(SVTNN_list):
        max_T_mean = max(SVTNN_list, key=lambda x: x.Truth[1] if isinstance(x, SVTNN) else x).Truth[1] # 如果进来这个函数，一般最大的是Fuzzynumber
        max_T_low = max(SVTNN_list, key=lambda x: x.Truth[0] if isinstance(x, SVTNN) else x+(-9999)).Truth[0]
        max_T_up = max(SVTNN_list, key=lambda x: x.Truth[2] if isinstance(x, SVTNN) else x+(-9999)).Truth[2]
        max_I_mean = max(SVTNN_list, key=lambda x: x.Indeterminacy[1] if isinstance(x, SVTNN) else x).Indeterminacy[1] 
        max_I_low = max(SVTNN_list, key=lambda x: x.Indeterminacy[0] if isinstance(x, SVTNN) else x+(-9999)).Indeterminacy[0]
        max_I_up = max(SVTNN_list, key=lambda x: x.Indeterminacy[2] if isinstance(x, SVTNN) else x+(-9999)).Indeterminacy[2]
        max_F_mean = max(SVTNN_list, key=lambda x: x.Falsity[1] if isinstance(x, SVTNN) else x).Falsity[1] 
        max_F_low = max(SVTNN_list, key=lambda x: x.Falsity[0] if isinstance(x, SVTNN) else x+(-9999)).Falsity[0]
        max_F_up = max(SVTNN_list, key=lambda x: x.Falsity[2] if isinstance(x, SVTNN) else x+(-9999)).Falsity[2]
        result = SVTNN(None, None, None)
        result.set_TIF([max_T_low,max_T_mean,max_T_up], [max_I_low,max_I_mean,max_I_up],[max_F_low,max_F_mean,max_F_up])
        for svtn in SVTNN_list:
            if isinstance(svtn, SVTNN):
                result.set_weight(svtn.weight[0], svtn.weight[1], svtn.weight[2])
                break
        return result
