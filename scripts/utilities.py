# from msilib.schema import Class
import dvc.api as dvc
import pandas as pd
import io 

class Utilities:

    def get_df(self,path, rep, rev):
        """ Accces data tracked with DVC """

        data = dvc.read(path=path,repo=rep, rev=rev)
        dataframe = pd.read_csv(io.StringIO(data))

        return dataframe