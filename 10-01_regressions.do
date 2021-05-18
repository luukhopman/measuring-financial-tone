clear all

/*
# -----------
# Regressions
# -----------
*/

local NAME "10-01_regressions"
local PROJECT "conference-calls-sentiment"
local STATA_VERSION "16.1"
local PROJECT_DIR "E:/Python/dss-thesis"


/*
# --------
# Settings
# --------
*/

set more off

/*
# ---------------------
# Set working directory
# ---------------------
*/

local full_dir "`PROJECT_DIR'/`PROJECT'"
cd "`full_dir'"

/*
# ---------------
# Market Reaction
# ---------------
*/

use "2_pipeline/07-02_dataset_construction/out/dataset.dta"

est clear
eststo: qui reg car_st lm_tone_norm num_words surprise-capex, vce(cluster gvkey) 
eststo: qui reg car_st  finbert_tone_norm num_words surprise-capex, vce(cluster gvkey) 
eststo: qui reghdfe car_st lm_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)
eststo: qui reghdfe car_st finbert_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)

esttab using "3_output/stata/market_reaction.csv", replace ///
	t(2) b(3) ar2(3) ///
	stats(r2_a N, fmt(3 0)) ///
	star(* 0.1 ** 0.05 *** 0.01)

/*
# --------
# Analysts
# --------
*/

use "2_pipeline/07-02_dataset_construction/out/analysts_dataset.dta"
	
est clear
eststo: qui reghdfe rating_change lm_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)
eststo: qui reghdfe rating_change finbert_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)
eststo: qui reghdfe price_change lm_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)
eststo: qui reghdfe price_change finbert_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)
eststo: qui reghdfe eps_change lm_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)
eststo: qui reghdfe eps_change finbert_tone_norm num_words surprise-capex, absorb(gvkey year) vce(cluster gvkey)

esttab using "3_output/stata/analysts.csv", replace ///
	t(2) b(3) ar2(3) ///
	stats(r2_a N, fmt(3 0)) ///
	star(* 0.1 ** 0.05 *** 0.01)
	
	
use "2_pipeline/09-04_experiment_lm_did/out/tone_did.dta", clear

/*
# ---------------
# LM Negative DID
# ---------------
*/

est clear
eststo: qui reg lm_negative treated post treated_post num_words, vce(cluster gvkey) 
eststo: qui reg lm_negative treated post treated_post num_words surprise-capex, vce(cluster gvkey) 
eststo: qui reghdfe lm_negative treated post treated_post num_words surprise-capex, absorb(year) vce(cluster gvkey)
eststo: qui reghdfe lm_negative treated post treated_post num_words surprise-capex, absorb(year gvkey) vce(cluster gvkey)

esttab using "3_output/stata/did_lm_negative.csv", replace ///
	t(2) b(3) ar2(3) ///
	stats(r2_a N, fmt(3 0)) ///
	star(* 0.1 ** 0.05 *** 0.01)

	
/*
# ---------------
# LM Positive DID
# ---------------
*/

est clear
eststo: qui reg lm_positive treated post treated_post num_words, vce(cluster gvkey) 
eststo: qui reg lm_positive treated post treated_post num_words surprise-capex, vce(cluster gvkey) 
eststo: qui reghdfe lm_positive treated post treated_post num_words surprise-capex, absorb(year) vce(cluster gvkey)
eststo: qui reghdfe lm_positive treated post treated_post num_words surprise-capex, absorb(year gvkey) vce(cluster gvkey)

esttab using "3_output/stata/did_lm_positive.csv", replace ///
	t(2) b(3) ar2(3) ///
	stats(r2_a N, fmt(3 0)) ///
	star(* 0.1 ** 0.05 *** 0.01)
