<h1 align="center">Movie_Analytics-internship_project</h1>

### Problem Statement:<br>
The objective is to develop a big data project utilizing Apache Spark and python to address analytical queries on the semi-structured MovieLens dataset, comprising a million records. The tasks involve the use of Spark RDD, Spark SQL, and Spark DataFrames, implemented through the Spark shell using Python API. The primary focus is on performing comprehensive analyses to extract valuable insights about users and movies, leveraging various Spark APIs.

### Architecture:<br>
<img align="center" alt="" src="https://raw.githubusercontent.com/sai019/Movie_Analytics-internship_project/main/Images/Movie-Analytics%20Architecture.gif" />

### Approach: <br>
By retrieving data from a web URL in compressed zip format, unzipping it locally, and transferring delimited data files to a 'raw_data' folder in Azure Data Lake Storage Gen2 using Python. In Azure Databricks, the raw data undergoes transformations with PySpark to ensure cleanliness and quality. Cleaned data is stored in a 'transformed_data' folder for easy access. Analytics are then conducted on this transformed data using PySpark SQL and DataFrames in Azure Databricks, providing valuable insights. This approach optimizes the data pipeline, improving data quality and analytical capabilities.

### Cloning this project:<br> 
```
git clone https://github.com/sai019/Movie_Analytics-internship_project.git
```
```
cd <project directory>
```
```
pip install -r requirements.txt
```
All set now you cloned this project successfully.

### Contributors:<br>
- SAI KUMAR

### Thank You
