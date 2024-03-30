<h1 align="center">Movie_Analytics-internship_project</h1>

### Problem Statement:<br>
The objective is to develop a big data project utilizing Apache Spark and Python to address analytical queries on the semi-structured MovieLens dataset, comprising a million records. The tasks involve using Spark RDD, Spark SQL, and Spark DataFrames, implemented through the Spark shell using Python API. The primary focus is on performing comprehensive analyses to extract valuable insights about users and movies, leveraging various Spark APIs.

### Architecture:<br>
<img align="center" alt="" src="https://raw.githubusercontent.com/sai019/Movie_Analytics-internship_project/main/Images/Movie-Analytics%20Architecture.gif" />

### Project Work Flow:<be>

Project Setup and Data Retrieval: 
- Set up the required development environment, including Azure Databricks and Azure Data Lake Storage Gen2.
- Configure access permissions and authentication mechanisms for accessing Azure services.
- Install necessary Python libraries for data retrieval such as requests.
- Run ``` src/components/extract_Datazip_to_local.py ``` script to retrieve the compressed zip file from the specified web URL.
- Store the downloaded files locally.

Data Transfer to Azure Data Lake Storage Gen2:
- Use Azure Storage SDK for Python to establish a connection to Azure Data Lake Storage Gen2.
- Run ``` src/components/files_upload_to_datalake.py ``` Upload the extracted delimited data files to the 'raw_data' folder in Azure Data Lake Storage Gen2.

Data Transformation with PySpark:
- Set up an Azure Databricks notebook or script to ingest data from the 'raw_data' folder.
- Use PySpark to perform data transformations and cleansing operations as required.
- Handle missing values, data type conversions, and other data quality issues.
- Implement transformations to conform to a predefined schema or data model.

Storage of Cleaned Data:
- Once data transformations are complete, store the cleaned data in a 'transformed_data' folder within Azure Data Lake Storage Gen2.
- Maintain the folder structure and naming conventions for organized data storage.
  
Analytics with PySpark SQL and DataFrames:
- Utilize PySpark SQL and DataFrames within Azure Databricks to conduct transformed data analytics.
- Write SQL queries or DataFrame operations to extract insights and perform analytical computations.

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

### Thank You
