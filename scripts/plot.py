
import sys,os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
sys.path.append('./')
from scripts.logger import Logger


class Plot:
    def __init__(self) -> None:
       
        try:
            self.logger = Logger("plot.log").get_app_logger()
            self.logger.info(
                'Successfully Instantiated Preprocessing Class Object')
        except Exception:
            self.logger.exception(
                'Failed to Instantiate Preprocessing Class Object')
            sys.exit(1)
    
    def plot_bar(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
        
        plt.figure(figsize=(12, 7))
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        self.logger.info(
            'Plotting a bar chart')
        plt.show()

    def plot_profile(self, df: pd.DataFrame, title: str) -> None:
       
        profile = ProfileReport(df)
        profile.to_file(output_file=f'{title}.html')
        self.logger.info(
            'Plotting a profile for the dataset: ')
        return profile

    def plot_pie(self, data, labels, title) -> None:
        
        plt.figure(figsize=(12, 7))
        colors = sns.color_palette('bright')
        plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
        plt.title(title, size=20)
        self.logger.info(
            'Plotting a pie chart')
        plt.show()

    def plot_hist(self, df: pd.DataFrame, column: str, color: str) -> None:
        
        sns.displot(data=df, x=column, color=color,
                    kde=True, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        self.logger.info(
            'Plotting a histogram')
        plt.show()
    
    def plot_hist_muli(self, df):
        
        sns.set()
        num_feats = list(df.select_dtypes(
            include=['int64', 'float64', 'int32']).columns)
        self.logger.info("Multiple histogram")
        df[num_feats].hist(figsize=(20, 15))


    # def plot_line(x, y, hue, style,df):
    #     sns.lineplot( x=x_col, y=y_col, hue=column, style=style data=df)
             

    def plot_count(self, df: pd.DataFrame, column: str) -> None:
        
        plt.figure(figsize=(12, 7))
        self.logger.info(
            'Plotting a plot_count')
        sns.countplot(df, hue=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()
   

    def plot_heatmap(self, df: pd.DataFrame, title: str, cbar=False) -> None:
        
        plt.figure(figsize=(12, 7))
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                    vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=18, fontweight='bold')
        self.logger.info(
            'Plotting a heatmap for the dataset: ')
        plt.show()

    def plot_box(self, df: pd.DataFrame, x_col: str, title: str) -> None:
        
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        self.logger.info(
            f'Plotting a box plot for Column: {x_col}')
        plt.show()
    

    def plot_box_multi(self, df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
        
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        self.logger.info(
            'Plotting a multiple box plot: ')
        plt.show()

    def plot_scatter(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        self.logger.info(
            'Plotting a scatter plot')
        plt.show()

    

    # function to get the values in a plot
    def plot_hist_2d(self, df1: pd.DataFrame, df2: pd.DataFrame, x_col: str, y_col: str, title: str, label1, label2) -> None:
        """Plot multiple histograms of the data.
        Args:
            df(pd.DataFrame): Dataframe to be plotted.
            x_col(str): column to be plotted.
        """
        sns.set()
        plt.hist(df1[x_col], color='black', alpha=0.3, label=label1)
        plt.hist(df2[y_col], color='red', alpha=0.3, label=label2)
        plt.legend()
        plt.plot()
        plt.title(title, size=20)
        self.logger.info(
            'Plotting multiple histogram')
        plt.show()

    def get_value(self, figure):
        
        self.logger.info(
            'Getting value for a plot')
        for p in figure.patches:
            figure.annotate(format(p.get_height()), (p.get_x() + p.get_width() / 2.,
                                                     p.get_height()), ha='center', va='center',
                            xytext=(0, 10), textcoords='offset points')

    # function to set figure parameters

    def fig_att(self, figure, title, titlex, titley, size, sizexy, weight):
       
        # setting the parameters for the title, x and y labels of the plot
        figure.set_title(title, size=size, weight=weight)
        figure.set_xlabel(titlex, size=sizexy, weight=weight)
        figure.set_ylabel(titley, size=sizexy, weight=weight)
        self.logger.info(
            'set figure parameters')

    # function to change rotation of the x axis tick labels
    def rotate(self, figure, rotation):
        
        # changing the rotation of the x axis tick labels
        self.logger.info(
            'Plotting a chart')
        for item in figure.get_xticklabels():
            item.set_rotation(rotation)

   
    def plot_subplots(self, x: str, y: str, xtitle: str, ytitle: str) -> None:
        
        sns.set(style="whitegrid")
        fig, axes = plt.subplots(nrows=1, ncols=2)
        fig.set_size_inches(25, 8)
        x.hist(ax=axes[0], alpha=0.3, color='red', bins=20)
        y.hist(ax=axes[1], alpha=0.3, color='blue', bins=20)
        axes[0].set_title(xtitle, size=20)
        axes[1].set_title(ytitle, size=20)
        self.logger.info(
            'Plotting a subplots')
        plt.show()

    def plot_heatmap_from_correlation(self, correlation, title: str):
        '''
        heatmap: Plot rectangular data as a color-encoded matrix and correlation matrix.
        title: Title of the plot
        correlation: correlation matrix
        '''
        plt.figure(figsize=(14, 9))
        sns.heatmap(correlation)
        plt.title(title, size=18, fontweight='bold')
        plt.show()