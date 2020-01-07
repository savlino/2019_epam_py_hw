"""
Module created to simlpify data science work.
First, you obliged to choose model from given list.

    *WARNING: module requires "inquirer" module

Currently module provides next models:
    - decision tree,
    - random forest,
    - gradient boosting,
    - principal component analysis
Second, output will show you default parameters for chosen module.
If you'll decide to correct them, do the following:
    1. type parameter's name, according to output list and hit 'return'
    2. put new value for parameter you chose, hit 'return'
If you're happy with default parameters - just hit 'return'.

Module accepts next types of datasets:
.csv, .parquet, .json, .tar.gz, .tar.bz2, .zip

By default dataset is taken from module's current folder.
Model's training results by default will output to module's current folder.

Optionaly, you can specify path to desirable dataset
or containing folder as argument to console.
As following argument you can direct
where you want your output /path to folder or url/.
"""

import sys
import os
import os.path
import inquirer

dataset_location = os.getcwd()
model_output = os.getcwd()
inp_data = ''

possible_extentions = [
    'csv', 'parquet', 'json', 'tar.gz', 'tar.bz2', 'zip'
]

if len(sys.argv) > 2:
    if os.path.isfile(sys.argv[1]) \
    and sys.argv[1].split('.')[-1] in possible_extentions:
        inp_data = sys.argv[1].split('/')[-1]
        model_output = sys.argv[2]
    else:
        dataset_location = sys.argv[1]
        model_output = sys.argv[2]
elif len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]) \
    and sys.argv[1].split('.')[-1] in possible_extentions:
        inp_data = sys.argv[1].split('/')[-1]
    else:
        dataset_location = sys.argv[1]

if inp_data == '':
    for _, _, files in os.walk(dataset_location):
        for f in files:
            if f.split('.')[-1] in possible_extentions:
                inp_data = f.split('/')[-1]
                break
    raise FileNotFoundError('wrong path or unsupported file type')

available_models = [
    'Decision tree',
    'Random forest',
    'Gradient boosting',
    'Principal component analysis'
]

decision_tree_params = {
    'train/test proportion': 0.2,
    'criterion': 'gini',     # gini/entropy
    'splitter': 'best',
    'max_depth': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1,

    'random_state': None,
    'max_features': None,
    'class_weight': None
}

random_forest_params = {
    'train/test proportion': 0.2,
    'n_estimators': 15,
    'max_features': 1,
    'bootstrap': True,
    'criterion': 'mse',
    'max_depth': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1,

    'random_state': None,
    'min_weight_fraction_leaf': 0,
    'max_leaf_nodes': None,
    'min_impurity_decrease': 0
}

gradient_boosting_params = {
    'train/test proportion': 0.2,
    'n_extimators': 100,
    'loss': 'deviance',     # deviance/exponential
    'learning_rate': 0.1,
    'subsample': 1,
    'random_state': None,
    'max_features': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1,

    'min_weight_fraction_leaf': 0,
    'max_leaf_nodes': None,
    'min_impurity_decrease': 0
}

principal_component_analysis_params = {
    'train/test proportion': 0.2,
    'n_components': None,

    'copy': True,
    'whiten': False,
    'random_state': None
}


def presentation(from_dict):
    """
    inner function for presenting actual model's current parameters
    """
    for key in from_dict:
        print(f'    {key}={from_dict[key]}')


def interface():
    """
    function carries out guidance through model training process
    """
    model_ask = [
        inquirer.List('model',
                      message="Which model would you chooze?",
                      choices=available_models,
                      )]

    answers = inquirer.prompt(model_ask)
    print(f'current model is {answers["model"]}\ncurrent parameters set:')

    if answers['model'] == 'Decision tree':
        work_model_params = decision_tree_params
    elif answers['model'] == 'Random forest':
        work_model_params = random_forest_params
    elif answers['model'] == 'Gradient boosting':
        work_model_params = gradient_boosting_params
    elif answers['model'] == 'Principal component analysis':
        work_model_params = principal_component_analysis_params

    param = 'some param'
    while param.lower() != '':
        param = input(
            f" {presentation(work_model_params)}\
            \nif you would like to change any of them, \
            \ntype it's name or press 'return' to proceed > "
        )

        if param in set(work_model_params):
            work_model_params[param] = input(f'set value for {param} > ')
            print(param + ' changed')

    return answers["model"], work_model_params


def data_magik(model, params, dataset, output_path=os.getcwd()):
    """
    Function provides data science magic by chosen method and given parameters
    """
    print(f"you've got {model} science now\n")


usr_input = ''

while usr_input.lower() != 'quit':
    usr_input = input(
    "-----------------<<>>-----------------\n\
    to begin model training command 'start',\n\
    to get help command 'help',\n\
    to leave program command 'quit'\n\
    >> "
    )

    if usr_input == 'start':
        test_model, test_params = interface()
        data_magik(test_model, test_params, inp_data, model_output)

    if usr_input == 'help':
        help('__main__')

sys.exit()
