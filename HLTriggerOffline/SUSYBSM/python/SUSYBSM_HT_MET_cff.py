import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDHarvester import DQMEDHarvester

SUSY_HLT_HT350_MET100 = cms.EDAnalyzer("SUSY_HLT_InclusiveHT",
  trigSummary = cms.InputTag("hltTriggerSummaryAOD"),
  pfMETCollection = cms.InputTag("pfMet"),
  pfJetCollection = cms.InputTag("ak4PFJetsCHS"),
  caloJetCollection = cms.InputTag("ak4CaloJets"),
  TriggerResults = cms.InputTag('TriggerResults','','HLT'),
  TriggerPath = cms.string('HLT_PFHT350_PFMET100_v'),
  TriggerPathAuxiliaryForHadronic = cms.string('HLT_IsoMu24_eta2p1_v'),
  TriggerFilter = cms.InputTag('hltPFHT350Jet30', '', 'HLT'), #the last filter in the path
  PtThrJet = cms.untracked.double(30.0),
  EtaThrJet = cms.untracked.double(3.0)
)

SUSYoHLToHT350oMET100oPOSTPROCESSING = DQMEDHarvester("DQMGenericClient",
  subDirs = cms.untracked.vstring("HLT/SUSYBSM/HLT_PFHT350_PFMET100_v"),
  efficiency = cms.vstring(
    "pfMetTurnOn_eff 'Efficiency vs PFMET' pfMetTurnOn_num pfMetTurnOn_den",
    "pfHTTurnOn_eff 'Efficiency vs PFHT' pfHTTurnOn_num pfHTTurnOn_den"
    ),
  resolution = cms.vstring("")
)

SUSY_HLT_HT300_MET100 = cms.EDAnalyzer("SUSY_HLT_InclusiveHT",
  trigSummary = cms.InputTag("hltTriggerSummaryAOD"),
  pfMETCollection = cms.InputTag("pfMet"),
  pfJetCollection = cms.InputTag("ak4PFJetsCHS"),
  caloJetCollection = cms.InputTag("ak4CaloJets"),
  TriggerResults = cms.InputTag('TriggerResults','','HLT'),
  TriggerPath = cms.string('HLT_PFHT300_PFMET100_v'),
  TriggerPathAuxiliaryForHadronic = cms.string('HLT_IsoMu24_eta2p1_v'),
  TriggerFilter = cms.InputTag('hltPFHT300Jet30', '', 'HLT'), #the last filter in the path
  PtThrJet = cms.untracked.double(30.0),
  EtaThrJet = cms.untracked.double(3.0)
)

SUSYoHLToHT300oMET100oPOSTPROCESSING = DQMEDHarvester("DQMGenericClient",
  subDirs = cms.untracked.vstring("HLT/SUSYBSM/HLT_PFHT300_PFMET100_v"),
  efficiency = cms.vstring(
    "pfMetTurnOn_eff 'Efficiency vs PFMET' pfMetTurnOn_num pfMetTurnOn_den",
    "pfHTTurnOn_eff 'Efficiency vs PFHT' pfHTTurnOn_num pfHTTurnOn_den"
    ),
  resolution = cms.vstring("")
)

SUSY_HLT_HT300_MET110 = cms.EDAnalyzer("SUSY_HLT_InclusiveHT",
  trigSummary = cms.InputTag("hltTriggerSummaryAOD"),
  pfMETCollection = cms.InputTag("pfMet"),
  pfJetCollection = cms.InputTag("ak4PFJetsCHS"),
  caloJetCollection = cms.InputTag("ak4CaloJets"),
  TriggerResults = cms.InputTag('TriggerResults','','HLT'),
  TriggerPath = cms.string('HLT_PFHT300_PFMET110_v'),
  TriggerPathAuxiliaryForHadronic = cms.string('HLT_IsoMu24_eta2p1_v'),
  TriggerFilter = cms.InputTag('hltPFHT300Jet30', '', 'HLT'), #the last filter in the path
  PtThrJet = cms.untracked.double(30.0),
  EtaThrJet = cms.untracked.double(3.0)
)

SUSYoHLToHT300oMET110oPOSTPROCESSING = DQMEDHarvester("DQMGenericClient",
  subDirs = cms.untracked.vstring("HLT/SUSYBSM/HLT_PFHT300_PFMET110_v"),
  efficiency = cms.vstring(
    "pfMetTurnOn_eff 'Efficiency vs PFMET' pfMetTurnOn_num pfMetTurnOn_den",
    "pfHTTurnOn_eff 'Efficiency vs PFHT' pfHTTurnOn_num pfHTTurnOn_den"
    ),
  resolution = cms.vstring("")
)

SUSY_HLT_HT_MET = cms.Sequence(SUSY_HLT_HT350_MET100 +
                                SUSY_HLT_HT300_MET100 +
                                SUSY_HLT_HT300_MET110
)

SUSY_HLT_HT_MET_POSTPROCESSING = cms.Sequence(SUSYoHLToHT350oMET100oPOSTPROCESSING +
                              SUSYoHLToHT300oMET100oPOSTPROCESSING +
                              SUSYoHLToHT300oMET110oPOSTPROCESSING
)
