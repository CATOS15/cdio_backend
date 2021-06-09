import unittest
import numpy as np

#Tanimoto coefficient
#Pearson's correlation coefficientf

#How to make a ground_truth
    #Choose an image
    #Greyscale the image
    #use mean / manual set best threshold
    #This is called a ground truth mask




class TestWash(unittest.TestCase):
    def test_quick(self):
        self.assertEqual(sum([2,3]), 5, "6 is nice")




    def tanimoto (img_test, ground_truth_mask):
        inter = img_test.intersection(ground_truth_mask)
        union = img_test.union(ground_truth_mask)

        sum_inter = sum(inter)
        sum_union = sum(union)

        return sum_inter/sum_union



    def pearson_(img_test, ground_truth_mask):
        return np.corrcoef(img_test, ground_truth_mask)




if __name__ == '__main__':
    unittest.main()


    
## Otzu / washing testing
## https://link.springer.com/chapter/10.1007/978-3-319-39393-3_4
## Pearson correlation 
    ## coefficient https://stackabuse.com/calculating-pearson-correlation-coefficient-in-python-with-numpy
## Tanimotos 
    ## https://en.wikipedia.org/wiki/Jaccard_index#:~:text=Tanimoto%20goes%20on%20to%20define,be%20similar%20to%20a%20third.
