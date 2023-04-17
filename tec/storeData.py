# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:29:53 2023

@author: manue
"""

class data:
    def __init__(self) -> None:
        # Data
        self.obsFile = []
        self.navFile = []
        
    def loadObsFile(self, obsFile, satellite):
        self.obsFile = obsFile.sel(sv=satellite).dropna(dim='time',how='all')
    
    def loadNavFile(self, navFile, satellite):
        self.navFile = navFile.sel(sv=satellite).dropna(dim='time',how='all')
    
