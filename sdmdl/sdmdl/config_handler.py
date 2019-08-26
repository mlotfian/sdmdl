import yaml
import io
import os

class config_handler():
    
    def __init__(self,root):
        
        self.root = root
        
        self.search_config()
        self.read_yaml()
        
    def search_config(self):
        
        self.config = ''
        
        for root, dirs, files in os.walk(self.root):
            for file in files:
                file_ext = file.split('.')[-1].lower()
                if file_ext == 'yml' or file_ext == 'yaml':
                    self.config = root + '/' + file
        if self.config == '':
            raise IOError('No yaml file found in root "%s" nor any of its subdirectories' % self.root)
    
    # temp function for creating a yml (WILL NOT END UP IN FINAL PRODUCT) thus will not be tested.
    
    def create_yaml(self,outpath):
        
        yml = { '# config file'         :   ''                          ,
                'data_path = '          :   'D:/sdmdl/data'             ,
                'occurrence_path = '    :   'D:/sdmdl/data/occurrences' }
        
        with io.open(outpath + '/config.yml', 'w', encoding='utf8') as outfile:
            yaml.dump(yml, outfile, default_flow_style=False, allow_unicode=True)
        
    def read_yaml(self):
        
        self.data_path = ''
        self.occ_path = ''
        self.result_path = ''
        
        with open(self.config, 'r') as stream:
            yml = yaml.safe_load(stream)
        for k in yml.keys():
            if 'data_path' in k and not k.startswith('#'):                                                    
                self.data_path = yml[k]
            elif 'occurrence_path' in k and not k.startswith('#'):
                self.occ_path = yml[k]
            elif 'result_path' in k and not k.startswith('#'):
                self.result_path = yml[k] 
        if self.data_path == '' or self.occ_path == '':
            raise IOError('The yaml file found does not contain a path for the data and/or occurrences.')