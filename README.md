There are many proprietary and open source AutoML tools available. This project dives into just a few of them with the goal of getting you started with hands-on AutoML. 
Check out [this great site](https://github.com/hibayesian/awesome-automl-papers) by Mark Lin for an overview of AutoML.

## Suggested Actions

* #### Click on Jobs to see a history of batch jobs and associated metrics.
    * The first two runs are baseline runs of Logistic Regression and Random Forests. The other runs show each of the AutoML jobs respectively. Each run tracks accuracy on the two data sets used in this project:  Heart Disease and Breast Cancer classification. 


* #### Click on Files to check out the notebooks and data associated with this project.
* #### Fork this project to run the notebooks on your own. 
* #### Click on Workspaces and start a Jupyterlab workspace.

## Summary of top open source AutoML tools

#### TPOT

* Has a preset list of search space dictionaries to chose from, but it is a little involved to customize your own search space. 
* Easy to parallelize jobs. 
* Uses genetic algos for hyperparameter optimization. 
* Includes data processing in the optimization routines.
* Does not build ensembles, but finds the best model pipeline.

#### auto-sklearn
* Fits an ensemble of the best performing models. 
* Easy to parallelize jobs. 
* Hyperparameter optimization through SMAC (Bayesian Optimization in combination with a aggressive racing mechanism). 
* Does not offer fine-grained control over the search space.

#### MLBox
* Has the easiest way to define the search space for algos and hyperparameters. 
* Uses the hyperopt library for hyperameter optimization (leverages Random Search and Tree of Parzen Estimators).
* Has nice features for encoding and drift detection.
* No parallelization of jobs or time limit options. Slow.
* Documentation is not as mature.

#### AutoKeras
* Network architecture and hyperparameter search for deep learning powered by Neural Architecture Search (NAS).
* Auto-Keras also applies “network morphism” (keeping network functionality while changing the architecture) along with Bayesian optimization to guide the network morphism for more efficient neural network search.
* NAS typically requires many hours of computing to search for optimal parameters.
* Generally less accurate than hand-crafted nets by experts, but can point you in the right direction.

#### Google AutoML
* Picky on how the data file is organized.
* Very much a black box.
* Can optimize to a metric of choice.
* Option for stopping criteria based on a metric of choice and/or time.

#### Azure Automated ML
* More forgiving on data file organization.
* Can optimize to a metric of choice.
* Algorithms used are transparent.
* Ensembles are created.
* Only stopping criteria is time (1 hour min).

## Bonus Material

#### H2O Driverless.ai
* Reach out to "dan@dominodatalab.com" to get access to the Domino Environment (a docker image that Domino will spin up) that runs H2O.

#### Ludwig
* No-code/low-code deep learning using smart default templates. 
* Useful alternative to AutoKeras if you already know the direction you should go.
* [Blog](https://blog.dominodatalab.com/a-practitioners-guide-to-deep-learning-with-ludwig/)
* [Domino Project](https://try.dominodatalab.com/u/joshpoduska/Ludwig/overview)

#### Other Tools
* Check out this [spreadsheet](https://docs.google.com/spreadsheets/d/1KVtbJfBcjnh_0YIgfLyfROxDHtcw8QOafjTicjyiUxo/edit#gid=1849753649) from Paco Nathan listing the proprietary and open source AutoML tools available today.

 