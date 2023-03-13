# ml_experimentation_framework

Train model with

```
train_model(model_class = get_model("ModelImpl1"),
            model_params= {},
            feature_generator_class=get_feature_generator("FeatureGeneratorImpl1"),
            dataset_class=get_data_access_object("DataAccessObjectImpl1"),
            dataset_params={}
)
```

- ML model training process, at high level, consists of `retrieving dataset`, `generating feature`, `training`(hyperparameter serach, fit).
- Each of the steps will be represented with common interface but will be inherted to be implemented differented. e.g. Any algorithm can be implemented by subclassing from base Model.
- Different Feature Generation subclasses can be applied to the same underlying datasets.
- Different Models can be applied to the same underlying features sets.
- Training result will need to be stored along with unique `run_id`.

- Common Interface for `model`s
  - Regardless of internal implementation, it should follow the common interface.
  - In case different internal implementation needs to be experimented and compared, multiple subclasses can be created and compared e.g. `LogisticRegressionSkLearn` vs `LogicsRegressionKeras`, both of which are inherited from the base `Model` class.

Reproduce with

```
train_model(run_id = "example_run_id"
)
```

- Version control will leverage `git_hash`. Based on the specific `git_hash`, status of `model `, `data_access_object`, and `feature_generator` modules will be loaded.
- Parameters provided will need to be loaded in order to fully reproduce the training.
- Note that all the relevant logic & parameters of `data_access_object` will be able to reproduce itself, but under the assumption that underlying data has not changed. But since the underlying data could change(historical reruns, fixing bugs that are found later, and etc), in order to fully reproduce the training, the training dataset will need to be stored as artifact. This comes with side effect of large & potentially duplicative data.
- `train_model`, when given `run_id` for reproducing previous training, Relevant `git_hash` should be loaded to retrieve relevant classes(`model`, `data_access_object`, and `feature_generator`) in order to reproduce the training.

Output table of the training will roughly look like:

```
model_runs
├── run_id (unique identifier for each model run)
├── model_class (type of model used, e.g. random forest, neural network, logistic regression)
├── hyperparameters (dictionary of hyperparameters used for this model run)
├── githash (version of the source code)
├── feature_generator_class (class used for feature generation/preprocessor step)
├── dataset_class (class name for abstraction built to load data from its sources)
├── metrics (dictionary of performance metrics logged for this model run)
├── artifacts (directory of saved model artifacts)
├── start_time (start time of the model training)
└── end_time (end time of the model training)
```

Experimentation Result Comparison

- Friendly user interface to compare commonalities and difference between previously run trainig processes with choice of performance metric to compare.
