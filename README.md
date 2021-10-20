In this Repo, we used GitHub Actions and used Python Application.

https://medium.com/swlh/automate-python-testing-with-github-actions-7926b5d8a865

It creates folder .github/workflows/python-app.yml

We mentioned to run pipelines on python-app.yml whenever there is a push on any branch.

Used python library pytest to run test-cases in the pipeline.

DVC

We also used DVC for basic ML version control. 

https://medium.com/swlh/automate-python-testing-with-github-actions-7926b5d8a865

### Below shows how DVC works.

downloaded git repo:

```dvc
git clone https://github.com/iterative/example-versioning.git
$ cd example-versioning
```

Once you cloned, delete their .git folder and use our github account and our remote repo..

Created virtual environment:

I used : python -m venv env

Then activated it by cd into env/Scripts and use activate.bat

Then pip install -r requirements.txt for packages

## First model version

Now that we're done with preparations, let's add some data and then train the first model. We'll capture everything with DVC, including the input dataset and model [metrics](https://dvc.org/doc/command-reference/metrics).

```dvc
$ dvc get https://github.com/iterative/dataset-registry \
          tutorials/versioning/data.zip
$ unzip -q data.zip
$ rm -f data.zip
```

Once downloaded and unzipped, we do ‘dvc init and dvc add data’ - so the data folder will be tracked by dvc and it will be automatically added to .gitignore file and it will not get pushed to repo..

For training : python train.py which returns model.h5

add that too to dvc : dvc add model.h5

When you add something to dvc, it creates .dvc files for those added like data.dvc, model.h5.dvc..

Now you can add these to git and commit and tag : 

Let's commit the current state:

```dvc
$ git add data.dvc model.h5.dvc metrics.csv .gitignore
$ git commit -m "First model, trained with 1000 images"
$ git tag -a "v1.0" -m "model v1.0, 1000 images"
```

#When we tag here and continue coding, say we are tagging v2.0 after code changes.. its more likely a new #branch in git.

#In local we can checkout to different tags and get that respective data, code used that time..

#But when we try to push, we will be asked to create a branch..



## Second model version

Let's imagine that our image dataset doubles in size. The next command extracts 500 new cat images and 500 new dog images into `data/train`:

```dvc
$ dvc get https://github.com/iterative/dataset-registry \
          tutorials/versioning/new-labels.zip
$ unzip -q new-labels.zip
$ rm -f new-labels.zip
```

For simplicity's sake, we keep the validation subset the same. Now our dataset has 2000 images for training and 800 images for validation, with a total size of 67 MB:

```text
data
├── train
│   ├── dogs
│   │   ├── dog.1.jpg
│   │   ├── ...
│   │   └── dog.1000.jpg
│   └── cats
│       ├── cat.1.jpg
│       ├── ...
│       └── cat.1000.jpg
└── validation
   ├── dogs
   │   ├── dog.1001.jpg
   │   ├── ...
   │   └── dog.1400.jpg
   └── cats
       ├── cat.1001.jpg
       ├── ...
       └── cat.1400.jpg
```

We will now want to leverage these new labels and retrain the model:

```dvc
$ dvc add data
$ python train.py
$ dvc add model.h5
```

Let's commit the second version:

```dvc
$ git add data.dvc model.h5.dvc metrics.csv
$ git commit -m "Second model, trained with 2000 images"
$ git tag -a "v2.0" -m "model v2.0, 2000 images"
```

That's it! We've tracked a second version of the dataset, model, and metrics in DVC and committed the [`.dvc`](https://dvc.org/doc/user-guide/project-structure/dvc-files) files that point to them with Git. Let's now look at how DVC can help us go back to the previous version if we need to.

## Switching between workspace versions

The DVC command that helps get a specific committed version of data is designed to be similar to `git checkout`. All we need to do in our case is to additionally run [`dvc checkout`](https://dvc.org/doc/command-reference/checkout) to get the right data into the workspace.

![img](https://dvc.org/img/versioning.png)

There are two ways of doing this: a full workspace checkout or checkout of a specific data or model file. Let's consider the full checkout first. It's pretty straightforward:

```dvc
$ git checkout v1.0
$ dvc checkout
```

These commands will restore the workspace to the first snapshot we made: code, data files, model, all of it. DVC optimizes this operation to avoid copying data or model files each time. So [`dvc checkout`](https://dvc.org/doc/command-reference/checkout) is quick even if you have large datasets, data files, or models.

On the other hand, if we want to keep the current code, but go back to the previous dataset version, we can target specific data, like this:

```dvc
$ git checkout v1.0 data.dvc
$ dvc checkout data.dvc
```

If you run `git status` you'll see that `data.dvc` is modified and currently points to the `v1.0` version of the dataset, while code and model files are from the `v2.0` tag.





