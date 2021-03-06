   
pdb_list_file = open('pdb_clean_list.txt','r')

probe_dict = {'aro':'AROMATIC CH CARBON', 'uncharged':'UNCHARGED NH NITROGEN', 'carbonyl_O':'CARBONYL OXYGEN', 'carboxylate': 'CARBOXYLATE OXYGEN', 'charged':'CHARGED NH NITROGEN', 'water':'WATER OXYGEN'}

for line in pdb_list_file.readlines():
        line = line.strip()
        pdb = line
        for probe in probe_dict.keys():
            ins_file='''JOBNAME %s_%s
PROBENAME %s
GRID_SPACING 0.5
CALC_CONTOUR_SURFACE 0
RUN_TYPE SUPERSTAR
DATA_SOURCE CSD
SHELL_VALUES 0.5 0
SIGCHECK_METHOD POISSON SHELL
PROPENSITY_CORRECTION LOGP DEFAULT DEFAULT
MIN_CAVITY_VOLUME 1
CAVITY_RADIUS 1
DATA_TYPE ISOSTAR
MOLECULE_FILE W:\\Informatics\\Pharmacophore\\anthony\\DPhil\\CODE\\CHOC\\src\\WebApp\\SUPERSTAR\\%s.pdb
CAVITY_DETECTION 1
MIN_PSP 4
MIN_PROPENSITY 1.0
SAVE_CAVITY MESH
USE_TORSIONS 1
MAP_FORMAT INSIGHT_ASCII_GRID
SUBSTRUCTURE ALL
'''%(pdb,probe,probe_dict[probe],pdb)
            input_file = open('%s/%s-%s_full.ins'%(pdb,pdb,probe),'w')
            input_file.write(ins_file)
            input_file.close()

