Theory: 
Abstract & overview of results:
@article{van2000coil,
  title={Coil challenge 2000 tasks and results: Predicting and explaining caravan policy ownership},
  author={van der Putten, Peter and de Ruiter, Michel and van Someren, Maarten},
  journal={Coil Challenge},
  volume={2000},
  year={2000}
}

Segmentation:
@article{qadadeh2018customers,
  title={Customers segmentation in the insurance company (TIC) dataset},
  author={Qadadeh, Wafa and Abdallah, Sherief},
  journal={Procedia computer science},
  volume={144},
  pages={277--290},
  year={2018},
  publisher={Elsevier}
}

Target group: Marketers
If the valuable but complex patterns which are detected by advanced intelligent techniques are not explained properly, 
 end users like marketers will still prefer the simple but crude and limited solutions.

Data exploration stuk:
analyze - consume - discover | attributes - one - distribution
analyze - consume - discover | attributes - many - correlation
Visualizaties: histogrammen, distributie en correlatie

Action: Discover
Target: Distribution/Correlation
Implementation: Histogram, distribution, correlation
Answer question: Can clear distinctions between data be found? Like, clustering by just 1 variable

Action: Discover
Target: Patterns
Implementation: Clustering
Answer question: Can you predict who would be interested in buying a caravan insurance policy?
- Visualize clusters with SOM. Scatter plots, etc

Action: Compare
Target: Features/Trends/Similarity
Implementation: - Comparing clusters by decision tree?
Answer question: Why are these customers interested in buying a caravan policy?

Naive bayes is the best


# JBI100-example-app

## About this app

You can use this as a basic template for your JBI100 visualization project.

## Requirements

* Python 3 (add it to your path (system variables) to make sure you can access it from the command prompt)
* Git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## How to run this app

We suggest you to create a virtual environment for running this app with Python 3. Clone this repository 
and open your terminal/command prompt in the root folder.


download a zip file of this folder, unzip it and copy it to a folder of choice on your computer

open a command prompt and run the following commands:

```
> cd <path to you folder of choice>\dashframework-main\dashframework-main 
> python -m venv venv

```
If python is not recognized use python3 instead

In Windows: 

```
> venv\Scripts\activate

```
In Unix system:
```
> source venv/bin/activate
```

(Instead of a python virtual environment you can also use an anaconda virtual environment.
 
Requirements:

• Anaconda (https://www.anaconda.com/) or Miniconda (https://docs.conda.io/en/latest/miniconda.html)

• The difference is that Anaconda has a user-friendly UI but requires a lot of space, and Miniconda is Command Prompt based, no UI, but requires considerably less space.

Then you should replace the lines: python -m venv venv and venv\Scripts\activate or source venv/bin/activate with the following:

```
> conda create -n yourenvname
> conda activate yourenvname
```
)

Install all required packages by running:
```
> pip install -r requirements.txt
```

Run this app locally with:
```
> python app.py
```
You will get a http link, open this in your browser to see the results. You can edit the code in any editor (e.g. Visual Studio Code) and if you save it you will see the results in the browser.

## Resources

* [Dash](https://dash.plot.ly/)
