import numpy as np

performance_star_ids = np.loadtxt("./performance.txt", dtype=np.int64, delimiter=' ', usecols=1)
performance_data = np.loadtxt("./performance.txt", dtype=np.float64, delimiter=' ', usecols=(3, 4, 5))


class Star(object):

    def __init__(self, star_id):
        self.filename = "./star_0"+str(star_id)+".txt"
        self.main_data = np.loadtxt(self.filename, dtype=np.float64, delimiter=' ', usecols=(0, 1, 2))
        self.row_index = np.where(performance_star_ids == star_id)[0][0]
        self.APASS_gmag = performance_data[self.row_index][0]
        self.RA = performance_data[self.row_index][1]
        self.DEC = performance_data[self.row_index][2]

        sort = self.main_data[:, 0].argsort()
        self.mjd = self.main_data[:, 0][sort]
        self.Evry_mag = self.main_data[:, 1][sort]
        self.err = self.main_data[:, 2][sort]

    def find_delta_t(self):
        sorted = np.sort(self.mjd)
        print (sorted[-1]-sorted[0]), " day range of data"
        delta_t_list = []
        for i in range(len(sorted)-1):
            diff = np.absolute(sorted[i] - sorted[i+1])
            delta_t_list.append(diff)
        return np.array(delta_t_list)



