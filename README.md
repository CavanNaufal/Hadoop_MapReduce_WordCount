<h1 align="center">Group 2 - Sistem Basis Data - 02</h1>
<h3 align="center">
  <a href="https://github.com/CavanNaufal">
    Muhammad Cavan Naufal Azizi
  </a>
  - 2106702730
</h3>
<h3 align="center">
  <a href="https://github.com/kresnarmdn">
    RBS Kresna Ramdani Galih
  </a>
  - 2106702610
</h3>
<h3 align="center">
  <a href="https://github.com/JGDoubleP">
    Jeremy Ganda Pandapotan
  </a>
  - 2106731573
</h3>
<h3 align="center">
  <a href="https://github.com/">
    Fahrezy Hutapea
  </a>
  - 2106731466
</h3>
<p>All of us are undergradute student of Computer Engineering Major, Department of Electrical Engineering, Faculty of Engineering, Universitas Indonesia.</p>

# **Hadoop WordCount**
This work was developed as group assignment for **Sistem Basis Data** course from Electrical Engineering Department, Faculty of Engineering, Universitas Indonesia.

<p align='center'><img src="https://itwadi.com/files/Hadoop.png"/></p>

## What is Hadoop ?
[Apache Hadoop](https://hadoop.apache.org/) is a collection of open-source software utilities that facilitate using a network of many computers to solve problems involving massive amounts of data and computation. It provides massive storage for any kind of data, enormous processing power and the ability to handle virtually limitless concurrent tasks or jobs.

## What is MapReduce ?
[MapReduce](https://en.wikipedia.org/wiki/MapReduce) is a **programming model** and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

<p align='center'><img src="https://dz2cdn1.dzone.com/storage/temp/12774199-mapreduce-process.png"/></p>

A **MapReduce job** usually **splits** the input data-set into independent chunks which are processed by the *map tasks* in a completely *parallel* manner. The framework **sorts** the outputs of the maps, which are then input to the *reduce tasks* **(Duh ! now the name Map --> Reduce is obvious )**. Typically both the input and the output of the job are stored in a file-system. The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks.

## How I work with all that fancy stuff ?
Applications specify the **input/output** locations and supply **map and reduce functions** via implementations of appropriate interfaces and/or abstract-classes (minimum requiremnets). These, and other job parameters, comprise the **job configuration**.
The Hadoop job client then **submits the job** (jar/executable etc.) **and configuration** to the *ResourceManager* which then assumes the responsibility of distributing the software/configuration to the workers, scheduling tasks and monitoring them, providing status and diagnostic information to the job-client.

All in all, pick application then input dataset and provide Map and Reduce Functions following a Map Reduce programming model.

### Inputs and Outputs 
One of the most important concepts to grasp is that MapReduce framework operates ONLY on **<key, value> pairs**, that is, the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job.
The key and value type classes have to be serializable by the framework and hence need to implement the Writable interface. Also, the key classes have to implement the WritableComparable interface to facilitate sorting by the framework.

**Example:** In Java we use **IntWritable** instead of ~Integer~, and **Text** instead of ~String~.

We used text files from the [Gutenberg project](https://www.i3s.unice.fr/~jplozi/hadooplab_lsds_2015/datasets/), in Plain Text UTF-8 format as my input dataset.

## Hadoop: Setting up a Single Node Cluster.
1. Execute the following command to download Hadoop on machine: `wget https://downloads.apache.org/hadoop/common/hadoop-2.10.0/hadoop-2.10.0.tar.gz`

2. Extract the downloaded file using the command: `tar -xzvf hadoop-2.10.0.tar.gz`

3. Setup the downloaded Hadoop version on machine in a Pseudo Distributed mode. Follow these [steps](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation).


## The Application: WordCount

<p align='center'><img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/04/Map-only.png"/></p>

*Well...the name and the sourcecode says it all.* **WordCount** is a simple application that counts the number of occurrences of each word in a given input set. **(Hmm.. a really big one in that manner)**

### Workflow of MapReduce:

- **Splitting**: Splittling text to words. The splitting parameter can be anything.

- **Mapping**: Takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (Key-Value pair).

- **Intermediate splitting**:  The entire process in parallel on different clusters. In order to group them in “Reduce Phase” the similar KEY data should be on the same cluster.

- **Reduce**:  Takes the output from Map as an input and combines those data tuples into a smaller set of tuples.

- **Combining**: The last phase where all the data (individual result set from each cluster) is combined together to form a result.

We highly recommend reading the full in detail walk-through found in the [Official Map Reduce Hadoop Tutorial](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html#Example:_WordCount_v1.0). And then, the next step is to implement your own work for this application to get started wth Hadoop and Map Reduce. :book: :green_book:

## Installation Tutorial

### 1.  ```Access this oracle website below```
```
https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html
```

### 2.  ```Download Java Development Kit 8 (JDK 8) windows x64```

![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/90dbde65-8167-464d-b9ab-7105b74baa4e)




## Resources: 
1. [Hadoop Tutorial: Setting up a Single Node Cluster.](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)
2. [Hadoop Tutorial: MapReduce Tutorial.](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
3. [Word Count Program With MapReduce and Java Tutorial by Shital Kat](https://dzone.com/articles/word-count-hello-word-program-in-mapreduce)
