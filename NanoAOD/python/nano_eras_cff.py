from Configuration.Eras.Modifier_run2_egamma_2016_cff import run2_egamma_2016
from Configuration.Eras.Modifier_run2_egamma_2017_cff import run2_egamma_2017
from Configuration.Eras.Modifier_run2_egamma_2018_cff import run2_egamma_2018
from Configuration.Eras.Modifier_run2_jme_2016_cff import run2_jme_2016
from Configuration.Eras.Modifier_run2_jme_2017_cff import run2_jme_2017
from Configuration.Eras.Modifier_run2_jme_2018_cff import run2_jme_2018
from Configuration.Eras.Modifier_run2_muon_2016_cff import run2_muon_2016
from Configuration.Eras.Modifier_run2_muon_2017_cff import run2_muon_2017
from Configuration.Eras.Modifier_run2_muon_2018_cff import run2_muon_2018
from Configuration.Eras.Modifier_run3_muon_cff import run3_muon

from Configuration.Eras.Modifier_run2_HLTconditions_2016_cff import run2_HLTconditions_2016
from Configuration.Eras.Modifier_run2_HLTconditions_2017_cff import run2_HLTconditions_2017
from Configuration.Eras.Modifier_run2_HLTconditions_2018_cff import run2_HLTconditions_2018

from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from Configuration.Eras.Modifier_tracker_apv_vfp30_2016_cff import tracker_apv_vfp30_2016

from Configuration.Eras.Modifier_run3_common_cff import run3_common
from Configuration.Eras.Modifier_run3_nanoAOD_pre142X_cff import run3_nanoAOD_pre142X
from Configuration.Eras.Modifier_run3_jme_Winter22runsBCDEprompt_cff import run3_jme_Winter22runsBCDEprompt

run2_nanoAOD_ANY = (
    run2_nanoAOD_106Xv2
)

run2_egamma = (run2_egamma_2016 | run2_egamma_2017 | run2_egamma_2018)