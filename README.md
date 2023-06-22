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
  <a href="https://github.com/fahrezyyh">
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


## Hadoop & Python WordCount Output
### Table
| Size/Type | Python(s) | Hadoop(s) | Ratio |
|     :---:    |     :---:      |     :---:     |     :---:     |
| 1 MB        | 0.137     | 30.242    | 0.00453    |
| 100 MB     | 27.021       | 62.245      | 0.43411    |
| 200 MB     | 42.617       | 71.460      | 0.59637    |
| 500 MB     | 243.039       | 93.246      | 2.60643    |
| 1000 MB     | 1905.303       | 197.669      | 9.63885    |

### Graph
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/c655b25c-619b-492b-906f-be74d3451f8f)
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/ec430f00-9315-4474-abc4-8fb1bad061d0)

### Dataset
[Gutenberg project](https://www.i3s.unice.fr/~jplozi/hadooplab_lsds_2015/datasets/)

---


## Installation Tutorial

### 1.  ```Access this oracle website below```
```
https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html
```

### 2.  ```Download Java Development Kit 8 (JDK 8) windows x64```

![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/90dbde65-8167-464d-b9ab-7105b74baa4e)

### 3.  ```Set Environment Variables (Java)```
```
Add it to the system variable with the name JAVA_HOME, then with the value, namely the path of the installed java folder.
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/8f2c7d08-8d2e-429a-b77d-5303fa151ff9)
```
and then add /bin to the variable path
```
### 4.  ```Java Verification```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/5db66a20-feb2-4fd7-a4cc-c2321cdac163)

### 5.  ```Download Hadoop (Recommended ver. 3.2.2)```
```
https://archive.apache.org/dist/hadoop/common/ 
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/082a3f7b-11df-4419-9afe-0e568e10bf45)

```
Choose hadoop-3.2.2.tar.gz. then extract the hadoop file that has been downloaded
```

### 6.  ```Set Environment Variables (Hadoop)```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/0b7ecfc2-e728-4b43-8177-f0d03a21196c)

```
Then add /bin and /sbin to the Path variable.
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/991cbac8-1039-466e-ac3e-65fecfd2709d)

### 7.  ```Add a data folder to the extracted hadoop file```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/26635dfc-54c7-4a18-bf0c-2c75d8fc2d20)

```
and then in the data folder create two folders named namenode and datanode.
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/eb2606f4-309b-4742-b482-97becaf64579)

### 8.  ```Edit core-site.xml, hdfs-site.xml, mapred-site.xml, dan yarn-site.xml```
etc/hadoop/core-site.xml :
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```
etc/hadoop/hdfs-site.xml :
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```
etc/hadoop/mapred-site.xml :
```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>
```
etc/hadoop/yarn-site.xml :
```
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```
### 9.  ```Edit Hadoop Env on hadoop env.cmd with the downloaded jdk folder path```
```
@rem
set JAVA_HOME = C:"\Program Files\Java\jdk-1.8"
```

### 10.  ```Download Patch file hadoop for Windows```
```
https://github.com/cdarlint/winutils 
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/4cf604e1-c16f-4d58-a690-475765cf7717)

### 11.  ```Extract the bin file then move it to the bin folder in the hadoop folder.```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/53536ec8-0e32-4cdf-b80a-121530b0258b)

### 12.  ```Hadoop Verification.```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/822aded6-3399-4cf4-a34d-289539e54780)

Setup the downloaded Hadoop version on machine in a Pseudo Distributed mode. Follow these [steps](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation).

---

## Hadoop WordCount (JAVA)

### 1.  ```Create Maven Project (Using IntelliJ) dengan Language Java dan Build System Maven..```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/0dc3c0a0-9a4c-40ac-82d6-f40adc9f895f)

### 2.  ```add dependencies at pom.xml..```
```
   <dependencies>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>3.2.2</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-mapreduce-client-core</artifactId>
            <version>3.2.2</version>
        </dependency>
    </dependencies>

```

### 3.  ```Create Package and inside the package create a java file containing the wordcount code.```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/2ccba58d-f7e7-49e3-a5f3-340015ac2c75)

The code can be seen in the link:
```
https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html#Source_Code
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/ab345efa-0db9-4053-b131-597fb2386791)

### 4.  ```Then create a jar file with maven.```
```mvn clean```<br />
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/a90118d1-3f16-44f4-94f4-68202f64be31) <br />
```mvn install```<br />
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/585b8d91-01a8-427f-8bfd-509abb2702a7)
<br />
Maka pada target folder terdapat file jar.	<br />
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/c6cc9369-9f8f-4265-b564-aa2cff402a9a)
<br />
### 5.  ```Create input file (.txt)```
example : <br />
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/28db6b2a-d718-41da-b380-229e22f1b1f1)

### 6.  ```run cmd as administrator then cd to the sbin folder```<br />
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/1430c429-5591-4aa2-8e66-79b6f14529ea)

### 7.  ```Run Hadoop and jps to make sure hadoop runs properly.start-all. cmd```<br />
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/06ae7964-3c9f-47cc-882a-2e7b69be37ff)

```hadoop fs -mkdir /testinp```<br />
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/96364da6-7d1f-4d8f-ae2d-b12cbd4991f7)

```
hadoop fs -put "D:\Universitas Indonesia\Semester 4\Sistem Basis Data\Hadoop\1M.txt" /testinp
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/9bc3de69-dfbc-4a5f-b164-e863ed2f2d89)

```
hadoop jar "D:\Universitas Indonesia\Semester 4\Sistem Basis Data\Hadoop\Hadoop_WordCount\target\Hadoop_WordCount-1.0-SNAPSHOT.jar" org.wordcount.WordCount /testinp /output_test
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/306c45eb-429c-42bc-b099-38c59eeca2b6)

### 8.  ```Output```
```
hadoop fs -cat /output_test/part-r-00000
```
![image](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/87458424/11bed839-f27f-4152-9b83-a0d0ab432f3c)

```
stop-all.cmd
```
![Screenshot 2023-06-21 175438](https://github.com/CavanNaufal/Hadoop_MapReduce_WordCount/assets/88435892/ba60652d-06f6-41d3-aa9c-109cb396bce0)

## Resources: 
1. [Hadoop Tutorial: Setting up a Single Node Cluster.](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)
2. [Hadoop Tutorial: MapReduce Tutorial.](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
3. [Word Count Program With MapReduce and Java Tutorial by Shital Kat](https://dzone.com/articles/word-count-hello-word-program-in-mapreduce)
