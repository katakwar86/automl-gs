# automl-gs

Give an input CSV file and a target field you want to predict to automl-gs, and get a trained high-performing machine learning or deep learning model plus customized code allowing you to integrate that model into any prediction workflow.

Nowadays, the cost of computing many different models and hyperparameters is much lower than the oppertunity cost of an data scientist's time. automl-gs is a Python 3 module designed to abstract away the common approaches to transforming tabular data, architecting machine learning/deep learning models, and performing random hyperparameter searches to identify the best-performing model. This allows data scientists and researchers to better utilize their time on model performance optimization.

* Generates native Python code; no platform lock-in, and no need to use automl-gs after the model script is created.
* Train model configurations super-fast *for free* using a **TPU** in Google Colaboratory.
* Each part of the generated model pipeline is its own  function w/ docstrings, making it much easier to integrate into production workflows.
* Extremely detailed metrics reporting for every trial stored in a CSV, allowing you to identify and visualize model strengths and weaknesses.
* Correct serialization of data pipeline encoders on disk (i.e. no pickled Python objects!)
* Retrain the generated model on new data without making any code/pipeline changes.
* Quit the hyperparameter search at any time, as the results are saved after each trial.

The models generated by automl-gs are intended to give a very strong *baseline* for solving a given problem; they're not the end-all-be-all that often accompanies the AutoML hype, but the results are easily tweakable to improve from the baseline.

## Framework Support

Currently automl-gs supports the generation of models for regression and classification problems using the following Python frameworks:

* TensorFlow (via `tf.keras`)
* XGBoost
* Catboost
* scikit-learn:
  * LinearRegression

## How it Works

automl-gs loads a given CSV and infers the data type of each column to be fed into the model. Then it tries a ETL strategy for each column field as determined by the hyperparameters; for example, a Datetime field has its `hour` and `dayofweek` binary-encoded by default, but hyperparameters may dictate the encoding of `month`, `year`, and `holiday` as additional model fields. automl-gs then creates a statistical model with the specified framework. Both the model ETL functions and model construction functions are saved as a generated Python script.

automl-gs then runs the generated training script as if it was a typical user. Once the model is trained, automl-gs saves the training results in its own CSV, along with all the hyperparameters used to train the model. automl-gs then repeats the task with another set of hyperparameters, until the specified number of trials is hit or the user kills the script.

The best model Python script is kept after each trial, which can then easily be integrated into other scripts, or run directly to get the prediction results on a new dataset.

## Helpful Notes

* *It is the user's responsibility to ensure the input dataset is high-quality.* No model hyperparameter search will provide good research on flawed/unbalanced datasets.

## Future Work

### Top Priority

* Results visualization (via `plotnine`)
* Fix redundant code (both parent and generated code)
* Native Polyaxon/Kubernetes Support
* Image field support (both as a CSV column field, and a special flow mode to take advantage of hyperparameter tuning)
* PyTorch model generation.

### Elsework

* Generate script given an explicit set of hyperparameters
* Minimize unneeded imports in the generated files.
* Bayesian hyperparameter search for standalone version.
* Training results visualization after completion.
* Support for generating model code for R.
* Localization (for generated code comments)
* TensorBoard support?
* Tool for generating a Flask/Starlette REST API from a trained model script
* Secondary progress bars for epoch progress in each trial.

## Maintainer/Creator

Max Woolf ([@minimaxir](http://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT