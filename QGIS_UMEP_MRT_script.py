import os
from qgis import processing


for nlat in range(1,47):
    for nlon in range(1,57):
        
        DEM_path =      'your_path_to_input_data/01DEM/DEM_%.2d_%.2d.tif' % (nlat, nlon)       
        DSM_path =      'your_path_to_input_data/02DSM/DSM_%.2d_%.2d.tif' % (nlat, nlon)
        Aspect_path =   'your_path_to_input_data/03Wallaspect/wallaspect_%.2d_%.2d.tif' % (nlat, nlon)
        Height_path =   'your_path_to_input_data/04Wallheight/wallheight_%.2d_%.2d.tif' % (nlat, nlon)
        LC_path =       'your_path_to_input_data/05UMEPLC/UMEPLC_%.2d_%.2d.tif' % (nlat, nlon)
        CDSM_path =     'your_path_to_input_data/06DSMs/cdsm_%.2d_%.2d.tif' % (nlat, nlon)
        TDSM_path =     'your_path_to_input_data/06DSMs/tdsm_%.2d_%.2d.tif' % (nlat, nlon)
        SVF_path =      'your_path_to_input_data/07SVF/%.2d_%.2d/svfs.zip' % (nlat, nlon)

        MET_path = 'your_path_to_input_data/wrf2umep/wrf2umep_%.2d_%.2d.txt' % (nlon+40, nlat+6)
        
        Output_dir = 'your_path_to_output_data/MRT/%.2d_%.2d' % (nlat, nlon)
        if not os.path.exists(Output_dir):
            os.mkdir(Output_dir)

        processing.run("umep:Outdoor Thermal Comfort: SOLWEIG",
        {'INPUT_DSM':DSM_path,
        'INPUT_SVF':SVF_path,
        'INPUT_HEIGHT':Height_path,
        'INPUT_ASPECT':Aspect_path,
        'INPUT_CDSM':CDSM_path,
        'TRANS_VEG':3,'LEAF_START':97,'LEAF_END':300,'CONIFER_TREES':False,
        'INPUT_TDSM':TDSM_path,
        'INPUT_THEIGHT':25,
        'INPUT_LC':LC_path,'USE_LC_BUILD':False,
        'INPUT_DEM':DEM_path,'SAVE_BUILD':False,'INPUT_ANISO':'','ALBEDO_WALLS':0.2,'ALBEDO_GROUND':0.15,'EMIS_WALLS':0.9,'EMIS_GROUND':0.95,'ABS_S':0.7,'ABS_L':0.95,'POSTURE':0,'CYL':True,
        'INPUTMET':MET_path,'ONLYGLOBAL':True,'UTC':8,
        'POI_FILE':None,'POI_FIELD':'','AGE':35,'ACTIVITY':80,'CLO':0.9,'WEIGHT':75,'HEIGHT':180,'SEX':0,'SENSOR_HEIGHT':10,'OUTPUT_TMRT':True,'OUTPUT_KDOWN':False,'OUTPUT_KUP':False,'OUTPUT_LDOWN':False,'OUTPUT_LUP':False,'OUTPUT_SH':False,'OUTPUT_TREEPLANTER':False,
        'OUTPUT_DIR':Output_dir})
